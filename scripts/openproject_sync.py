#!/usr/bin/env python3
"""
OpenProject API v3 Headless Sync Script
======================================
This script provides a headless command-line utility and programmatic library
for managing projects, subprojects, descriptions, and work packages (tasks)
on OpenProject (https://project.pxg.studio) using the API v3 standard.

Features:
- Zero-dependency: Uses standard library `urllib` instead of `requests`.
- Programmatic & CLI: Exposes both an `OpenProjectAPI` class and command line entry.
- Gantt & WBS Sync: Parses Mermaid Gantt charts (start date, duration, dependency)
  and Markdown lists (WBS descriptions) and syncs them to OpenProject as tasks.
- Dynamic Discovery: Discovers project types and maps status values automatically.
- Idempotency & Conflict Resolution: Matches tasks via `[ID]` prefix and tracks
  `lockVersion` for safe updates.

Usage:
  export OPENPROJECT_URL="https://project.pxg.studio"
  export OPENPROJECT_TOKEN="your_api_token"
  
  # Test connection
  ./openproject_sync.py --action test
  
  # Create a project
  ./openproject_sync.py --action create --name "QHS_CORE" --identifier "qhs-core"
  
  # Update description from Markdown file
  ./openproject_sync.py --action update-desc --project-id 6 --file docs/architecture/05-governance-timeline.md
  
  # Sync Gantt and WBS tasks (dry-run)
  ./openproject_sync.py --action sync-tasks --project-id 6 --file docs/architecture/06-detailed-gantt.md --dry-run
  
  # Sync Gantt and WBS tasks (live execution)
  ./openproject_sync.py --action sync-tasks --project-id 6 --file docs/architecture/06-detailed-gantt.md
"""

import os
import sys
import re
import json
import base64
import argparse
from datetime import datetime, timedelta
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

class OpenProjectAPI:
    """Class wrapper for headless communication with the OpenProject API v3."""
    
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = self._get_auth_headers()

    def _get_auth_headers(self):
        """Generates HTTP Basic Auth headers for OpenProject API v3."""
        auth_str = f"apikey:{self.token}"
        auth_bytes = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
        return {
            "Authorization": f"Basic {auth_bytes}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def make_request(self, endpoint, method="GET", data=None):
        """Executes a request to OpenProject API using standard urllib."""
        url = f"{self.base_url}{endpoint}"
        if data:
            data_bytes = json.dumps(data).encode("utf-8")
        else:
            data_bytes = None

        req = Request(url, method=method, headers=self.headers, data=data_bytes)
        try:
            with urlopen(req, timeout=20) as response:
                res_data = response.read().decode("utf-8")
                return response.status, json.loads(res_data) if res_data else {}
        except HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                parsed_error = json.loads(error_body)
                print(f"[-] API Error ({e.code}) on {method} {endpoint}: {parsed_error.get('message', error_body)}")
                if 'errors' in parsed_error:
                    print(f"    Details: {parsed_error['errors']}")
            except Exception:
                print(f"[-] HTTP Error ({e.code}) on {method} {endpoint}: {error_body}")
            return e.code, {}
        except URLError as e:
            print(f"[-] Connection Error on {method} {endpoint}: {e.reason}")
            sys.exit(1)

    def test_connection(self):
        """Tests the connection and authentication with the API."""
        print(f"[*] Testing connection to: {self.base_url}/api/v3/users/me")
        status, res = self.make_request("/api/v3/users/me")
        if status == 200:
            print(f"[+] Connected successfully! Authenticated user: {res.get('name')} (ID: {res.get('id')})")
            return True
        else:
            print(f"[-] Authentication failed (Status: {status})")
            return False

    def create_project(self, name, identifier, parent_id=None):
        """Creates a project or subproject."""
        payload = {
            "name": name,
            "identifier": identifier,
            "public": False
        }
        
        if parent_id:
            payload["_links"] = {
                "parent": {
                    "href": f"/api/v3/projects/{parent_id}"
                }
            }
            print(f"[*] Creating subproject '{name}' under parent project ID: {parent_id}")
        else:
            print(f"[*] Creating top-level project '{name}'")

        status, res = self.make_request("/api/v3/projects", method="POST", data=payload)
        if status == 201:
            print(f"[+] Project created successfully!")
            print(f"    Name: {res.get('name')}")
            print(f"    ID: {res.get('id')}")
            print(f"    Identifier: {res.get('identifier')}")
            return res.get('id')
        else:
            print(f"[-] Failed to create project (Status: {status})")
            return None

    def update_project_description(self, project_id, markdown_content):
        """Updates the description of a project."""
        payload = {
            "description": {
                "format": "markdown",
                "raw": markdown_content.strip()
            }
        }
        print(f"[*] Updating description for project ID: {project_id}")
        status, res = self.make_request(f"/api/v3/projects/{project_id}", method="PATCH", data=payload)
        if status == 200:
            print(f"[+] Project description updated successfully.")
            return True
        else:
            print(f"[-] Failed to update description (Status: {status})")
            return False

    def fetch_statuses(self):
        """Fetches all work package statuses from OpenProject and returns a lowercased map to href."""
        status, res = self.make_request("/api/v3/statuses")
        if status != 200:
            print("[-] Failed to fetch statuses.")
            return {}
        
        elements = res.get("_embedded", {}).get("elements", [])
        mapping = {}
        for elem in elements:
            name = elem.get("name", "").lower()
            href = elem.get("_links", {}).get("self", {}).get("href")
            mapping[name] = href
        return mapping

    def get_status_link(self, status_name, status_mapping):
        """Resolves a generic status ('done', 'active', 'new') to an OpenProject status API resource link."""
        if status_name == "done":
            for name in ["closed", "done", "resolved", "completed"]:
                if name in status_mapping:
                    return status_mapping[name]
        elif status_name == "active":
            for name in ["in progress", "active", "in_progress", "in-progress", "development"]:
                if name in status_mapping:
                    return status_mapping[name]
        
        # Fallbacks for 'new'
        for name in ["new", "open", "specification", "draft"]:
            if name in status_mapping:
                return status_mapping[name]
                
        if status_mapping:
            return list(status_mapping.values())[0]
        return None

    def fetch_task_type_link(self, project_id):
        """Discovers the type resource link for Tasks dynamically."""
        status, res = self.make_request(f"/api/v3/projects/{project_id}/types")
        if status != 200:
            status, res = self.make_request("/api/v3/types")
            
        if status == 200:
            elements = res.get("_embedded", {}).get("elements", [])
            for elem in elements:
                name = elem.get("name", "").lower()
                if name in ["task", "work package", "work_package", "todo"]:
                    return elem.get("_links", {}).get("self", {}).get("href")
            if elements:
                return elements[0].get("_links", {}).get("self", {}).get("href")
        return "/api/v3/types/1"  # Hard fallback

    def fetch_existing_work_packages(self, project_id):
        """Fetches all work packages in the project and maps them by their parsed ID prefix."""
        endpoint = f"/api/v3/projects/{project_id}/work_packages?pageSize=500"
        status, res = self.make_request(endpoint)
        if status != 200:
            print(f"[-] Failed to fetch existing work packages (Status: {status})")
            return {}
        
        elements = res.get("_embedded", {}).get("elements", [])
        existing = {}
        for elem in elements:
            subject = elem.get("subject", "")
            match = re.match(r'^\[([a-zA-Z0-9_]+)\]', subject)
            if match:
                task_id = match.group(1)
                existing[task_id] = {
                    "wp_id": elem.get("id"),
                    "subject": subject,
                    "start_date": elem.get("startDate"),
                    "due_date": elem.get("dueDate"),
                    "status_href": elem.get("_links", {}).get("status", {}).get("href"),
                    "description_raw": elem.get("description", {}).get("raw", ""),
                    "lock_version": elem.get("lockVersion")
                }
        return existing

    def create_work_package(self, project_id, subject, start_date, due_date, description, type_href, status_href):
        """Creates a new work package in the project."""
        payload = {
            "subject": subject,
            "startDate": start_date.strftime("%Y-%m-%d") if start_date else None,
            "dueDate": due_date.strftime("%Y-%m-%d") if due_date else None,
            "description": {
                "format": "markdown",
                "raw": description.strip()
            },
            "_links": {
                "type": {"href": type_href}
            }
        }
        if status_href:
            payload["_links"]["status"] = {"href": status_href}

        status, res = self.make_request(f"/api/v3/projects/{project_id}/work_packages", method="POST", data=payload)
        return status == 201

    def update_work_package(self, wp_id, lock_version, updates):
        """Updates an existing work package with conflict resolution (lockVersion)."""
        payload = {
            "lockVersion": lock_version
        }
        payload.update(updates)
        status, res = self.make_request(f"/api/v3/work_packages/{wp_id}", method="PATCH", data=payload)
        return status == 200


def parse_markdown_file(file_path, default_start_date_str="2026-05-14"):
    """Parses a Markdown planning file to extract Mermaid Gantt tasks and WBS descriptions."""
    if not os.path.exists(file_path):
        print(f"[-] File not found: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Parse Mermaid Gantt
    tasks = {}
    gantt_match = re.search(r'```mermaid\s*\ngantt(.*?)\n```', content, re.DOTALL | re.IGNORECASE)
    if gantt_match:
        gantt_code = gantt_match.group(1)
        current_section = "General"
        for line in gantt_code.split('\n'):
            line = line.strip()
            if not line or line.startswith('title') or line.startswith('dateFormat') or line.startswith('axisFormat'):
                continue
            if line.startswith('section'):
                current_section = line.replace('section', '', 1).strip()
                continue
            
            # Format: Subject : modifiers, ID, start, duration
            if ':' in line:
                parts = line.split(':', 1)
                subject = parts[0].strip()
                rhs = parts[1].strip()
                args = [x.strip() for x in rhs.split(',')]
                
                if len(args) >= 3:
                    modifiers = []
                    idx = 0
                    if args[0] in ['done', 'active', 'crit'] or (args[0] == 'active' and args[1] == 'crit'):
                        modifiers = [args[0]]
                        if args[1] == 'crit':
                            modifiers.append(args[1])
                            idx = 2
                        else:
                            idx = 1
                    
                    if len(args) - idx >= 3:
                        task_id = args[idx]
                        start_raw = args[idx+1]
                        duration_raw = args[idx+2]
                        
                        status = "new"
                        if "done" in modifiers:
                            status = "done"
                        elif "active" in modifiers:
                            status = "active"
                            
                        tasks[task_id] = {
                            "id": task_id,
                            "subject": subject,
                            "status": status,
                            "start_raw": start_raw,
                            "duration_raw": duration_raw,
                            "section": current_section,
                            "description": ""
                        }
                        
    # 2. Resolve start/due dates
    default_start = datetime.strptime(default_start_date_str, "%Y-%m-%d")
    
    # First pass: resolve absolute dates
    for task_id, task in tasks.items():
        if re.match(r'^\d{4}-\d{2}-\d{2}$', task["start_raw"]):
            task["start_date"] = datetime.strptime(task["start_raw"], "%Y-%m-%d")
            dur_match = re.match(r'^(\d+)(d|w)$', task["duration_raw"])
            days = 1
            if dur_match:
                val, unit = dur_match.groups()
                days = int(val) * (7 if unit == 'w' else 1)
            task["due_date"] = task["start_date"] + timedelta(days=days)
            
    # Second pass: resolve dependencies (iterative lookup)
    for _ in range(len(tasks)):
        resolved_any = False
        for task_id, task in tasks.items():
            if task.get("start_date") is not None:
                continue
            
            start_raw = task["start_raw"]
            if start_raw.startswith("after "):
                dep_id = start_raw.replace("after ", "").strip()
                if dep_id in tasks and tasks[dep_id].get("due_date") is not None:
                    task["start_date"] = tasks[dep_id]["due_date"]
                    dur_match = re.match(r'^(\d+)(d|w)$', task["duration_raw"])
                    days = 1
                    if dur_match:
                        val, unit = dur_match.groups()
                        days = int(val) * (7 if unit == 'w' else 1)
                    task["due_date"] = task["start_date"] + timedelta(days=days)
                    resolved_any = True
        if not resolved_any:
            break
            
    # Third pass: fallback for unresolved dependencies
    for task_id, task in tasks.items():
        if task.get("start_date") is None:
            task["start_date"] = default_start
            dur_match = re.match(r'^(\d+)(d|w)$', task["duration_raw"])
            days = 1
            if dur_match:
                val, unit = dur_match.groups()
                days = int(val) * (7 if unit == 'w' else 1)
            task["due_date"] = task["start_date"] + timedelta(days=days)
            
    # 3. Parse WBS details
    lines = content.split('\n')
    current_task_id = None
    desc_lines = []
    
    for line in lines:
        task_header_match = re.match(r'^\s*\*\s+\*\*([a-zA-Z0-9_]+):\s*(.*?)\*\*', line)
        if task_header_match:
            if current_task_id and current_task_id in tasks:
                tasks[current_task_id]["description"] = "\n".join(desc_lines).strip()
            current_task_id = task_header_match.group(1).strip()
            desc_lines = []
            continue
            
        if current_task_id:
            stripped = line.strip()
            # Stop parsing description on new markdown sections or top level non-task list elements
            if line.startswith('#') or line.startswith('---') or (stripped.startswith('*') and not stripped.startswith('* **') and not line.startswith(' ') and not line.startswith('\t')):
                if current_task_id in tasks:
                    tasks[current_task_id]["description"] = "\n".join(desc_lines).strip()
                current_task_id = None
                desc_lines = []
            else:
                desc_lines.append(line)
                
    if current_task_id and current_task_id in tasks:
        tasks[current_task_id]["description"] = "\n".join(desc_lines).strip()
        
    return tasks


def sync_tasks(api, project_id, file_path, start_date_str, dry_run=False):
    """Executes the task synchronization loop."""
    print(f"[*] Parsing planning file: {file_path}")
    parsed_tasks = parse_markdown_file(file_path, start_date_str)
    print(f"[+] Parsed {len(parsed_tasks)} tasks from Markdown file.")
    
    if not parsed_tasks:
        print("[-] No tasks parsed from file. Ensure Mermaid Gantt section is present.")
        return
        
    if dry_run:
        print("\n=== DRY RUN MODE: Tasks to sync ===")
        for tid, task in parsed_tasks.items():
            print(f"- [{tid}] {task['subject']}")
            print(f"  Section:     {task['section']}")
            print(f"  Status:      {task['status']}")
            print(f"  Start Date:  {task['start_date'].strftime('%Y-%m-%d')}")
            print(f"  Due Date:    {task['due_date'].strftime('%Y-%m-%d')}")
            if task['description']:
                desc_preview = task['description'].replace('\n', '\n               ')
                print(f"  Description: {desc_preview}")
            print()
        return

    print("[*] Connecting to OpenProject to fetch metadata...")
    status_mapping = api.fetch_statuses()
    type_href = api.fetch_task_type_link(project_id)
    existing_wps = api.fetch_existing_work_packages(project_id)
    
    print(f"[+] Found {len(existing_wps)} existing synchronized work packages in project.")
    
    created_count = 0
    updated_count = 0
    noop_count = 0
    
    for tid, task in parsed_tasks.items():
        subject_with_id = f"[{tid}] {task['subject']}"
        status_href = api.get_status_link(task["status"], status_mapping)
        
        if tid in existing_wps:
            # Check for changes
            existing = existing_wps[tid]
            wp_id = existing["wp_id"]
            lock_version = existing["lock_version"]
            
            updates = {}
            if existing["subject"] != subject_with_id:
                updates["subject"] = subject_with_id
                
            start_str = task["start_date"].strftime("%Y-%m-%d")
            if existing["start_date"] != start_str:
                updates["startDate"] = start_str
                
            due_str = task["due_date"].strftime("%Y-%m-%d")
            if existing["due_date"] != due_str:
                updates["dueDate"] = due_str
                
            if existing["description_raw"].strip() != task["description"].strip():
                updates["description"] = {
                    "format": "markdown",
                    "raw": task["description"]
                }
                
            if status_href and existing["status_href"] != status_href:
                updates["_links"] = {"status": {"href": status_href}}
                
            if updates:
                print(f"[*] Updating task [{tid}] (OpenProject ID: {wp_id})...")
                success = api.update_work_package(wp_id, lock_version, updates)
                if success:
                    print(f"    [+] Updated successfully.")
                    updated_count += 1
                else:
                    print(f"    [-] Failed to update.")
            else:
                noop_count += 1
        else:
            # Create new task
            print(f"[*] Creating new task: {subject_with_id}...")
            success = api.create_work_package(
                project_id=project_id,
                subject=subject_with_id,
                start_date=task["start_date"],
                due_date=task["due_date"],
                description=task["description"],
                type_href=type_href,
                status_href=status_href
            )
            if success:
                print(f"    [+] Created successfully.")
                created_count += 1
            else:
                print(f"    [-] Failed to create.")
                
    print(f"\n[+] Task synchronization completed:")
    print(f"    - Created: {created_count}")
    print(f"    - Updated: {updated_count}")
    print(f"    - No-op:   {noop_count}")


def main():
    parser = argparse.ArgumentParser(description="OpenProject Headless Sync Utility")
    parser.add_argument("--action", choices=["test", "create", "create-sub", "update-desc", "sync-tasks"], required=True,
                        help="Action to execute")
    parser.add_argument("--name", help="Project name (required for create/create-sub)")
    parser.add_argument("--identifier", help="Project identifier slug (required for create/create-sub)")
    parser.add_argument("--parent-id", type=int, help="Parent project ID (required for create-sub)")
    parser.add_argument("--project-id", type=int, help="Project ID to update (required for update-desc/sync-tasks)")
    parser.add_argument("--file", help="Path to Markdown file (required for update-desc/sync-tasks)")
    parser.add_argument("--start-date", default="2026-05-14", help="Fallback project start date in YYYY-MM-DD format")
    parser.add_argument("--dry-run", action="store_true", help="Perform actions in dry-run mode (only affects sync-tasks)")
    
    args = parser.parse_args()

    # Get configuration from env variables
    url = os.environ.get("OPENPROJECT_URL")
    token = os.environ.get("OPENPROJECT_TOKEN")

    if not url or not token:
        print("[-] Error: OPENPROJECT_URL and OPENPROJECT_TOKEN environment variables must be set.")
        print("    Example:")
        print("    export OPENPROJECT_URL=\"https://project.pxg.studio\"")
        print("    export OPENPROJECT_TOKEN=\"4a7b9c1d...\"")
        sys.exit(1)

    api = OpenProjectAPI(url, token)

    if args.action == "test":
        api.test_connection()
    elif args.action == "create":
        if not args.name or not args.identifier:
            print("[-] Error: --name and --identifier are required to create a project.")
            sys.exit(1)
        api.create_project(args.name, args.identifier)
    elif args.action == "create-sub":
        if not args.name or not args.identifier or not args.parent_id:
            print("[-] Error: --name, --identifier, and --parent-id are required to create a subproject.")
            sys.exit(1)
        api.create_project(args.name, args.identifier, args.parent_id)
    elif args.action == "update-desc":
        if not args.project_id or not args.file:
            print("[-] Error: --project-id and --file are required to update a description.")
            sys.exit(1)
        if not os.path.exists(args.file):
            print(f"[-] Error: File not found at {args.file}")
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        api.update_project_description(args.project_id, content)
    elif args.action == "sync-tasks":
        if not args.project_id or not args.file:
            print("[-] Error: --project-id and --file are required to sync tasks.")
            sys.exit(1)
        sync_tasks(api, args.project_id, args.file, args.start_date, args.dry_run)

if __name__ == "__main__":
    main()

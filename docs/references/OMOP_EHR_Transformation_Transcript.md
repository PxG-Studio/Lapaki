# Transcript: Transformation of EHR data to OMOP Common Data Model

**Speaker:** Min Jiang, Ph.D. Candidate  
**Source Video:** [YouTube Link](https://www.youtube.com/watch?v=T1zKVlN7Wlg)  
**Date of Presentation:** October 22, 2015  
**Abstract:** Technical presentation at SBMI regarding the transformation of UT Electronic Health Record (EHR) data to the Observational Medical Outcomes Partnership (OMOP) Common Data Model (CDM), detailing lab test conversions (LOINC mapping, tf-idf ranking, dynamic range matching) and drug/condition coding.

---

| Time | Transcript Line |
|---|---|
| **0:00** | that |
| **0:17** | okay my name is minja I'm PhD candidate of best BMI today I'm gonna present the |
| **0:25** | work of transformation of EHR data to OMAP comdata model and here's the agenda |
| **0:34** | first I will give some introduction of a mob CDM and then I will give a summary |
| **0:40** | of UT can encode data and after that I will introduce our transformation |
| **0:47** | process while step by step and finally we'll give some visualization of results |
| **0:53** | and we also talk about the future work of this project and the LOC Klosterman's |
| **1:01** | so first I will introduce the common data model on clinical observation |
| **1:07** | healthcare so as we all know the |
| **1:12** | observation health data is very important to creating a reliable can |
| **1:17** | evidence in the clinical research however there's still a lot of challenge |
| **1:24** | to do so so first come from diverse data sources the kink observational health |
| **1:31** | data could come from electronic health records the hospital the hospital Billings the insurance claims were so |
| **1:39** | from longitudinal surveys so to combine such |
| **1:46** | kind of diverse data source it's kind of a challenge because each data source has |
| **1:51** | its own purpose to design and also has this own technology to present so how to |
| **1:58** | combine such kind of multiple data sources into a clinical study is a challenge |
| **2:03** | another issues come from repeatability of the study of the clinical study on |
| **2:10** | multiple sides so in order to get the good generalizability of the clinical |
| **2:16** | study will only do the study on multiple sides |
| **2:22** | but due to there's some technical environmental issues or some different |
| **2:29** | data formats it's a kind of challenge to do so so the standardization of the |
| **2:37** | observation data could be a good way to solve this issue so in this way if you |
| **2:45** | turn into all the data source into standards that are standardized the data we could perform of efficient in a |
| **2:53** | reliable clinical research then I will |
| **3:00** | give some introduction of OMAP CBM so basically in order to do the generalization the standardization we |
| **3:07** | need some common data model so loudest we have a lot of common data model |
| **3:13** | designing that community research and the one of them is OMA become their |
| **3:18** | model which is purposed to present the healthcare data from diverse source in a |
| **3:23** | consistent and standardized way and which also asked for collaborative |
| **3:29** | research across different data sources and home up the full name is of the |
| **3:36** | observational medical outcome partnership so which is organization to |
| **3:41** | absorb to the OP the proper use of observational health database for medical study actually and now it's |
| **3:49** | become the part of the NADA program named the observational health data science and information informatics |
| **3:55** | pronounced the Odyssey which is purposed to create and apply some open-source |
| **4:03** | third-party tools to your large network of health database to improve human |
| **4:10** | health so this diagram shows the whole picture |
| **4:19** | when multiple source of data comes into the transformation of to the AMA become |
| **4:27** | their model so in the community we also |
| **4:32** | we still we also already develop a lot of analysis method to apply on this |
| **4:41** | common data model to generate some analysis results for for for repetitive |
| **4:50** | use so here we can see if we gonna |
| **4:56** | represent the data into the common data model we could make use of our available |
| **5:03** | existing third-party tools to generate some analysis results and here I'm going |
| **5:14** | to use the model details so the OMAP model is composed of |
| **5:20** | different parts you can see the one is the standardize the clinical data which |
| **5:27** | represent the court kinko events from the data repository and the standardize |
| **5:33** | the health system data is about the healthcare provider system and |
| **5:38** | standardize the health economies about the coast of the health system and the |
| **5:45** | standardized derived elements that part is actually loaded directly derived from |
| **5:51** | the kinko repositories so it is better based on the clinical artifacts we |
| **5:58** | generated some something and the standardized the metadata that is about |
| **6:04** | the metadata of the transformation process so for example we could include the version of vocabulary used in the |
| **6:12** | transformation process and the standardized vocabulary which is used to |
| **6:18** | define all the clinical events in the omapere model |
| **6:25** | and for the Umatilla model the vocabulary is the kind of flexible study |
| **6:32** | so here's the list of the terminology or ontologies |
| **6:38** | which are included in the vocabulary so we can see there could be come from drug |
| **6:45** | procedure or lab tests so so user could |
| **6:52** | adapt to depends on their own terminology in the in the their data |
| **6:58** | data repository user to select multiple or flexible data of terminology through |
| **7:06** | presenting the OMAP data model so now |
| **7:12** | I'm gonna introduce briefly of the UT clinical data in UT data you roughly |
| **7:20** | have three minim and Mayans in the warehouse but we need to exclude the records |
| **7:25** | without at least the wine was transaction that means those in water those records without any invoice of |
| **7:33** | transaction means lots of real records and we also have some mystification |
| **7:40** | algorithm to remove such duplicate records so as a result we have two |
| **7:47** | meaning unifications with spinning transaction records so now I'm going to |
| **7:54** | use the transformation process so first I will start with the left has |
| **8:03** | to result conversion so for lab test results in the common data model we use |
| **8:11** | the management table to present such things so imagined is defined as the |
| **8:18** | capture of a structure value obtained through systematic examination of a person or sample so in the management |
| **8:28** | table if it capture laboratory results vital signs or quantitative finding but |
| **8:35** | here we just focus on the laboratories out the management table the physical |
| **8:43** | structure is like this so we can see some of them other tables are related to |
| **8:49** | this table for example the person the provider and visitor and in the during |
| **8:59** | the conversion process we found we have some challenge our tactics to actually |
| **9:05** | convert the laboratory test laying and results to localization part but in a UT |
| **9:13** | data we found there's no standard terminology to present the laboratory |
| **9:19** | test only the internal ID is assigned to |
| **9:24** | each in the port or entire records in the furthermore we also found even |
| **9:31** | multiple entries means multiple IDs could refer to the same network to a test and for the new border test name it |
| **9:42** | actually it's not easy to get computation by a computer because he's |
| **9:47** | just designed for the human raters so the same user also happens on the test |
| **9:53** | results so - to represent an ab testing interest |
| **10:02** | anders standardized away we need to choose some standard standard and a |
| **10:08** | large so here we just choose the line code to present all the things the line |
| **10:14** | code is wider used in to present a laboratory results in clinical study and |
| **10:21** | for each knowing code it has some attributes the one is component means |
| **10:27** | was measured and the property means the character a characteristic was measured |
| **10:33** | for example the mass per volume substance per warning and the attribute |
| **10:40** | system means the space specimen type for example the blood the urine and the loin |
| **10:48** | code worse include the unit of the matter so here's the screenshot of the |
| **10:57** | alloying code search interface developed by the research community and we can see |
| **11:03** | for each knowing codes we have the long name of the lab test and we have a |
| **11:10** | different attributes such as a component in poverty system scale method and the |
| **11:19** | units so before we start the conversion |
| **11:24** | you were study some statistics on our data so in our data we have about 29,000 |
| **11:34** | entries for lab tests name an amount of those we found some of them are invalid |
| **11:42** | test name so we move them as a result we have 21,000 test name and in the in dose |
| **11:52** | in readout table we we found that there is a 14,000 unique name |
| **11:59** | so here we also generate statistic on the coverage of the the frequency of |
| **12:06** | each you nickname for the first 500 you |
| **12:12** | nickname the coverage is 82% and and we |
| **12:18** | can see when we got to the first of four thousand the percentage is 98 percent so |
| **12:26** | that means for 4000 for those four |
| **12:31** | thousand drinking and cover most of the depth in the water test name so in this |
| **12:37** | study we're just trying to focus on the most most of frequency laboratory test name here so our solution to do the |
| **12:49** | conversion is to develop an annotation tool for Mary review basically so our |
| **12:56** | annotation tool includes a search interface we could use that to very |
| **13:02** | easily locate the similar and related test name in our duty data in a war so |
| **13:10** | we provide some helpful information and a tool to make the annotation more |
| **13:15** | efficiently so for example we include the distribution of lab tests value |
| **13:21** | range here to help annotator to decide which kind of going code should be |
| **13:27** | assigned to and then we also include the ranking of senior tasks in the line code |
| **13:33** | which generating using the tf-idf algorithm and the size of that we also |
| **13:42** | integrate to the search interface 4-legged code in our annotation tool so |
| **13:50** | here this is the word annotation tool looks like the left pane shows the |
| **13:56** | search interface for our for the laboratory test in our UT data so when |
| **14:03** | user input a key word here and there were show some the all the test name |
| **14:10** | which had which had map mask this keyword search so exiting our UT |
| **14:21** | datasets multiple test name could refer to the same task so here when we search |
| **14:28** | the single test assets we could do the annotation in the batch so that could |
| **14:34** | stay for some some time so when user click the each of the test |
| **14:41** | name the right panel where show take the detailed statistic including like the |
| **14:51** | range value or the panels so based on those helpful information |
| **14:57** | the annotator could be finding the the right code more easily and the bottom |
| **15:06** | right shows the search interface developed by the community which is to |
| **15:11** | search the link code |
| **15:17** | so besides of the tassel name we also have the test results need to convert |
| **15:23** | total test results at about 26 minutes and amount of them 77% our numerical |
| **15:34** | results and 23% our free text and among |
| **15:39** | those free text 18% our code without so that means those result could be |
| **15:45** | converted to code and the 2% inverted tests and results for example there |
| **15:51** | could be come from comments some results notes which is a lot real actually the |
| **15:59** | bottle retest and 3% laboratory test test without any results so here we just |
| **16:11** | show some Valladares result examples we can see the most frequent one is the |
| **16:19** | image is acquired not a reporting on this accession number that could be example and neither is like the TMP and |
| **16:28** | cancel reason and see comments something like that and that's showed me stuff for |
| **16:37** | code both verbal results so here we can see some of something like snide |
| **16:43** | collective slight yellow which is our objective words to describe the bottle |
| **16:51** | results so I'm gonna start to culture in |
| **17:24** | progress yeah actually this is actually |
| **17:44** | many reviewed by the physician so maybe I can ask a detail for the for the |
| **17:51** | physician yeah cuz to be generous on the list and then the matter the physician |
| **17:58** | will take Mary will be London and some of the work picked up yeah I think that |
| **18:09** | could be another kind of standard |
| **18:15** | okay let's get started - I introduced the process of medication part for the |
| **18:22** | medication parts in OMAP it has three tables first one is drug exposure which |
| **18:30** | captures records about the drug and the second one is brother hero which is |
| **18:37** | actually derived from the first drug exposure table to present a span of time |
| **18:42** | when a person exposed to a particular activity regarding British and for the |
| **18:49** | dose hero it was the derived derived a from drug exposure and we represent a span of time |
| **18:56** | when person is to be exposed to a constant dose of four specific active |
| **19:01** | dragon grilling so our task is trying to |
| **19:07** | transform the the tables and I will repeat the clinical data warehouse may |
| **19:13** | include the medication effects and medication d2 those three tables so in |
| **19:22** | this part our biggest challenge comes from the information music so for example in the |
| **19:29** | table drug exposure that requires the end the date of the each drug use but we |
| **19:36** | still can we cannot find such kind of information our UT data so our solution |
| **19:42** | is trying to infer those information based on existing information for |
| **19:47** | example we could use the day's supply and start dates to do estimation of the |
| **19:52** | end bait and the another issue is from the terminology and some laundry using our |
| **20:00** | records so we found one six we're cutting our UT table lack of Arsenal |
| **20:07** | either arcs no more NDC code so our solution is trying to use the automatic |
| **20:13** | way to do the automatic encoding for those records without any codes and |
| **20:20** | after that we did some manual review to make sure the result is cracked so here |
| **20:31** | we I can just introduce how we're going to do the automatic encoding and the |
| **20:37** | manual review so first we have the OMA vocabulary which includes the list of |
| **20:43** | mapping between the concept ID and medication name then we use the third |
| **20:50** | path tool named dilution which is actually open source search engine tool we use that to create a loosened X and |
| **20:58** | then we instructed the medication phrase which knack of code and and after that |
| **21:06** | we calculate similarity score according to the algorithm in the loosing we get a |
| **21:13** | rank list and from those ranked a top ranked list we have a physician to |
| **21:20** | manually review the top ranked list to make sure which one should be cracked |
| **21:28** | and here's the transformation result this looks like so we have the three |
| **21:34** | tables the drug exposure table including the information like the concept the |
| **21:40** | start date the end dates and also include the quantity days supply and |
| **21:46** | there's some signature information for the drug euro table we include the drug |
| **21:53** | concept ID the worst I include the drop the euro start and end the date and for |
| **21:59** | the dose Europe besides such information we also included those values so here we |
| **22:10** | can start to introduced our conversion on the condition parts in OMAP model we |
| **22:18** | have two tables to present condition related things the one is condition occurrence not one is condition euro |
| **22:25** | which has very similar structure night the drug so for the conditional chorus |
| **22:32** | we have the condition start date end date and the concept so basically just |
| **22:40** | represents the clinical observation of persons of the existence of disease or |
| **22:48** | medical condition an irritable just represents the span of time on a given |
| **22:55** | condition so which include us the euro start date end date and a current |
| **23:00** | account and condition concept in our UT |
| **23:05** | data we actually transform that part from the dyatlov's table during our |
| **23:13** | diagnose table we don't have the condition and daily information but that |
| **23:19** | information is required for the on Matt Damon so actually we for our C's is kind |
| **23:26** | of hard to estimate the actual data of the end date of the condition so we just do a fix the rule here we |
| **23:35** | said and the data goes to the start date class condition plus 30 days which is |
| **23:41** | kind of common way to handle these missing information in the Policy Forum |
| **23:48** | so basically here for kornek disease yes |
| **23:57** | that's that's good there's a good question because we don't have such information so we're just trying to find |
| **24:04** | out how to solve this issue we asked we post the question on the forum but they |
| **24:10** | just suggest me to do so like the to do the fixed format like fixed weight like |
| **24:17** | plus 30 days for 60 days because this is a common way that they do for the |
| **24:23** | example day like database yeah right for |
| **24:58** | the chronic disease is for so we're very hard to evaluate actually this started |
| **25:03** | and ended date because it's hard to track the status of the such kind of disease through the eunuch 20 health |
| **25:10** | workers yeah I think yeah I think that's a maybe |
| **25:18** | the the things we need to figure out how to create some mechanism to handle the |
| **25:25** | chronic disease respectively yeah that's |
| **25:34** | a good way maybe |
| **25:40** | and I'm gonna introduce the transformation process and other tables |
| **25:46** | for the person and provider in the UT data we have some conflict some |
| **25:51** | demographic information means for the same person name we may have the |
| **25:58** | different demographic information such as birth date and we're so a gender even |
| **26:06** | so to fix that issue we choose which is trying to mow choose the most current |
| **26:12** | demographic information according to the dates the creation date and for provide |
| **26:19** | the name we also found some lanes as Nazis easy access which is always |
| **26:24** | another one so we do the filtering based on providing information in was table |
| **26:31** | because in the worst table the provider |
| **26:36** | existing them what can't or should be three one and |
| **26:46** | yes yes |
| **26:54** | we just found that kind of situation |
| **27:00** | sorry right right duplication so |
| **27:16** | actually we did we do not do the detoxication here |
| **27:49** | so that's how so you're absolutely right some cases so we actually had training |
| **28:09** | between certain yes or no there will be |
| **28:20** | some forced some cases where |
| **28:41** | later we need to incorporate this part into our project the concept |
| **28:58** | so so you mean the 44 plan imparted for for factually for example for the |
| **29:07** | medication we in our UT data we have some like five 80% data which actually |
| **29:16** | have some which are also assigned to the standardized terminology like in DC or |
| **29:22** | axonal and for those which lack of codes we do the automatic encoding and then do |
| **29:29** | matter with you know we're not reaching |
| **29:35** | out you stats we use the loosing to do some ranking stuff and then we based on |
| **29:41** | the general ranking list they do matter with you so that could save some time |
| **29:55** | and for busy table that comes from the encounter factor to going our UT tape |
| **30:01** | data repository and the renewed filtering according to the encounter type here so in our table we have the |
| **30:09** | appointment image which is kind of encounter typing we also have some other |
| **30:15** | type like audits 10 foam core which is obviously should be moved during the |
| **30:22** | conversion process so now I are going to |
| **30:28** | show some visualization of the data so we use the archness which is the open |
| **30:34** | source tool developed by the Odyssey program so which purpose is to try to |
| **30:43** | label the characterization and the quality assessment and visualization of |
| **30:49** | the database so in this tool it has two |
| **30:54** | components the first one is our package and run within the local environment |
| **31:00** | basically under our transform attic |
| **31:05** | transformation of the on map data and then generate some statistical report |
| **31:12** | and another components to use the some website page to show and the some a |
| **31:18** | series of interactive reports diagram to show such generated data death |
| **31:26** | results from the first step so here you can see the first diagram |
| **31:34** | shows the data density after each category of the data in the genome |
| **31:40** | update model so here we can see the |
| **31:45** | condition occurrence is the most frequent one and and then the drokken |
| **31:52** | euro and the drug exposure and and then the recent occurrence and the drug |
| **31:59** | exposure and the drug of Europe so in the diet the diagram below the werster |
| **32:06** | show the concept of per person for different category of data so we have a |
| **32:15** | statistic here we can see the max maximum in value and some statistic |
| **32:21** | value for each category |
| **32:30** | and this diagram is showed that result about person so we allow we have the |
| **32:38** | about three million persons but here we do not exclude the person without any |
| **32:44** | kinds of transaction being with records and for people we could say the people's |
| **32:54** | birth date distribution the gender distribution the population and the |
| **32:59** | population by race by different as ladies |
| **33:10** | and here we just show the I would generate to the drug results which is |
| **33:15** | basically on the face down the drug exposure table and actually there's a |
| **33:21** | two way to present this kind of data one ways they used it a format named the |
| **33:29** | tree map so in this tree map each rectangular area represent a drop use a |
| **33:35** | specific drug use so for example there's if you move the mouse each area they |
| **33:43** | will show the detail information about this drug concept so we can see what's |
| **33:51** | the prevalence of these globules and how many numbers are used in drug and even |
| **33:57** | the records proportion and the blow |
| **34:04** | diagram shows another way to visualize this results this is from the table so |
| **34:10** | there's the list of tables table items could show each drug use in this in |
| **34:19** | these data sets we also can see the same information like a province and the |
| **34:25** | record for per person |
| **34:33** | and if you select any records in the tables the blow diagram also show the |
| **34:40** | prevalence for one thousand people's according to different age groups so we |
| **34:48** | could say the Sivas Denton twenty many |
| **34:54** | grams oral tablet its use situation in |
| **35:01** | the different age group and also they |
| **35:07** | differ from the from the male and the |
| **35:12** | female |
| **35:19** | so after we do the conversion what we |
| **35:25** | are going to do after the transformation so basically the first one is we still |
| **35:33** | because in this way we only just say extract the structured data from the EHR |
| **35:39** | so we still have some clinical information which embedded in the |
| **35:44** | clinical tax which is unstructured data need to be extracted so we may use to |
| **35:50** | use some apply lateral language processing methods to extract such |
| **35:55** | information to make the model more comprehensive to do the clinical study |
| **36:02** | and another thing we could do is we could apply the existing another an |
| **36:11** | analytics tool or Mordo all this data for example in the autistic community |
| **36:17** | they just create some a lot of tools for example the cohort creation and analysis |
| **36:23** | tool and the worse though they implement some protocol of kink of studies for |
| **36:29** | example a treatment pathway the pharmacogenetic drug study and the drug |
| **36:34** | utilization children protocol here I |
| **36:40** | just show some screenshots of the existing Atlantic tools in the odyssey |
| **36:45** | forum so this one is named the hermit's is used to search in vocabulary so here |
| **36:56** | we can see we could use improve any keywords here and then they will show the result of the concepts name and it's |
| **37:03** | a class and it's a domain and and its source so using this search without which we |
| **37:12** | could create a concept set used to define clinical cohort cohort |
| **37:19** | so this one this troll named the Circe which is kind of a cohort deflation tool |
| **37:27** | so this is the midst of existing cohort deflation actually when we click any |
| **37:34** | item so in this interface we could |
| **37:40** | define the cohort we want they define the cohort basically by defining the |
| **37:48** | concepts at first so for so here they have four concept sets item attack there |
| **37:57** | so through that we could define a concept set for example the Cooper's and |
| **38:02** | diabetes and then after that in the expression tab we could use the define |
| **38:12** | the concept set to present all patients with diabetes and besides of this they |
| **38:19** | also can define using some additional additional criteria to define the cohort |
| **38:26** | so Wednesday has finished the definition so there will be automatically generated |
| **38:33** | and imported into the database for further use |
| **38:41** | and here is another tool named capsule |
| **38:47** | which is a feasibility of a study tool |
| **38:53** | so besides of the concept they actually use another criteria for example like |
| **38:59** | including some demographic information gender and which should be more flexible |
| **39:08** | to defining a population so okay so for |
| **39:18** | this study I'm just saying for my |
| **39:24** | supervisor partial provider citizenship and my colleagues a concil who did a lot |
| **39:30** | of contribution on this project also and some collaborator dr. Emma provide |
| **39:37** | access our access to that clinical data warehouse and to charge and Michael who |
| **39:43** | did a lot of the technical support there so we thanks for them |
| **40:16** | yeah that's good there's good question so actually we just finished the |
| **40:21** | transformation part here and basically we also saw that the webpage of the |
| **40:28** | witch including the descriptive statistics data in the UT data I think a |
| **40:34** | lot of things we need to do is just trying to to compare such kind of result |
| **40:40** | to make sure what we generate it is it's a cracked yeah that's just that's an |
| **40:48** | extra things but you also need to do |
| **40:56** | sure because in the UT clinical data there were so some kind of voice data some |
| **41:05** | noise so yeah so basically for those kind of noise could double the age some |
| **41:12** | some kind of people searching maybe more than 100 word 2200 maybe this is a kind |
| **41:17** | of obviously a lot of cracks about it but such kind of things I mean the |
| **41:23** | person's age yes so that that's only one example so you also saw another kind of |
| **41:30** | example inside you know other category of data such as drugs and and and medication and and lab tests so I think |
| **41:40** | we need to make some criteria to find out how many data a lot of a lot of |
| **41:48** | obviously incorrect data |
| **41:54** | what is quality talk about quality means |
| **42:00** | of the data so in other words people that waiting for the mass of the earth so that's not a problem with |
| **42:06** | transformation of the problem a collection or a reporting or what happens that the transformation process |
| **42:12** | has nothing to do yes there are problems that may be introduced by transformation |
| **42:18** | so separately evaluate one of the |
| **42:24** | challenges of course are tended to open |
| **42:30** | is to slice and dice the data set in various ways so that at least some |
| **42:37** | problems right right yeah yeah thanks |
| **42:59** | I think most of them most of them |
| **43:15** | I mean there's or prescriptions are they |
| **44:18** | tied to a condition that is thick for |
| **44:23** | the studies |
| **44:44** | ut dataset I think actually we transform the each |
| **44:52** | individual part from the into each individual tables actually for the condition we use that I close the table |
| **44:59** | and for another part we use them maybe some separate tables so cashing |
| **45:14** | condition I'm not very sure about that maybe consult |
| **45:43** | diabetes the accountants but it's time to metformin that brochure that Foreman |
| **45:51** | to confirm the probabilities so I I just |
| **45:57** | don't know as you know for like x-rays it's sometimes rule out little bits the |
| **46:06** | biggest case of Boston they sort of 19 |
| **46:28** | we went through some UT that I said we'll find some inconsistency between |
| **46:34** | the precaster and so how to transform |
| **46:43** | this how to deal with this company today sue me that he found their saying |
| **46:50** | consistency between the pre-tax and structured data so actually our process |
| **46:59** | we only transform the structured data here so maybe later we had gone to |
| **47:05** | trying to convert the free text Pony or so we always to think about this issue |
| **47:12** | because when we before the this kind of step because the in the kinko tax we |
| **47:18** | also we may have found some always can found some inconsistent because the |
| **47:24** | flexibility of the tax use at the language use so I think the structured |
| **47:30** | data could be kind of standard or more |
| **47:36** | kind of golden standards we could use to leverage how we extracted that when when |
| **47:45** | we extract the data from the pretext so that could be a way to do and and maybe |
| **47:57** | we clear something LP technologies to to generate some maybe conflicts extracted |
| **48:06** | from the free tax only so for example in the multiple concur notes we could found |
| **48:13** | some the kind of records which is maybe |
| **48:21** | a lot matchable so we could use some an LP technologies to do to some |
| **48:28** | generalization statistics to find out |
| **48:33** | trying to figure out which is to which is not |
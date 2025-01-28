# Assignment 2

## Q1: Study description [5 points]

Read Osth & Fox (2019) from the start until the "Re-analyses of archival datasets" section. Write a short paragraph answering the following questions:

* What was the main question that the authors were trying to answer in this study?
  * Are people more likely to think two items were presented together if they were near to one another in the list? To put it more broadly, do people associate things that were seen nearby in time to one another, even if they aren’t told to do so?
* What are the two main independent variables in Experiment 1?
  * Pair type (intact or rearranged) and lag between the items in rearranged pairs.
* What is the main dependent variable?
  * Probability of saying “yes”, that is, probability of saying that they did see that pair of items before.
* Is this a within-subject or between-subject (also known as across-subject) design?
  * Within-subject.

## Q2: Dataset [7 points]

Download the Datasets/exp1.csv spreadsheet from the OSF repository and open it in a spreadsheet viewer like Excel. Look at the data and compare it to the description in the paper. Answer the following questions:

* What do the phase, type, response, RT, correct, and lag columns indicate?
  * Phase of the experiment (study or test), type of pair presented during the test (intact or rearranged), response (0 for rearranged, 1 for target, -1 for no response, whether the response was correct (1) or incorrect (0), number of pairs separating rearranged pairs.
* What value is used to indicate missing data?
  * -1.

## Q3: BIDS standard [8 points]

Describe two changes that would be required to make the data in the exp1.csv file compliant with the BIDS standard for behavioral experiments. You can ignore the optional and recommended attributes.

Some necessary changes (may not be an exhaustive list) include:
* The file must be split by subject, with one file per subject.
* The file must be a TSV file instead of a CSV file.
* The filename should be standardized, something like `sub-101_task-recognition_beh.tsv`.
* Missing values should be labeled as "n/a", not "-1".

Create a BIDS-compliant data dictionary for the following columns in the exp1.csv file: phase, type, response. See here for details about tabular files and their corresponding data dictionaries. Include Description and Levels keys for each column, indicating all values that each column may take and what they mean. Use the JSONLint tool to validate and reformat your file. Upload the formatted JSON file here.

See `task-recognition_beh.json` for an example. The column descriptions and levels should be sufficient to distinguish them.

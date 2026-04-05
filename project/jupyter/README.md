# Polyn et al. (2011) dataset

The data in `2011_Polyn_scored.csv` are converted from the raw data available from the Penn Computational Memory Lab's [data archive](https://memory.psych.upenn.edu/Data_Archive).

Polyn, S. M., Erlikhman, G. & Kahana, M. J. Semantic cuing and the scale insensitivity of recency and contiguity. J Exp Psychology Learn Mem Cognition 37, 766 (2011). https://psycnet.apa.org/doi/10.1037/a0022475

## Data dictionary

subject
: subject identifier code

list
: list number

item
: item that was presented or recalled

input
: position the item was presented in the list (also known as serial position)

output
: position that the item was recalled during the free-recall period (also known as output position)

study
: "true" if this item was presented and "false" if it was not (this only happens when the participant accidentally recalls an item that was not on the list, or if they accidentally repeat the same item multiple times during recall). To exclude all repeats and intrusions, filter for trials where the study field is "true"

recall
: "true" if this item was recalled and "false" if it was not recalled

repeat
: the number of times this item was repeated during recall

intrusion
: "true" if this item was recalled but was not actually presented on the list

task
: 1: uncategorized list, followed by free recall; 2: categorized list, followed by free recall; 3: categorized list, followed by recall-by-category

category
: category this item belongs to ("n/a" for intrusions)

period
: if this was a recall-by-category list (task code=3), indicates the recall period that the category was cued

category_input
: position that the item was presented, relative to other items from the same category in the list

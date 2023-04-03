# DSCI550_Assignment2 Team 3

This is the second assignment from the DSCI 550 class. This assignment is collaborated and completed by Team 3. <br>
Team menbers: Jimin Ding, Mingyu Zong, Hui Qi, Xiaoyu Dong

## Group Assignment Allocation
Jimin Ding
> Took charge for step 8 (language detection)<br>
Took charge for step 9 (RTG Translation)<br>
Wrote codes and answers for questions 2 in the report<br>
Wrote answers towards thoughts about RTG

Mingyu Zong
> Took charge for step 7 (Tika-Similarity)<br>
Took charge for step 8 (Package data)<br>
Wrote codes and answers for questions 1 in the report<br>
Wrote answers towards thoughts about Apache Tika

Hui Qi 
> Wrote codes and answers for questions 2, 3, 6, 7 in the report<br>
Wrote readme.md

Xiaoyu Dong
> Took charge for step 6 (add three other datasets with different MIME types)<br>
Wrote codes and answers for added datasets, unintended consequences, questions 5 in the report<br>



## Dependencies

A list of all of the dependencies used, included their version number  
```
editdistance==0.5.3
elasticsearch==8.6.2
Flask==1.1.2
jellyfish==0.9.0
nltk==3.4.5
numpy==1.21.5
pandas==1.4.4
Pillow==9.4.0
pytesseract==0.3.10
python_Levenshtein==0.20.9
requests==2.23.0
scikit_learn==1.2.1
scipy==1.7.3
simplejson==3.18.3
SolrClient==0.3.1
stemming==1.0.1
tika==1.23.1
```
## Installation

Install the requirements necessary to run this project:  

```
pip install -r requirements.txt
```

## Running the project
Run the following 4 files in the Step5 folder to add flim, sport, ifHate, ifSarcasm features in combine.csv, and integrate the result into combine_after5.csv.
```
add_film.py
sarcasm_token.py
add_hatespeech.py
add_sarcasm.py
```
In MIME datasets folder, 3 MIME type.ipynb imports combine_after5.csv (Pixstory dataset with step 5 features), exports combine_final.csv (Pixstory dataset with both step 5 and 6 features), and draws graphs to answer report questions 1 and 5. Images of positive words and zip file of covid data are also in the folder.
```
3 MIME type.ipynb
```

The following script in the Step7 folder is used to convert the TSV with 95k rows into smaller batches of json files, each bacth has 100 instances.
```
split.py
```
After split, use these three files in tika-similarity to compute Jaccard, Edit-Distance, and Cosine similarity scores for each batch correspondingly.
```
jaccard_similarity.py
edit-value-similarity.py
cosine_similarity.py
```
With calculated simiarity scores, run the following files to generate circle.json, clusters.json, and levelCluster.json, which are needed for D3 visualizations.
```
edit-cosine-circle-packing.py
edit-cosine-cluster.py
generateLevelCluster.py
```

In the Q2_image_code folder, open Q2_time.ipynb will show the code to visualize feature of users' post time of a day. This is the answer towards report question 2.
```
Q2_time.ipynb
```
In the Q3_image_code folder, open Q3_genders_ages_interests.ipynb will show the code to visualize features among users' interests, genders, and ages. This is the answer towards report question 3.
```
Q3_genders_ages_interests.ipynb
```
Run the following file in the Step5 folder to draw graphs for answers in report question 4.
```
Hatespeech_Age & Gender.py
```
In the Q6_Language_Indentification folder, open Q6_Language_Indentification.ipynb will show the code to visualize users' distribution from narratives' language identification. This is the answer towards report question 6.
```
Q6_Language_Indentification.ipynb
```

## Methodology

#### Step8: Language detection by using Tika’s language identifier and Google LangDetect/Python
Since the narrative part of the post has a lot of tags, we wrote the remove_tag function to remove tags from the text. Then we called tika.language.from_buffer and langdetect.detect to detect the language of the text, and store the detection results into 'tika_language' and 'google_language'columns.

``` 
tika.language.from_buffer
langdetect.detect
``` 

#### Step9: RTG Translation
First, we use the results of Step8 to put the non-English post index into the Trans_list. Then remove tags and urls from the post with remove_tag and find_regular (because of the possibility of a timeout error). Then we use docker tp create RTG localhost and translate the text using tika.translate.auto_from_buffer(txt,'en').

It is easy to generate a timeout error while translating because the text is too long or in certain languages (such as Hindi and Mali). For text longer than 120, we cut it into multiple texts according to punctuation marks, then translated thoses pieces and integrated. The result is stored in 'rtg_translate' column.

``` 
tika.translate.auto_from_buffer
``` 

#### Q7: Tika-Similarity
Follow instructions on https://github.com/chrismattmann/tika-similarity and Professor's proposed workflow posted on Slack.





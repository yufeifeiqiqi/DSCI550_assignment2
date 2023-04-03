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





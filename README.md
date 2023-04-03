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
> Took charge for step 5 and 10 (GeoTopicParser)<br>
Wrote codes and answers for questions 1, 3,4 in the report
Wrote answers towards thoughts about GeoTopicParser

Xiaoyu Dong
> Took charge for step 6 (add three other datasets with different MIME types)<br>
Wrote codes and answers for added datasets, unintended consequences, questions 5 in the report<br>



## Dependencies

A list of all of the dependencies used, included their version number  
```
attr==0.3.2
attrs==22.1.0
brotli==1.0.9
brotlipy==0.7.0
ConfigParser==5.3.0
cryptography==38.0.4
Cython==0.29.32
detoxify==0.5.1
dl==0.1.0
docutils==0.18.1
HTMLParser==0.0.2
importlib_metadata==4.11.3
ipython==8.12.0
ipywidgets==7.6.5
Jinja2==2.11.3
jnius==1.1.0
keyring==23.4.0
lockfile==0.12.2
lxml==4.9.1
matplotlib==3.7.1
numpy==1.21.5
ordereddict==1.1
pandas==1.4.4
Pillow==9.5.0
protobuf==4.22.1
pyOpenSSL==23.1.1
railroad==0.5.0
Sphinx==5.0.2
toml==0.10.2
tornado==6.2
xmlrpclib==1.0.1
zipp==3.11.0
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

#### Step11: Detoxify Scores Generation
This step uses the 'rtg_translate' column derived from RTG Translation. A script written in Python iterates through each value within the column, passes it as input string into detoxify, and saves score from each category into corresponding columns. Since RTG translated most of the posts into English, we ruled out the 'multilingual' model. Considering the additional 'sexual_explicit' category would provide more insights about these Pixstory posts, we determined to use the 'unbiased' model for all entries.

With combine_add_geo.csv (in folder Step10 - GeoTopicParser) and detoxify_scores.py (in folder Step11 - Detoxify) in the same folder, running the following command will generate a final.tsv with 7 more columns for scores: 'Toxicity', 'Severe_Toxicity', 'Obscenity', 'Identity_Attack', 'Insult', 'Threat', 'Sexual_Explicit'.
```
python3 detoxify_scores.py
```





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
> Detoxify scores generation<br>
Posts' toxicity analysis<br>
Thoughts about Detoxify<br>

Hui Qi 
> Took charge for step 5 and 10 (GeoTopicParser)<br>
Wrote codes and answers for questions 1, 3, 4 in the report<br>
Wrote answers towards thoughts about GeoTopicParser

Xiaoyu Dong
> Took charge for step 7 (Image Captioning and Object Recognition)<br>
Wrote codes and answers for questions 6, 7, 8 in the report<br>
Wrote answers towards thoughts about Tika Image Captioning and Tika’s Inception Rest service



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
langdetect==1.0.9
lxml==4.9.1
matplotlib==3.7.1
numpy==1.21.5
ordereddict==1.1
pandas==1.4.4
Pillow==9.5.0
protobuf==4.22.1
pyOpenSSL==23.1.1
railroad==0.5.0
re==2.2.1
Sphinx==5.0.2
tika==2.6.0
toml==0.10.2
tornado==6.2
xmlrpclib==1.0.1
zipp==3.11.0
mvn==3.9.1
```
## Installation

Install the requirements necessary to run this project:  

```
pip install -r requirements.txt
```

## Running the project

In the Step8-Language Detection folder, open combine_language_detection.ipynb will show the code of the results of language of the post and the pie plot for question 2.
```
combine_language_detection.ipynb
```

In the Step9-RTG folder, open RTG_translate.ipynb and use docker to run RTG will show the code of the translation results of the narrative part of the post.
```
RTG_translate.ipynb
```

In the Step10-GeoTopicParser folder, oepn GeoTopicParser.ipynb will show the code of the results of extracting out location names from narratives and getting their longitudes and latitudes.
```
GeoTopicParser.ipynb
```

In the Q1_image_code folder, open Q1.ipynb will show the code to visualize correlations among gender, age, interest and geolocation mentioned. This is the answer towards report question 1.
```
Q1.ipynb
```

In the Q3_4_image_code folder, open Q3.ipynb will show the code to visualize correlations between post language and identified mentioned locations. This is the answer towards report question 3.
```
Q3.ipynb
```
In the Q3_4_image_code folder, open Q4.ipynb will show the code of the results about correlations between the sporting events, or the entertainment events with locations. This is the answer towards report question 4.
```
Q4.ipynb
```

## Methodology

#### Step7: Download images, Install Tika Image Dockers and generate captions for Pixstory images posts
I wrote a python script to modify URLs with prefix “/optimized” and download 95k images. I used Dockers for Image Captioning and Object Recognition. Commands for captions and objects are:

``` 
docker build -f Im2txtRestDockerfile -t uscdatascience/im2txt-rest-tika
docker run -p 8764:8764 -it uscdatascience/inception-rest-tika
docker build -f InceptionRestDockerfile -t uscdatascience/inception-rest-tika 
docker run -p 8764:8764 -it uscdatascience/inception-rest-tika
``` 
I added two columns, Image Caption and Detected Objects, to the dataframe. Codes to download images, find captions, identify objects, analyze and visualize can be found in Step7/ImageDownloadDetect.ipynb.

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

#### Step10: Location nname entity recognition by Tika GeoTopicParser with REST service of lucene-geo-gazetteer to find Lat/Lng
Following instructions on slack and GeoTopicParser website to set up the REST service of lucene-geo-gazetteer, NER location model, geotopic-parser, and geotopic-server. The core code running in python is listed below.
```
parser.from_buffer
```



#### Step11: Detoxify Scores Generation
This step uses the 'rtg_translate' column derived from RTG Translation. A script written in Python iterates through each value within the column, passes it as input string into detoxify, and saves score from each category into corresponding columns. Since RTG translated most of the posts into English, we ruled out the 'multilingual' model. Considering the additional 'sexual_explicit' category would provide more insights about these Pixstory posts, we determined to use the 'unbiased' model for all entries.

With combine_add_geo.csv (in folder Step10 - GeoTopicParser) and detoxify_scores.py (in folder Step11 - Detoxify) in the same folder, running the following command will generate a final.tsv with 7 more columns for scores: 'Toxicity', 'Severe_Toxicity', 'Obscenity', 'Identity_Attack', 'Insult', 'Threat', 'Sexual_Explicit'. For the posts that cannot be handled by RTG, which means they have a null value for 'rtg_translate', the scores are assigned to be null as well.
```
python3 detoxify_scores.py
```





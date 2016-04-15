# Aspect-Based-Sentiment-Analysis
Sentiment analysis is increasingly viewed as a vital task both from an academic and a commercial standpoint. The majority of current approaches, however, attempt to detect the overall polarity of a sentence, paragraph, or text span, regardless of the entities mentioned (e.g., laptops, restaurants) and their aspects (e.g., battery, screen; food, service). By contrast, this task is concerned with aspect based sentiment analysis (ABSA), where the goal is to identify the aspects of given target entities and the sentiment expressed towards each aspect. Datasets consisting of customer reviews with human authored annotations identifying the mentioned aspects of the target entities and the sentiment polarity of each aspect will be provided.
Description
Sentiment analysis is increasingly viewed as a vital task both from an academic and a commercial standpoint. The
majority of current approaches, however, attempt to detect the overall polarity of a sentence, paragraph, or text
span, regardless of the entities mentioned (e.g., laptops, restaurants) and their aspects (e.g., battery, screen; food,
service). By contrast, this task is concerned with aspect based sentiment analysis (ABSA), where the goal is to
identify the aspects of given target entities and the sentiment expressed towards each aspect. Datasets consisting
of customer reviews with human authored annotations identifying the mentioned aspects of the target entities
and the sentiment polarity of each aspect will be provided.

In particular, the task consists of the following subtasks:
Subtask 1: Aspect term extraction
Subtask 2: Aspect term polarity
Subtask 3: Aspect category detection
Subtask 4: Aspect category polarity

Datasets Used:
We used the datasets from SemEval 2016 ABSA datasets for restaurant reviews.

Steps:

1) Download stanford-corenlp suite from https://www.dropbox.com/sh/rk3901gi9l50d54/AACrT_RwI84HWFfclrRTTkVNa?dl=0
    This should be kept in the same folder as the project.
2) Run corenlp.py
3) Run client.py
    The program uses absa--test.xml as the test dataset.
4) Run aspect_term_extarctor.py
    This extracts all the aspect terms from each review in the test file.
5) Run pol.py
    This calculates the polarities of the aspect terms.
6) Run categorizer.py
    This places all the aspect terms in respective categories.
7) Run catpol.py
    This calculates polarities of the aspect category.
8) finally run makeXML.py
    This collects all the extracted data and combines them to an xml file in the same format as the test file.


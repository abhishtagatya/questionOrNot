# QuestionOrNot Classifier

An attempt to classify a sentence scraped using selenium containing a list of sentences and predict if such sentence is a question.

### Requirements

Anaconda Library:
  - pip=18.1
  - numpy=1.15.4
  - matplotlib=3.0.1
  - pandas=0.23.4
  - scikit-learn=0.20.1
  - jupyter=1.0.0
  - requests=2.22.0

Install the library by the instruction below.

### Installation

Install the dependencies and create the Anaconda Enviroment.

```sh
$ conda env create -f nlp_qa_env.yml --name nlp_class_question
$ conda activate nlp_class_question
```

### Play Around

Feel free to play around with the `question_or_not.tsv` or `question_or_not_cleaned.tsv` (only different is the ratio between sentence labeled question or not)

- Scraping :
    Included a script to scrape the sentence from a website `sentence_generator_scraper.py`
- Text Selection :
   Included a script to clean the data that has been scraped in `text_selection.py`
- Text Classification :
   Included a train the pipeline of TFIDF-Vectorizer and LinearSVC in `text_classification.py`

### Current Result

with `question_or_not_cleaned.tsv`

```sh
VALUE COUNTS
False    750
True     250

CONFUSION MATRIX
[[172  15]
 [ 19  44]]
 
CLASSIFICATION REPORT
              precision    recall  f1-score   support

       False       0.90      0.92      0.91       187
        True       0.75      0.70      0.72        63

   micro avg       0.86      0.86      0.86       250
   macro avg       0.82      0.81      0.82       250
weighted avg       0.86      0.86      0.86       250

ACCURACY SCORE
86.4% Accurate
```
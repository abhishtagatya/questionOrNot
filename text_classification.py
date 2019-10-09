import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

df = pd.read_csv('question_or_not_cleaned.tsv', sep='\t')

print('NULL DATA')
print(df.isnull().sum())
print('\nVALUE COUNTS')
print(df['Question'].value_counts())

X = df['Sentence']
y = df['Question']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, shuffle=False
)

print(len(X_train), len(X_test), len(y_train), len(y_test))

text_classifier = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LinearSVC())
])
text_classifier.fit(X_train, y_train)

predictions = text_classifier.predict(X_test)

# Confusion Matrix
print("CONFUSION MATRIX")
print(confusion_matrix(y_test, predictions))

print("CLASSIFICATION REPORT")
print(classification_report(y_test, predictions))

print("ACCURACY SCORE")
print(f"{accuracy_score(y_test, predictions) * 100}% Accurate")

while(True):
    sentence = input()
    print(text_classifier.predict([sentence]))

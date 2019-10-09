from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd
import random

sentence_generator = 'http://www.bestrandoms.com/random-sentence'

driver = webdriver.Chrome(executable_path='.\chromedriver77.exe')

sentence_set = set()

scrape_iteration = int(input("Enter Scrape Amount : "))

for i in range(scrape_iteration):

    driver.get(sentence_generator)
    page = driver.page_source

    soup = BeautifulSoup(page, 'html.parser')
    sentence_found = soup.find_all('p', class_='font-18')

    for j in sentence_found:
        question = False

        sentence = j.find('b').find('span').text

        if '?' in sentence:
            question = True
        else:
            if (random.choice([True, False, False])): continue

        sentence_set.add((sentence, question))
    print(f'Scraped : {i}')

print(sentence_set)

driver.quit()

data = {}
df = pd.DataFrame(data)

sentence_list = []
answer_list = []
s = [(sentence_list.append(i), answer_list.append(j)) for i, j in list(sentence_set)]

df['Sentence'], df['Question'] = sentence_list, answer_list

df.to_csv('question_or_not2.tsv', sep='\t', encoding='utf-8')

print(f'SUCCESS! Scraped {scrape_iteration} and set of {len(sentence_list)}')
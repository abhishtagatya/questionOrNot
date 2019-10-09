import pandas as pd
import random

df = pd.read_csv('question_or_not2.tsv', sep='\t')

len_df = (df.shape)[0]

false_list, true_list = [], []

for i in range(len_df):
    if (df.iloc[i]['Question'] == False):
        if (len(false_list) < 250):
            false_list.append((df.iloc[i]['Sentence'], False))
        continue
    true_list.append((df.iloc[i]['Sentence'], True))

true_list.append(('Robert, did you water the plants today?', True))
true_list.append(('Kevin forgot his wallet?', True))
true_list.append(('Are you even trying or what?', True))

combined_list = true_list + false_list

random.shuffle(combined_list)

data = {}
df = pd.DataFrame(data)

sentence_list = []
answer_list = []
s = [(sentence_list.append(i), answer_list.append(j)) for i, j in combined_list]

df['Sentence'], df['Question'] = sentence_list, answer_list
df.to_csv('question_or_not_cleaned2.tsv', sep='\t', encoding='utf-8')


print("SUCCESS")

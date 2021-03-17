import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re
import spacy
#nlp = spacy.load('en_core_web_lg')
from twitterscraper import query_tweets
from twitterscraper.query import query_tweets_from_user
import datetime as dt
import pandas as pd

d = dt.timedelta(days=2)

end_date = dt.datetime.now()
begin_date = end_date-d


limit = 100
lang = 'english'

#Use this to search a specific user

user = 'livemint'
tweets = query_tweets_from_user(user)
df = pd.DataFrame(t.__dict__ for t in tweets)

df = df.loc[df['screen_name'] == user]

df = df['text']

df

#Use this if wanting to seach for a specific Phrase or word

#tweets = query_tweets('impeachment', begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
#df = pd.DataFrame(t.__dict__ for t in tweets)

#df = df['text']

#df

#This splits all the sentences up which makes it easier for us to work with

all_sentences = []

for word in df:
    all_sentences.append(word)

all_sentences
#df1 = df.to_string()

#df_split = df1.split()

#df_split
lines = list()
for line in all_sentences:
    words = line.split()
    for w in words:
       lines.append(w)


print(lines)

#Removing Punctuation

lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]

lines

lines2 = []

for word in lines:
    if word != '':
        lines2.append(word)

# This is stemming the words to their root
from nltk.stem.snowball import SnowballStemmer

# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')

stem = []
for word in lines2:
    stem.append(s_stemmer.stem(word))

stem

#Removing all Stop Words

# stem2 = []
#
# for word in stem:
#     if word not in nlp.Defaults.stop_words:
#         stem2.append(word)
#
# stem2
#
# df = pd.DataFrame(stem2)
#
# df = df[0].value_counts()

#df
#df['freq'] = df.groupby(0)[0].transform('count')
#df['freq'] = df.groupby(0)[0].transform('count')
#df.sort_values(by = ('freq'), ascending=False)

#This will give frequencies of our words

from nltk.probability import FreqDist

freqdoctor = FreqDist()

for words in df:
    freqdoctor[words] += 1

freqdoctor

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#This is a simple plot that shows the top 20 words being used
#df.plot(20)

df = df[:20,]
plt.figure(figsize=(10,5))
sns.barplot(df.values, df.index, alpha=0.8)
plt.title('Top Words Overall')
plt.ylabel('Word from Tweet', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()

# import spacy
# from spacy import displacy
# from collections import Counter
# import en_core_web_sm
# nlp = en_core_web_sm.load()
#
# def show_ents(doc):
#     if doc.ents:
#         for ent in doc.ents:
#             print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
#
# str1 = " "
# stem2 = str1.join(lines2)
#
# stem2 = nlp(stem2)
#
# label = [(X.text, X.label_) for X in stem2.ents]
#
# df6 = pd.DataFrame(label, columns = ['Word','Entity'])
#
# df7 = df6.where(df6['Entity'] == 'ORG')
#
# df7 = df7['Word'].value_counts()
#
# df = df7[:20,]
# plt.figure(figsize=(10,5))
# sns.barplot(df.values, df.index, alpha=0.8)
# plt.title('Top Organizations Mentioned')
# plt.ylabel('Word from Tweet', fontsize=12)
# plt.xlabel('Count of Words', fontsize=12)
# plt.show()

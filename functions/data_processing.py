import re
import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from collections import defaultdict


# nltk.download('stopwords')

## ---------------------------------------------------------- used in 01_data_cleaning---------------------------------------------------##


def remove_urls(vTEXT):
    """
    takes a string and removes urls
    """
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b',
                   ' ', vTEXT, flags=re.MULTILINE)
    return(vTEXT)


def retrieve_hashtag(org_string):
    pattern = re.compile(r'#\w{1,}')
    matches = pattern.finditer(org_string)
    hashtags = [match.group(0) for match in matches]
    return hashtags


def retrieve_mentions(org_string):
    pattern = re.compile(r'@\w{1,}')
    matches = pattern.finditer(org_string)
    mentions = [match.group(0) for match in matches]
    return mentions


def remove_punctuations(org_string):
    org_string = re.sub(r'&amp', "", org_string)
    pattern = re.compile(r'\b\w+\b')
    filtered = " ".join(m.group(0) for string in org_string.split()
                        for m in [pattern.search(string)] if m)
    return filtered


# def remove_punctuations(vTEXT):
#     tmp = re.sub(r'&amp', "", vTEXT)
#     tmp = re.sub(r'\n', "", tmp)
#     vTEXT = re.sub(r'[^\w\s]+', ' ',
#                    tmp, flags=re.MULTILINE)
#     return(vTEXT)

def remove_stopwords(text, remove_word=[]):
    stop = stopwords.words('english')
    stop.extend(remove_word)
    removed = " ".join(x for x in text.split() if x not in stop)
    return removed


lemmatizer = nltk.WordNetLemmatizer()


def lemmatize(text):
    text = " ".join(lemmatizer.lemmatize(word, pos="v")
                    for word in text.split())
    return text

## ---------------------------------------------------------- used in 02_Exploratory_Data_Analysis---------------------------------------------------##


def count_words(sentences, remove_word=[]):
    d = defaultdict(int)

    for text in sentences.split():
        # iterate over sentences
        if text not in remove_word:
            if text in d:
                d[text] = d[text]+1
            else:
                d[text] = 1
    return d


def count_words_in_df(df, col, remove_word=[]):
    d = defaultdict(int)
    keys = d.keys()
    values = d.values()
    for sentence in df.loc[:, col]:
        d_tmp = count_words(sentence, remove_word)
        for key, val in d_tmp.items():
            if key not in keys:
                d[key] = val
            else:
                d[key] += val

    return d

## -------------------------------------------------- used in 03_Vectorization_and_dimension_reduction.ipynb---------------------------------------------------##

import re
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')


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

def remove_stopwords(text):
    stop = stopwords.words('english')
    removed = " ".join(x for x in text.split() if x not in stop)
    return removed

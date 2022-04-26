import re


def remove_urls(vTEXT):
    """
    takes a string and removes urls
    """
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b',
                   ' ', vTEXT, flags=re.MULTILINE)
    return(vTEXT)


# def remove_punctuations_urls(vTEXT):
#     """
#     takes a string and remove urls and punctuations,
#     calls the remove_urls() function for url removal
#     """
#     vTEXT = re.sub(r'\n', ' ', re.sub(
#         r"[^\w\s\']", '', remove_urls(vTEXT)))
#     return(vTEXT)

def remove_punctuations_urls(vTEXT):
    """
    takes a string and remove urls and punctuations,
    calls the remove_urls() function for url removal
    """
    tmp = re.sub(r'&amp', "", remove_urls(vTEXT))
    tmp = re.sub(r'\n', "", tmp)
    vTEXT = re.sub(r'[^\w\s\'\@\#]+', ' ',
                   tmp, flags=re.MULTILINE)
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

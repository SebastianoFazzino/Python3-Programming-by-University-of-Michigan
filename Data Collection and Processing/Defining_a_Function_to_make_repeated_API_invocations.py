#Let’s make a python function to contact the datamuse API repeatedly, passing different values associated with the key rel_syn (standing for synoninyms). 


import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_syn"] = word
    params_diction["max"] = "5" # get at most 5 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]



print(get_rhymes("clever"))


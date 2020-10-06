import requests
import json

#We use requests.get to fetch the contents of a web page
page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")

#we can see that the variable page is a requests object
print(type(page))

print(page.text[:150]) # print the first 150 characters

print(page.url) # print the url that was fetched

print("------")

# .json() convert the page into a python object and assigns it to the variable x
x = page.json() 

#printing x, we see that we're dealing with a list of dictionaries
print(type(x))

print("---first item in the list---")

print(x[0])

print("---the whole list, pretty printed---")

print(json.dumps(x, indent=2)) # pretty print the results




#The get function in the requests module takes an optional parameter called params. 
#If a value is specified for that parameter, it should be a dictionary.


kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched




#another example

d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)






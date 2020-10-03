#the two most common functions used when dealing with josn files are
#  loads and dumps


#we always start importing json
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
print(type(a_string))

#json.loads() takes a string as input and prodices a python object(a dictionary or a list) as output
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
print(d['results'][0])



#json.dumps() does the inverse of load: it takes a python object as input and it returns a string
def pretty(obj):
                     #dumps takes different parameters, one has always to be a python object,
                     #we ca also sort the keys and indent will print some indentation in the output string
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
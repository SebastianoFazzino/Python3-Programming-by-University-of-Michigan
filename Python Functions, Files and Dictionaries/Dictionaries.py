#Creating a new dictionary key and value through an operation:

animals = {"cat":12, "dog":6, "elephant":23}
animals['lion'] = animals['cat'] + animals['dog']
print(animals)


#updating a value in a dictionary:
    
animals['lion'] = animals['lion'] + 5
print(animals['lion'])



#how to get a list of keys and values from a dictionary:

print(list(animals.keys()))
print(list(animals.values()))
print(list(animals.items()))



#how to iterate through a dictionary keys:
    
for key in animals.keys():
    print(key, "new value is:", animals[key] +5)
    

total = 0
for key in animals:
    if len(key) > 3:
        total += animals[key]
print(total)
    
    
#using boolean operator in a dictionary:
    
print('lion' in animals)
print('tiger' in animals)

if 'cat' in animals:
    print(animals['cat'])
else:
    print('there are no cats in this dictionary!')
    
    

# .get method and dictionaries

print(animals.get('dog'))

# if we use .get with a key that is not in the dictionary, the output will be 'None'
print(animals.get('shark'))

# if we pass two values to the get method, we'll create a new key, if it's not in the dictionary already
print(animals.get('shark',10))


#aliasing and copying

opposites = {'up':'down', 'right':'wrong','ture':'false'}
alias = opposites

print(alias is opposites) #this returns True

alias['right'] = 'left'

print(opposites['right']) 
#the value of key 'right' has changed to 'left' in both opposites and alias dictionaties

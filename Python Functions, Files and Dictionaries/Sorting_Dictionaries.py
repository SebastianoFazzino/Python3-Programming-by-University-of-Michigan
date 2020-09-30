#Sorting a dictionary

L = ['E','F','B','A','D','I','I','C','B','A','D','D','D','E']

D ={}

for letter in L:
    if letter in D:
        D[letter] += 1
    else:
        D[letter] = 1
        
for letter in sorted(D.keys()):  #this will sort the dictionary keys in alphabetic order
    print("{} appears {} times".format(letter, D[letter]))

print("\n-----------------\n")

for letter in sorted(D.keys(), key = lambda k: D[k]): #this will sort the dictionary values, from the smallest to the bigger
    print("{} appears {} times".format(letter, D[letter]))
    
print("\n-----------------\n")
   
#we'll now reverse the order of sorting values:  
for letter in sorted(D.keys(), key = lambda k: D[k], reverse = True): 
    print("{} appears {} times".format(letter, D[letter]))
    
    
      
#Some excercise   
    
#Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary.keys())




#Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to buy at the store. 
#Sort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

grocery_keys_sorted = sorted(groceries.keys())




#Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary.keys(), key = lambda k: dictionary[k], reverse = True)




#some more sortings:
    
L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k, d):
    return d[k]

ks = d.keys()

print("\n---------------------\n")

print(sorted(ks, key=lambda x: g(x, d)))
print(sorted(ks, key=lambda x: d[x]))



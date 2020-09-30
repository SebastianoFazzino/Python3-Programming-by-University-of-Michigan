
#sorting tuples

Tuples = [('A', 3, 2),
          ('C', 1, 4),
          ('B', 3, 1),
          ('A', 2, 4),
          ('C', 1, 2)]

for tup in sorted(Tuples): #this will sort tuples starting from the first value inside them
    print(tup)

print("\n---------------------\n")


#we're going to sort the elements in the list 'fruit' by their length
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear', 'banana' ] 
new_order = sorted(fruits, key = lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

print("\n---------------------\n")
    

#let's say we want the longest word to print ou first, but break ties,
#with alphabetic order rather then reverse aphabetic order:
                              
                                                    #we simply add a minus sign before len()
new_order = sorted(fruits, key = lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)
#we now have the fruits ordered by their length first and then by lphabetical order,
#however this only works if we have a bumeric property


print("\n---------------------\n")


#let's say that we want to sort the element in this dictionary, starting sorting cities by alphabetical order,
#and then by temperature, lowest to highest:
    
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key = lambda city: (city, weather[city]['temp']))
print(sorted_weather)















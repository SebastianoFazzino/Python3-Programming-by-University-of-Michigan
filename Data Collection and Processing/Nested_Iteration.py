nested1 = [['a','b','c'],['d','e'],['f','g','h'],[12,55,96]]
for I in nested1:
    print("level 1: ")
    for i in I:
        print("    level 2: " + str(i))
        
        
print("--------------------------------------")

 
       
#given the follow nested lists, let's say we want to retrieve every last name and save those values in the variable last
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last = []

for last_names in info:
    last.append(last_names[1])
        
    print(last)
        

print("--------------------------------------")


#more examples:
#let's say we want to save every string containing 'b' into a new list called b_strings
List = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []

for items in List:
    for word in items:
        if 'b' in word:
            b_strings.append(word)
            
print(b_strings)
     

print("--------------------------------------")

#when we deal with different types of data structures, we need to use different approaches accordingly:

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1:  ")
    #in this case, if we try to directly iterate through the elements in the list, we'll get an error message;
    #that's wh we need to use a different approach, using an 'if' statement to check the data types in the list
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))   
            
    else:
        print(x)
        

#Nested Lists

nested1 = [['a','b','c'],['d','e'],['f','g',]]
print("let's print the first element in the list:",nested1[0])
print(len(nested1))

nested1.append(['i'])
#after appending one more element to the list, its length will be 4
print(len(nested1))

#we can also append a value to a list element:
nested1[0].append('1')
nested1[1].append(2)

#we can iterate through the list elements and print them:
for elements in nested1:
    print(elements)
    
    
#we can use double indexing to print elements in the list:
print(nested1[0][2]) #this statement will print 'c'
print(nested1[2][1]) #this statement will print 'g'


#we can assign new values to element in the list:
nested1[1][0]= 100
print(nested1[1]) #element in position 1 is now [100, 'e', 2]



#we can also have a list of functions:

def square(x):
    return x*x

List = [square, abs, lambda x: x+1]

print("\n****names****")
for f in List:
    print(f)
    
print("\n****call each of them****")
for f in List:
    print(f(-2))

print("\n****just the first one in the list****")
print(List[0])
print(List[0](3))  



#given the following list, let's say we want to retrieve the string 'elm':

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
elm = data[7][0][2]
print("\n",elm)


    

#The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like lists for most practical purposes), 
#pairing up all the first items as one tuple, all the second items as a tuple, and so on. 
#Then we can iterate through those tuples, and perform some operation on all the first items, all the second items, and so on.


l1 = [3, 4, 5]
l2 = [1, 2, 3]
l3 =[]

#in the code below we add the value of l1[i] to l2[i] using a for loop and append method
for i in range(len(l1)):
    l3.append(l1[i] + l2[i])

print('Using for loop:',l3)

#we can zip the two lists together using zip function

l3 = list(zip(l1,l2))

#and the output will be a list of tuples
print('Using zip function:',l3)

#once we've created this zip-together list, we can combine the numbers in the tuples as follow:
l4 = []
for num1, num2 in l3:
    l4.append(num1 + num2)


#or, more simply, we could use a list comprehension
l5 = [num1 + num2 for (num1, num2) in list(zip(l1, l2))]
print('Using list comprehension:',l5)


#we can also use map function to execute the same operation:
l6 = map(lambda num: num[0] + num[1], zip(l1,l2))
print('Using map function:',list(l6))



print("*************************************")




#Exercise:
#Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, 
#that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can be accomplished in one line of code.

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [ (l1+l2) for (l1,l2) in list(zip(L1,L2)) if (l1>10 and l2<5) ]
print(L3)




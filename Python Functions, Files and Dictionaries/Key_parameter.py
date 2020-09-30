
lst1 = [1, 7, -66, 8, 96, 11]

def absolute_func(x):
    print("---figuring out what to write on the post-it note for " + str(x))
    if x > 0:
        return x
    else:
        return -x
    

for n in lst1:
    print(absolute_func(n))
    
 
    
 
#Optional Key Parameter:
    
lst2 = sorted(lst1, key = absolute_func)
print(lst2)
#passing the function absolute as key, -66 will print after 1,7,8 and 11, because its absolute value
#is bigger than the previous numbers


#or in reverse order:  
print("\n...about to call sorted...")  
print(sorted(lst1, reverse = True, key = absolute_func))
print("finished execution of sorted! ")


#we can also use a lambda expression to pass a key parameter:
    
lst3 = sorted(lst1, key = lambda x: absolute_func(x))
print(lst3)



#You will be sorting the following list by each element’s second letter, a to z. 
#Create a function to use when sorting, called second_let. It will take a string as input and return the second letter of that string. Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(x):
    return x[1]

sorted_by_second_let= sorted(ex_lst, key= second_let)
        



#Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, and returns only its last character. 
#Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(x):
    return(x[-1])

nums_sorted = sorted(nums, key = last_char, reverse = True)





#Once again, sort the list nums based on the last digit of each number from highest to lowest. 
#However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']


nums_sorted_lambda = sorted(nums, reverse = True, key = lambda x: x[-1])



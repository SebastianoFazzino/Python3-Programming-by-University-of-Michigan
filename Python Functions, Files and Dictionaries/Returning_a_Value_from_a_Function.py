#Returning a value from a function:
    
def square(x):
    '''This function is used to square numbers'''
    y = x * x
    return y

to_square = int(input('Enter the number to square: '))
result = square(to_square)

print('The result of {} squared is {}'.format(to_square, result))



#A return statement, once executed, immediately terminates execution of a function

def weird():
    print("here")
    return 5
    print("there")
    return 10
#in this function, print('here') and return 10 will never execute.
x = weird()
print(x)







def name_length(list_of_names):
    '''This function will iterate through a list of names
    and will return True if one of the name length is > 5 and 
    False if none of the names length is > 5'''
    
    for name in list_of_names:
        if len(name) > 5:
            return True
    return False

list1 = ['Sam','Tera','John']
list2 = ['Natalie','Mark','Paris']

print(name_length(list1))
print(name_length(list2))

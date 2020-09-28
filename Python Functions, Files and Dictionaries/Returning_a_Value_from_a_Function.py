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





def total(lst):
    tot = 0
    for num in lst:
        tot = tot + num
    return tot
    
    
y = total([1,2,3])
print(y)




#functions can call other functions, this process is called "Composition"
    
def square(x):
    y = x * x
    return y

def sum_of_square(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)
    
    return a + b + c

a = -5
b = 2
c = 10

result = sum_of_square(a,b,c)
print(result)





#this function will return the most common letter out of a string:

def most_common_letter(s):
    frequencies = count_freq(s)
    return best_key(frequencies)


def count_freq(Str):
    Dict = {}
    for char in Str:
        if char not in Dict:
            Dict[char] = 0
        Dict[char] = Dict[char] + 1
    return Dict
        
        
def best_key(dictionary):
    Keys = dictionary.keys()
    best_key_so_far = list(Keys)[0]
    for key in Keys:
        if dictionary[key] > dictionary[best_key_so_far]:
            best_key_so_far = key
            
    return best_key_so_far


sentence = input("Enter a sentence: ")
print(most_common_letter(sentence))
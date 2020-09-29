
def f(x):
    return x - 1

print(f(3))


#lambda expressions are utilized to construct anonymous functions. 
#To do so, we will use the lambda keyword

#we don't need to add a return statement for lambda expressions,
#the return is implicit

lambda_call = lambda x: x -1
print(lambda_call(3))
print((lambda x: x-2)(6))


print(type(f))              #both print statements will return 
print(type(lambda_call))    #class 'function'



def last_char(Str):
    return(Str[-1])

#we can write the same funcion using lambda as follows:
    
lastChar = lambda Str: Str[-1]


print(lastChar("hello"))     #both print statements will have 
print(last_char("hello"))    #the same output





#more examples:
    
num = lambda z: -z
print(num(5))
print(num(-9))



square = lambda a: a * a
print(square(5))



sample = lambda b: b % 3
print(sample(11))








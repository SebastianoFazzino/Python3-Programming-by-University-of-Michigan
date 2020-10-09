#A test case expresses requirements for a program, in a way that can be checked automatically. Specifically, a test asserts something about the state of the program at a particular point in its execution.

#assume we have a function and we want to test if its output is as expeted

def square(x):
    return x * x
    
#now we write the assert statement followed by the function to test,
#the output that we expect from the function and an error message in case 
#the function output is different from what we expect

assert square(10) == 100, "The output of square(10) is 100!"
#since the function passed the test, nothing gets printed



#let's write another assert statement where an error message gets printed:
    
assert square(5) == 30, "The output of square(5) is 25!" #this message gets printed!

#more examples:
    
x = 2
y = 3

assert x + y == 6, "I think this is wrong!!!"

assert 19 % 2 == 0, "Nope!"

assert sorted([5, 66, 9, 8]) == [5, 8, 9, 66], 'Almost!'

assert sorted([5, 66, 9, 8], reverse = True) == [66, 9, 8, 5], 'Almost!'



#it is important to specify that if one of the assert statement triggers an error message,
#no codes following that statement get executed


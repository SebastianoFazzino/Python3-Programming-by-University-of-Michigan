#The try/except control structure provides a way to process a run-time error and continue on with program execution.


try:
    items = ['a', 'b']
    third = items[2] #we go an index error here
    print("This won't print") #hence this statement won't be executed
except Exception:
    print("got an error") 

print("continuing")



try:
    x = 5
    y = x/0 
    print("This won't print, either")
except:
    print("error 2")


print("continuing again")


#There’s one other useful feature. The exception code can access a variable that contains information about exactly what the error was. 
#Thus, for example, in the except clause you could print out the information that would normally be printed as an error message but continue on with execution of the rest of the program. 
#To do that, you specify a variable name after the exception class that’s being handled. The exception clause code can refer to that variable name.

try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e: #the error type has been assigned to the variable 'e'
    print("got an error")
    print(e) #so we can print the error message, in this case 'list index out of range'

print("continuing")

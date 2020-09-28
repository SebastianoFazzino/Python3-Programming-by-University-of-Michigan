#Break and Continue Statements:
    
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?") #This print statement will never be executed

print("We are done with the while loop.")






x = 0
while x < 100:
    print('''We are incrementing x!
          \n----------------------''')
    if x % 2 == 0:
       x += 3
       continue
    if x % 3 == 0:
        x += 5
        
    x += 1
    
print("Done with the loop! X has value: " + str(x))


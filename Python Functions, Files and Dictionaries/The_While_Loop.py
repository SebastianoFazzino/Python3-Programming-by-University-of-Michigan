#The While statement

def sumTo(aBound):
    
    '''Returns the sum of 1+2+3...n'''    
    theSum = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(99))

        

count = 0
even_nums =[]

while count <= 15:
    if count % 2 == 0:
       even_nums.append(count)  
    count = count + 1
    
print("\nEven numbers on a range of 15:",even_nums,'\n')


index = 0
accum = 0
while index < len(even_nums):
    accum += even_nums[index]
    index += 1
print("Sum of numbers in 'even_nums':",accum)




# the listener loop is essentially a pattern that waits for some input or some value before deciding to terminate the loop.
#here's an example of listener loop:
    
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum += x
    
print("The Sum:",theSum)




def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print("Please enter Y for yes or N for no.")
            
        return answer
    
response = get_yes_or_no("Do you like lima beans? Y)es or N)o: ")   
if response == 'Y':
    print("Great! They are very healthy.")
elif response == 'N':
    print("Too bad. If cooked right, they're quite tasty.")







def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()



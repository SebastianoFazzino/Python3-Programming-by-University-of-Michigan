#to read a file we start creating a file object using open('filename','r'), where 'r' stands for 'read'

file = open('Olympics.txt','r')

#we use 'readlines' or 'read' to read the file
lines = file.readlines()
characters = file.read()

#we can print the number of lines or characters in the file
print(len(lines))
print(len(characters))

#or we iterate through the file object and print all the lines
for line in lines:
    print(line.strip())
    
file.close()
    


#this is another way for opening a file:

with open ('Olympics.txt','r') as data:
    for line in data:
        print(line)

#When we use 'with' we don't need to close() the file after we have finished working on it.
    
    
   
    
   
    
#to write text files the procedure is pretty similar:
    
file_obj = open('squares.txt','w')
for number in range(15):
    square = number * number
    file_obj.write(str(square) + '\n')
    
file_obj.close()
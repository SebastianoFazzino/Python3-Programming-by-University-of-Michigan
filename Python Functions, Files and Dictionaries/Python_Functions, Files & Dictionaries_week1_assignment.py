#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
#Find the total number of characters in the file and save to the variable num

file = open('travel_plans.txt')
file_reader = file.read()

num = len(file_reader)




#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
#Find the total number of words in the file and assign this value to the variable num_words.

file = open("emotion_words.txt")
file_reader = file.read()
words = file_reader.split()

num_words = 0
for word in words:
    num_words += 1
    
print(num_words)




#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

file = open("school_prompt.txt")
file_reader = file.readlines()

num_lines = 0

for line in file_reader:
    num_lines += 1
    
print(num_lines)



#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

file = open("school_prompt.txt")
file_reader = file.read()

beginning_chars = ""
for word in file_reader[:30]:
    beginning_chars = beginning_chars + word 

    
print(beginning_chars)





#Using the file school_prompt.txt, assign the third word of every line to a list called three.

file = open("school_prompt.txt")
file_reader = file.readlines()

three =[]
for lines in file_reader:
    words = lines.split()
    three.append(words[2])
        
    
    
 
    
#Create a list called emotions that contains the first word of every line in emotion_words.txt.

file = open("emotion_words.txt")
file_reader = file.readlines()

emotions = []

for lines in file_reader:
    words = lines.split()
    emotions.append(words[0])



#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.


file = open('travel_plans.txt')
first_chars = file.read()[:33]





#Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

file = open("school_prompt.txt","r")
file_reader = file.read()

words = file_reader.split()

p_words = []

for word in words:
    if 'p' in word:
        p_words.append(word)
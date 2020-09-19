#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. 
#Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, 
#count the number of items with values > 3.0.

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0
Temps = rainfall_mi.split(",")
for temp in Temps:
    if float(temp) > 3:
        num_rainy_months += 1
        
 
    
 
#The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, 
#including one-letter words. Store the result in the variable same_letter_count.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

same_letter_count = 0
words = sentence.split(" ")
for word in words:
    if word[0] == word[-1]:
        same_letter_count += 1
        
       
        
       
#Write code to count the number of strings in list items that have the character w in it. 
#Assign that number to the variable acc_num.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0
for word in items:
    if "w" in word:
        acc_num += 1
        
        
        
        
#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.


sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

num_a_or_e = 0
words = sentence.split(" ")
for word in words:
    if "a" in word or "e" in word:
        num_a_or_e += 1
        
        
        
        
#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0

for letter in s:
    if letter in vowels:
        num_vowels += 1

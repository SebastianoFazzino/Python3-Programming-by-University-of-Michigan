
#Below are a set of scores that students have received in the past semester. Write code to determine how many 
#are 90 or above and assign that result to the value a_scores
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores = scores.split(" ")
a_scores = 0
for score in scores:
    if int(score) >= 90:
        a_scores = a_scores + 1
        




#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. 
#Only the first letter of each word should be used, each letter in the acronym should be a capital letter, 
#and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

acro = ""
unwanted = ""
needed = ""
words = org.split(" ")
needed = needed + words[1], words[3], words[4], words[6]
unwanted = unwanted + words[0], words[2], words[5]

for word in unwanted:
    stopwords.append(word)

for word in needed:
    acro = acro + (word[0]).upper()
    
    
    
    
#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. 
#The first two letters of each word should be used, each letter in the acronym should be a capital letter, 
#and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. 

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = ""
unwanted = ""
needed = ""
words = sent.split(" ")
needed = needed + words[1], words[2], words[4], words[5], words[6]
unwanted = unwanted + words[0], words[3]

for word in unwanted:
    stopwords.append(word)
    
for word in needed:
    acro = acro + (word[0:2]).upper() + ". "
acro = acro[:-2]



#A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it 
#and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"

r_phrase = len(p_phrase)
r_phrase = p_phrase[r_phrase ::-1]



#Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, 
#how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). 
#For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]


for items in inventory:
    items = items.split(",")
    item = items[0]
    qty = items[1]
    price = items[2]
    
    print("The store has {} {}, each for {} USD.".format(qty, item, price))
    
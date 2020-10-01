#We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. 
#At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

#To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(Str):
    for p in punctuation_chars:
        Str = Str.replace(p, '')
    return Str

#Next, define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. 
#Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
            
#then, with get_pos function, we count how many positive words are there in the string we pass through the function           
def get_pos(s):
    s = strip_punctuation(s).split()
    
    positive_counter = 0
    for word in positive_words:
        for w in s:
            #we must use lower() method in the comparison to get the right number of positive words
            if w.lower() == word:
                positive_counter += 1
        return positive_counter


#Next, define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. 
#Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. 
#Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
           

#then, with get_neg function, we count how many negative words are there in the string we pass through the function           
def get_neg(s):
    s = strip_punctuation(s).split()
    negative_counter = 0
    for words in negative_words:
        for w in s:
            if w.lower() == words:
                negative_counter += 1
    return negative_counter


#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). 
#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. 
#Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order.


TwitterData = open("project_twitter_data.csv","r")
ResultingData = open("resulting_data.csv","w")



def write(ResultingData):
    ResultingData.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    ResultingData.write("\n")
    
    #we read the file ResultingData and we iterate through the lines to get the data needed
    file_read =  TwitterData.readlines()
    file = file_read[1:]  
    for lines in file:
        lines = lines.strip().split(',')
        
        #we then write the data into the file
        rows = ("{}, {}, {}, {}, {}".format(lines[1], lines[2], get_pos(lines[0]), get_neg(lines[0]), (get_pos(lines[0])-get_neg(lines[0]))))    
        ResultingData.write(rows)
        ResultingData.write("\n")

        
#we call the function 'write' and to finish we close the files       
write(ResultingData)

TwitterData.close()
ResultingData.close()




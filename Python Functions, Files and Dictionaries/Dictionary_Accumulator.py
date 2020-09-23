file = open('Olympics.txt','r')
file_reader = file.read()

Dict = {}
Dict['t'] = 0
Dict['s'] = 0

for letter in file_reader:
    if letter == 't':
        Dict[letter] += 1
    elif letter == 's':
        Dict[letter] += 1
        
print('t: ' + str(Dict['t']) + ' occurrences')
print('s: ' + str(Dict['s']) + ' occurrences')
    


#we can use the accumulator for every letter in the file:
    
new_Dict = {}

for letter in file_reader:
    if letter not in new_Dict:
        new_Dict[letter] = 0
        
    new_Dict[letter] += 1


#and print the total number of each letter:
    
for letter in new_Dict.keys():
    print(letter + ": " + str(new_Dict[letter]) + " occurrences")
    
    

#accumulating result from a dictionary:

animals = {"cat":12, "dog":6, "elephant":23, 'shark':13}
total = 0

for count in animals:
    total = total + animals[count]
print(total)

    

#Scrabble score calculator:

letter_values = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':8,'w':4,'x':8,'y':4,'z':10}
scrabble_score = 0
for letter in new_Dict:
    if letter in letter_values:
        scrabble_score = scrabble_score + letter_values[letter] * new_Dict[letter]
        
print(scrabble_score)





#finding the most and less occurrent character

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d ={}

for char in placement:
    if char not in d:
        d[char] = 0
    d[char] = d[char] +1
    
keys = list(d.keys())

min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key
        
        
 
        
product = "iphone and android phones"
lett_d = {}

for letter in product:
    if letter not in lett_d:
        lett_d[letter] = 0
    lett_d[letter] = lett_d[letter] + 1
    
keys = list(lett_d.keys())

max_value = keys[0]

for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key
    
 
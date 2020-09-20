#Using split() and for loops:

addition_str = "2+5+10+20"
addition_str = addition_str.split("+")

sum_val = 0
for num in addition_str:
    sum_val = sum_val + int(num)
    
print("SUM:",sum_val,"\n")


#calculating the average temperature:
    
    
week_temps = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

week_temps = week_temps.split(",")
count = 0
total = 0

for temp in week_temps:
    total = total + float(temp)
    count = count + 1
    
avg_temp = total / count

print("\nAverage week temperature:",avg_temp)


#Write code to create a list of numbers from 0 to 67
#and assign that list to the variable nums.

nums = list(range(0,68))


#Write code to create a list of word lengths for the words in original_str
#using the accumulation pattern and assign the answer to a variable num_words_list.

original_str = "The quick brown rhino jumped over the extremely lazy fox"
List = original_str.split(" ")

num_words_list = []

for word in List:

    num_words_list.append(len(word))


#Create an empty string and assign it to the variable lett.
#Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").

lett = ""
for i in range(7):
    lett = lett + "b"
print(lett)



#Write a program that uses the turtle module and a for loop to draw something. 
#It doesn’t have to be complicated, but draw something different than we have done in the past.
#(Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. 
#Try setting .speed(10) for the turtle to draw fast

import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
Seb = turtle.Turtle()
Seb.color('red')
Seb.speed(10)

distance = 60
angle = 45
for i in range(8):
    Seb.forward(distance)
    Seb.right(angle)

turtle.done() 





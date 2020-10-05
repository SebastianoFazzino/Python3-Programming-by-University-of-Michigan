#List Comprehensions are concise ways to create lists from other lists. The general syntax is:
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]

things = [2, 5, 6, 11]
            
lst_comp = [value * 2 for value in things]

print(lst_comp)



print("*************************************")



#The for loop below produces a list of numbers greater than 10. 
#let's use list comprehension below the given code to accomplish the same thing and assign it the the variable lst2.

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [num for num in L if num > 10]



print("*************************************")



#we can combine map and filter operations by chaining them together

things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])




print("*************************************")




#let's filter all uneven numbers using a list comprehension inside a function
def keep_evens(nums):
               #in this case we have a filtration expression
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([2,5,33,45,14,48]))



print("*************************************")



#More Examples:
    
#Given the following dictionary, let's assign all the values of the key 'name' in any sub dictionary to the variable compri
#We'll use a list comprehension to complete the exercise
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

#we start descending a level in the dictionary
inner_list = tester['info']

compri = [d['name'] for d in inner_list]
print(compri)



print("*************************************")



#let's build a function that takes a list of strings as input and returns a list of strings which length is more than 3 letters
#we're going to use list comprehension in the first example
def longlength0(strings):
    return [string for string in strings if len(string) > 3]

#we're going to use map function in the second example
def longlength1(strings):
    return list(map(lambda string: len(string) > 3, strings))

#we're going to use filter function in the third example
def longlength2(strings):
    return list(filter(lambda string: len(string) > 3, strings ))
    

print(longlength0(['R','Ruby','Python','JavaScript','C#',"C++"]))
print(longlength1(['R','Ruby','Python','JavaScript','C#',"C++"]))
print(longlength2(['R','Ruby','Python','JavaScript','C#',"C++"]))
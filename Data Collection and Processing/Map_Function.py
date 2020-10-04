#map takes two arguments, a function and a sequence. 
#The function is the mapper that transforms items. It is automatically applied to each item in the sequence. 

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

#we can either pass a defined function or a lambda expression as argument for map
def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9, 14]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)



#more examples:
#let's say that given the following list of strings, we want to create a new list, called abbrevs_upper
#that contains the same strings in upper case, and to do so we need to use map

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]


#one way to do it is defining a function and passing it as map argument
def transformer(Str):
    return Str.upper()

abbrevs_upper = map(transformer, abbrevs)

#or passing a lambda expression as map argument
abbrevs_upper = map(lambda letter: letter.upper(), abbrevs)
print(abbrevs_upper)



#Using map, let's create a list assigned to the variable greeting_doubled that doubles each element in the list lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]


def double(lst):
    return lst * 2

#again, we can either define a function and pass it as map argument or use lambda expression
greeting_doubled = map(double, lst)
greeting_doubled = map(lambda l: l * 2, lst)

print(greeting_doubled)
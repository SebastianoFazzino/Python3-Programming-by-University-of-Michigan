#filter function takes two arguments, a function and a sequence. The function takes one item and return True if the item should. 
#It is automatically called for each item in the sequence. We don’t have to initialize an accumulator or iterate with a for loop.


#the following function takes a sequence of numbers as imput and using filter function, returns only even numbers
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(list(keep_evens([3, 4, 6, 7, 0, 1, 12])))




#more examples:
#given the following list of strings, let's say we want to assign every word with 'w' in it
#to the variable filter_testing

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = filter(lambda word: 'w' in word, lst_check)

print(list(filter_testing))



#given the following list, we want to assign words containing the letter 'o' to the variable lst2

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = filter(lambda word: 'o' in word, lst)

print(list(lst2))
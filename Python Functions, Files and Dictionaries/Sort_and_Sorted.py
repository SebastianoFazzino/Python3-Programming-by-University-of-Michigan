#The primary difference between the list sort() function and sorted() function is that the sort() will modify the list it is called on,
#meanwhile sorted() function will create a new list containing a sorted version of the list it is given.


#sort function:
    
lst1 = [1,7.-66,8,96]
lst2 = ['Apple','Watermelon','Banana','Cherry']

lst1.sort()
lst2.sort()

print('lst1 sorted:', lst1,
      '\nlst2 sorted:', lst2)

print(lst2.sort()) #returns none



#sorted function:
 
lst1 = [1,7.-66,8,96]
lst2 = ['Apple','Watermelon','Banana','Cherry']

lst3 = sorted(lst1)
print(lst1, lst3) #lst1 is unchanged

print(sorted(lst2))
print(lst2) #lst2 is unchanged


#we can apply the sorted() function to any sequence, not just to lists:
    
print(sorted("Orange"))
#the output will be: "['O', 'a', 'e', 'g', 'n', 'r']"
#Uppercase characters always come before lowercase characters



#if we use sort() on a string, we'll get an error message:
"Orange".sort()




#reverse order

print(sorted(lst2, reverse = True))
print(sorted("apple", reverse = True))



#Because the same list has two different names, a and b, we say that it is aliased. 
#Changes made with one alias affect the other. In the codelens example below, you can see 
#that a and b refer to the same list after executing the assignment statement b = a.

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)



#If we want to modify a list and also keep a copy of the original, 
#we need to be able to make a copy of the list itself, not just the reference. 
#This process is sometimes called cloning, to avoid the ambiguity of the word copy.
#The easiest way to clone a list is to use the slice operator.

a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)
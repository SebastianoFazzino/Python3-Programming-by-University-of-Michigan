
#Shallow Copies:
    
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]

#execunting this print statement, we can notice that original and 
#copied_version look identical
print(copied_version)

#when we check if copied_version is original, we get a False, 
#menaning that the two lists refer to two different objects
print(copied_version is original) 

#when we check if copied_version and original have the same content, we get a True
print(copied_version == original)

#let's append another element to the list original:
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")

#although we appended the list ['canines'] to original, 
#printing copied-version, we can see that the list ['canines'] has been appended to it as well
print(copied_version)



print("\n******************************************\n")


#Deep Copies:

#let's see how to make a copy of a list that is completely independent of the original
original = [['dogs', 'puppies'], ['cats', "kittens"]]

#in order to do it we create an empty list
copied_outer_list = []

#and we append the data in the list through iteration
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)

#if we now append an element to the original list, it won't affect the copied list,
#that's because we made a deep copy, completely independent of the original list
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)



print("\n******************************************\n")



#let's say we have a list which has more than two levels, like in this case,
#were we have the string 'canines' as element of the list

#Well, in this case we can use the 'copy module, which has a method called deepcopy that will take care of the operation for us

#we start importing the module copy:
import copy

original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]

#as mentioned, we use copy.deepcopy method, which takes a sequence as its value,
#and it produces a deep copy of the original list
deeply_copied_version = copy.deepcopy(original)


#if we append a value to an element in original, it'll affect the shallow copy too
original[0].append(["marsupials"])


#but if we append values to the top level list in original, this won't affect the shallow copy
original.append("Hi there")
original.append(2)
original.append(['animals'])

#printing the three different versions of original, we can see that they all differ from one other 
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version) 






#tuples packing     
cr7 = ("Cristiano","Ronaldo",1985,"Juventus FC","Football Player")
print(cr7[2]) #this returns the third element in the tuple




def circleInfo(r):
    '''Returns circumference, area of a cirlce'''
    
    circum = 2 * 3.14 * r
    area = 3.14 * r * r
    
    return (circum,area) #this will returns a tuple with two values

print(circleInfo(10))
    


#tuples unpacking
name, surname, birth_year, team, profession = cr7


a,b,c,d = 1,2,3,4   #we need the same number of values on both sides
                    #otherwise we'll get an error
                    
                    

def add(x, y):
    return x + y

z = (5, 4)
print(add(*z)) #the * causes the values in z to be unpacked





#unpacking into iterator variables:
    
    
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)



#enumerate built-in function takes a sequence as inpu and returns a sequence of tuples:

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])



#more examples
    
Dict = {'k1': 3, 'k2': 7, 'k3': 'same'}

for element in Dict.items():
    print("key: {}, value: {}".format(element[0],element[1]))    

#or more easily we can do:   
for key, value in Dict.items():
    print("key: {}, value: {}".format(key,value))
    
    
    
    
    

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names = []
p_number = []

for key, value in pokemon.items():
    p_names.append(key)
    p_number.append(value)
    

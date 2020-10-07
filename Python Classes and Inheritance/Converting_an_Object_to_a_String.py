class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    
#The __str__ method is responsible for returning a string representation as defined by the class creator. 
#In other words, you as the programmer, get to choose what a Point should look like when it gets printed. 
#In this case, we have decided that the string representation will include the values of x and y as well as some identifying text. It is required that the __str__ method create and return a string.
    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)

p = Point(7,6)
print(p)




#Exercise:
#Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: name, brand, and fiber. 
#When an instance of Cereal is printed, the user should see the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” To the variable name c1, assign an instance of Cereal 
#whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2. To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3. Practice printing both!

class Cereal():
    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber
        
    def __str__(self):
        return("{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,
                                                                                                self.brand,
                                                                                                self.fiber))
    
               
c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1,'\n',c2)
               
        
               
              
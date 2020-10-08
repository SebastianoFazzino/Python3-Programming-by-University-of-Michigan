#Given the class Point:

class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY
                
    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)

#let's say that we want to add the value of x or y in p1 to p2, to be able to do so, 
#we need to create another method in the class:
    
    def __add__(self, otherPoint):
        return(self.x + otherPoint.x,
               self.y + otherPoint.y)

#we can create more method, like substraction:
    
    def __sub__(self, otherPoint):
        return(self.x - otherPoint.x,
               self.y - otherPoint.y)
    
       
    
    
p1 = Point(15, 3)
p2 = Point(-3, 6)

#now, given p1 and p2, we can print the sum of their values:

print(p1 + p2)

#or the substraction:
    
print(p2 - p1)




#Methods can return any kind of value as their return value,
#but it's good to specify that they can also return other istances.

#Given the class Point:

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
                
    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)

    def __add__(self, otherPoint):
        return(self.x + otherPoint.x,
               self.y + otherPoint.y)
  
    def __sub__(self, otherPoint):
        return(self.x - otherPoint.x,
               self.y - otherPoint.y)
    
#let's say we want the class to accept two points and return a new point
#that is halfway between the two. We can proceed as follows:
    
    def halfway(self, target):
        midX = (self.x + target.x) / 2
        midY = (self.y + target.y) / 2
        return Point(midX, midY)
    

#now, given p1 and p2, we want to return a halfway point that we can call p3:

p1 = Point(15, 3)
p2 = Point(-3, 6)

p3 = p1.halfway(p2)
print(p3)
 
#now p3 is a new istance of Point class, so we can do:
    
print(p3.getX()) 
print(p3.getY())


 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
#the getX method simply returns the value of the instance variable x from the object self. 
#In other words, the implementation of the method is to go to the state of the object itself and get the value of x. Likewise, the getY method looks almost the same.   

#Let’s add another method, distanceFromOrigin, to see better how methods work. 
#This method will again not need any additional information to do its work, beyond the data stored in the instance variables. It will perform a more complex task.
    def distanceFromOrigin(self):
        return((self.x ** 2) + (self.y ** 2)) ** 0.5 

point1 = Point(2, 4)
print(point1.distanceFromOrigin())


#Exercise:
#Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. 
#Create an instance method called limbs that, when called, returns the total number of limbs the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. 
#Call the limbs method on the spider instance and save the result to the variable name spidlimbs.

class Animal():
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs
        
    def limbs(self):
        return (self.arms + self.legs)
    
    
spider = Animal(4,4)
spidlimbs = spider.limbs()

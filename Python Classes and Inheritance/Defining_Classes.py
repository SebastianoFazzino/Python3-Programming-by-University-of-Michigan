#In many cases, when we are trying to solve problems we need to create
#objects that are related to the problem we need to solve; we need to create our own classes


#to create a class, we use the keywork 'class', followed by the name of the class
class Point():
#Every class should have a method with the special name __init__. This initializer method is often referred to as the constructor
#The self parameter is automatically set to reference the newly created object that needs to be initialized.
#We can make our class constructor more generally usable by putting extra parameters into the __init__ method 
   def __init__(self, initX, initY):
       self.x = initX
       self.y = initY
       
   def getX(self):
       return self.x
       
        
#The self parameter (you could choose any other name, but nobody ever does!) is automatically set to reference the newly created object that needs to be initialized.       
point1 = Point(5, 10)
point2 = Point(3, 6)

print(point1.getX())



#exercise:
#Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. 
#Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.

class NumberSet():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
t = NumberSet(6, 10)
        
      

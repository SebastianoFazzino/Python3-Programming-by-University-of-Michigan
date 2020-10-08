#given a list of istances, we may want to sort them by some index

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price
        
        
FruitList = [
           Fruit('Cherry', 10),
           Fruit('Apple', 5),
           Fruit('Blueberry', 20)
           ]    

#now, the sort the fruit by price, we call the method sorted,
#and as key of the method we pass 'sort_priority' function defined in the class

for fruit in sorted(FruitList, key = Fruit.sort_priority):
    print(fruit.name, fruit.price)
    
    
#we can also use a lambda expression as follows:

for fruit in sorted(FruitList, key = lambda fruit: fruit.sort_priority()):
    print(fruit.name, fruit.price)
    
#more examples:
#let's say we want to sort the fruits in FruitListst by word length, from the longest to the shortest:
    
for fruit in sorted(FruitList, key = lambda fruit: len(fruit.name), reverse = True):
    print(fruit.name)
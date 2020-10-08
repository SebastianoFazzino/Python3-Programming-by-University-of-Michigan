#each instance of a class has its own namespace with its own instance variables. Two instances of the Point class each have their own instance variable x. Setting x in one instance doesn’t affect the other instance.
#A class can also have class variables. A class variable is set as part of the class definition.

#For example, consider the following version of the Point class which has a graph method that generates a string representing a little text-based graph with the Point plotted on the graph.

class Point:

    printed_rep = "+"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())


#When the interpreter sees an expression of the form <obj>.<varname>, it:
# 1)Checks if the object has an instance variable set. If so, it uses that value.

# 2)If it doesn’t find an instance variable, it checks whether the class has a class variable. If so it uses that value.

# 3)If it doesn’t find an instance or a class variable, it creates a runtime error 


#When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
# 1)Evaluates the expression on the right-hand side to yield some python object;

# 2)Sets the instance variable <varname> of <obj> to be bound to that python object. 
   #Note that an assignment statement of this form never sets the class variable; it only sets the instance variable.
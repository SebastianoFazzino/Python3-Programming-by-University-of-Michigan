#defining a simple function:
    
def hello():
    '''This function is used for greeting'''
    print('Hello, welcome!')
# we can now invoke the function:       
hello()





#using a function to draw with turtle:
    
import turtle

def drawSquare(t, distance):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(distance)
        t.left(90)


wn = turtle.Screen()      # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()    # create alex
drawSquare(alex, 50)      # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()




#function parameters:

def hello2(name):
    greeting = 'Hello {}, glad to meet you!'.format(name)
    print(greeting)
    
hello2('Seb')


your_name = str(input('Enter your name: '))
hello2(your_name)





def hello3(name, nr):
    greetings = 'Hey {}, welcome!'.format(name)
    print(greetings * nr)
    
your_name = str(input('enter your name: '))
a_number = int(input('enter a number between 1 and 9: '))

hello3(your_name, a_number)
    
    
    
    
#functions and if statement:
    
def hello4(name1, name2):
    if len(name1) > len(name2):
        print(name1)
    else:
        print(name2)

hello4('Julia', 'Ron')






    
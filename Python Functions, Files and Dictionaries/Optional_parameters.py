#Optional parameters

def Funct(a, List =[]):
    List.append(a)
    return List
    
print(Funct(3))
print(Funct(4))
print(Funct(11))
print(Funct(5, ['Hello']))



#Keyword parameters

initial = 7

def f(x,y=3,z=initial):
    print("x, y, z, are: " + str(x),',', str(y),',', str(z))
    
f(2,6,8)
f(2,z=11)
f(x=1,y=(1+initial),z=2)



#if we change the value of 'initial' after the function has been invoked, z value won't change:
    
initial = 7
def f(x, y = 3, z = initial):
    print ("x, y, z are:", x, y, z)
    
initial = 0 #in this case changing this parameter value won't have any effect of the function's parameters
f(2)

#but if we pass 'initial' as a function's parameter, the parameter's value will change accordingly:
    
f(x=1,y=(1+initial),z=2)





#keyword parameters with .format

names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
    
    

#We can use the .format method to insert the same value into a string multiple times.

names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))
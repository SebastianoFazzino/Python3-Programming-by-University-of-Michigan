#When to use a lambda expression and when to use a named function:
#if the lambda expression is short and simple, so that it's pretty easy to understand what it's doing, 
#use the lambda expression, and as soon as it gets too complex, refer to a name function instead.

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

#this is an example of an outher limit simple enough lambda expression:
print(sorted(states, key=lambda state: len(states[state][0])))



#Suppose that we wanted to take a different property. 
#For each state, we want to find the number of cities in its city list that begin with the letter S. We want to sort in that order.

#In this case it's easier to use a named function:
    
def s_cities_count(cities_list):
    ''' Return a count of how many cities begin with 'S' '''
    count = 0
    for city in cities_list:
        if city[0] == 'S':
            count += 1
    return count

print(sorted(states, key = lambda state: s_cities_count(states[state])))


#Alternatively we can call the function s_cities_count inside another function

def s_cities_count_for_state(state):
    cities_list = states[state]
    return s_cities_count(cities_list)

print(sorted(states, key = s_cities_count_for_state))


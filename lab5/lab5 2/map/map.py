#Name: Tarini Srikanth
#Instructor: Turner
#Project: Lab 5- Map

import math
def square_all(t):
    #adds all the sqaures to a new array, used while loop
    x=0
    a=[]
    while(x<len(t)):
        a.append(t[x]**2)
        x=x+1
    return a

def add_n_all(t,a):
    #adds al to the new array, a+ t, used list comprehension
    n=[i+a for i in t]
    return n


def distance_all(t):
    #adds to new array the distance (0,1,2), based on the input to the
    #origin (0)
    #input list: [[1,2],[2,3],[3,4]]
    a=[]
    distanceOfValue=0
    for i in t:
        value1 = (i[0]-0)**2
        value2= (i[1]-0)**2
        distanceOfValue = round(math.sqrt(value1+value2),1)
        a.append(distanceOfValue)
    return a

        
        
        
    
    
    

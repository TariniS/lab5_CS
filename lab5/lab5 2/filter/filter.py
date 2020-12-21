#Name:Tarini Srikanth
#Instructor: Turner
#Project: Lab 5- Filter

def are_positive(t):
    #only adds if the value is postive, using list comprehension
    a=[i for i in t if i>0]
    return a
def are_greater_than(t,n):
    #only adds if value is greater than n, using while loop
    x=0
    a=[]
    while(x<len(t)):
        if(t[x]>n):
            a.append(t[x])
        x=x+1
    return a
def are_in_first_quadrant(t):
    #only adds if value is in the first quadrant. Used for loop.
    #assumed that input would be an array of arrays, with length
    #2 for the inner array (x,y)
    #[(1,2),(2,3),(-2,4)]
    x=0
    a=[]
    for i in t:
        if((i[0]>=0)and(i[1]>=0)):
            a.append(i)
    return a
            
        
            
           
    
    
    

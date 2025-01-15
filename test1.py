#Unserstanding the concept of the function with multiple functions

def add(a, b):
    return a+b  
        
a = 5
b = 10

print(add(add(a,b),add(a,b)))
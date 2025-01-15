'''
square 
add
multiplication
'''

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def squ(a):
    return a*a


a = int(input("Enter the Number a ="))
b = int(input("Enter the Number b ="))

print(add(add(squ(a),squ(b)),mul(mul(a,b),2)))
'''
Maths Formula
'''

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def squ(a):
    return a*a

def sub(a,b):
    return a-b


a = int(input("Enter the Number a ="))
b = int(input("Enter the Number b ="))

print(mul(add(add(squ(a),squ(b)),mul(a,b)),sub(a,b)))

#Rotate a list to the left by n positions.

# Input: lst = [1, 2, 3, 4, 5], n = 2
# Output: [3, 4, 5, 1, 2]


def rotate_right(a, c):

    if not a:  
        return a
    c %= len(a) 
    return a[-c:] + a[:-c]



a = []

b = int(input("How many numbers would you like to enter? "))

for _ in range(b):
    temp = int(input("Enter a number: "))
    a.append(temp)

c = int(input("Enter the number of positions to rotate to the right: "))
rotated = rotate_right(a, c)

print("The List is",a)
print("The Rotated List is",rotated)


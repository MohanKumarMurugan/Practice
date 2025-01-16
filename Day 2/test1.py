#Rotate a List

# Input: lst = [1, 2, 3, 4, 5], n = 2
# Output: [3, 4, 5, 1, 2]

a = []

b = int(input("How many numbers would you like to enter? "))

for _ in range(b):
    temp = int(input("Enter a number: "))
    a.append(temp)


print("The List is",a)


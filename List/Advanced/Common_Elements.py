# Find the common elements between two lists.

list1 = []

a = int(input("No of element to be insert in the list : "))

for i in range(a):
    temp = int(input("Enter the Values : "))
    list1.append(temp)

list2 = []

b = int(input("No of element to be insert in the list : "))

for i in range(b):
    temp1 = int(input("Enter the Values : "))
    list2.append(temp1)

common_values = [item for item in list1 if item in list2]

print(common_values)
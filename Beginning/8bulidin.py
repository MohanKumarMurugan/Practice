# Sort a list of integers in ascending order.

a = []

numbers = int(input("Enter no of values : "))
for i in range(numbers):
    values = int(input("values need to add in the list : "))
    a.append(values)

a.sort()

print("The list is  : ",a)
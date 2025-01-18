# Append an element to a list and print the updated list.

a = []

numbers = int(input("Enter no of Elements : "))
for i in range(numbers):
    values = input("values need to add in the list : ")
    a.append(values)

print("The List Created : ",a)

appended = input("Enter the value to append : ")

a.append(appended)

print("Updated List : ",a)
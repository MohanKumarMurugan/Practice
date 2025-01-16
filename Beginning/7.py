# Reverse a list and print it.

a = []

numbers = int(input("Enter no of elements : "))
for i in range(numbers):
    values = input("values need to add in the list : ")
    a.append(values)
print("The list is  : ",a)

reversed = a[::-1]

print(reversed)
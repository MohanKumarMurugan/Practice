# Remove the third element from a list.
# Find the length of a given list.
a = []

numbers = (int(input("Enter no of values : ")))
for i in range(numbers):
    values = input("values need to add in the list : ")
    a.append(values)

print("The List Created : ",a)
print(len(a))

a.pop(2)

print("The Updated List Created : ",a)
print(len(a))
# Create a list comprehension that squares each element in a given list.

list1 = []

a = int(input("No of Element in the List 1 : "))
for i in range (a):
    values1 = int(input("values need to add in the list: "))
    list1.append(values1)

squared_numbers = [x**2 for x in list1]

print(squared_numbers)
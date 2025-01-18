# Remove duplicates from a list.

list1 = []

a = int(input("No of Element in the List : "))
for i in range (a):
    values1 = int(input("values need to add in the list : "))
    list1.append(values1)

unique_numbers = list(set(list1))

print("Unique numbers:", unique_numbers)
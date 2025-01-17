# Merge two lists into a single list.

list1 = []

a = int(input("No of Element in the List 1 : "))
for i in range (a):
    values1 = input("values need to add in the list 1 : ")
    list1.append(values1)

list2 = []

b = int(input("No of Element in the List 2 : "))
for j in range (b):
    values2 = input("values need to add in the list 2 : ")
    list2.append(values2)

updated_list = list1 + list2

print(updated_list)
# Check if a list is empty.

list1 = []

a = int(input("No of Element in the List 1 : "))
for i in range (a):
    values1 = int(input("values need to add in the list: "))
    list1.append(values1)

if len(list1) == 0:
    print("The list is empty")

else:
    print("The list Contains data")
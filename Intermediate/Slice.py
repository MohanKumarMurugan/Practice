# Slice a list to get the first 5 elements.

list1 = []

a = int(input("No of Element in the List 1 : "))
for i in range (a):
    values1 = input("values need to add in the list: ")
    list1.append(values1)

if (len(list1) >= 4):
    print(list1[:5])
else:
    print("Invalid Data")
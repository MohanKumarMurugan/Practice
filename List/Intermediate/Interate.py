# Iterate over a list and print each element.

list1 = []

a = int(input("No of Element in the List : "))
for i in range (a):
    values1 = input("values need to add in the list : ")
    list1.append(values1)

for element in list1:
    print(element)
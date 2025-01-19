# Create a new list that contains only the even numbers from an existing list.

list1 = []

a = int(input("No of Element in the List 1 : "))
for i in range (a):
    values1 = int(input("values need to add in the list: "))
    list1.append(values1)

list2 = []

for i in range (len(list1)):
    if list1 [i] % 2 == 0:
        list2.append(list1[i])
    
print(list2)

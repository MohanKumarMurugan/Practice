# Split a list into two halves.

list1 = []

a = int(input("No of element to be insert in the list : "))

for i in range(a):
    temp = int(input("Enter the Values : "))
    list1.append(temp)

list2 = []
list3 = []

mid = len(list1)//2

list2 = list1[:mid]
list3 = list1[mid:]

print("The first Half is : ", list2)
print("The second Half is : ", list3)
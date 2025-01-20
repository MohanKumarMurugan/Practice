# Find the second-largest number in a list.

def sorting(list1):
    for k in range(1,len(list1)):
        j = k
        while j > 0 and list1[j - 1] > list1[j]:
            list1[j - 1], list1[j] = list1[j], list1[j - 1]
            j -= 1
    return list1


list1 = []

a = int(input("No of element to be insert in the list : "))

for i in range(a):
    temp = int(input("Enter the Values : "))
    list1.append(temp)

sorted_list = sorting(list1) 
print("Sorted List:", sorted_list)

if len(list1) > 2:
    print(list1[-2])
else:
    print("Doesn't Contain that much of Data")
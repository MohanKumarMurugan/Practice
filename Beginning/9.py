# Find the index of a specific element in a list.

a = []

numbers = int(input("Enter no of values : "))
for i in range(numbers):
    values = input("values need to add in the list : ")
    a.append(values)

j = (input("Enter the Data To Check the index : "))

if j in a:
    indev_value = a.index(j)
    print("The Data ",j ,"Exist in the index : ", indev_value)

else: 
    print("The Data ",j ,"is not exist in the List")

# Check if a given element exists in a list.

a = []

numbers = int(input("Enter no of values : "))
for i in range(numbers):
    values = input("values need to add in the list : ")
    a.append(values)

j = (input("Enter the Data To Check : "))

if j in a:
    print("The Data ",j ,"Exist in the List")

else: 
    print("The Data ",j ,"is not exist in the List")

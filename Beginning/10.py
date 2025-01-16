# Count the occurrences of a specific value in a list.

# Enter the number of elements: 5  
# Enter the elements: 1 2 2 3 2  
# Enter the value to count: 2

a = []

numbers = int(input("Enter no of elements : "))
for i in range(numbers):
    values = int(input("values need to add in the list : "))
    a.append(values)

value = int(input("Enter the value to count: "))

count = 0
for item in a:
    if item == value:
        count += 1

print("The value ", value ,"occurs " ,count ,"times in the list.")

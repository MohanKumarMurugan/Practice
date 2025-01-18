# Replace all occurrences of a specific value in a list with another value.

list1 = []

a = int(input("No of Element in the List 1 : "))
for i in range (a):
    values1 = int(input("values need to add in the list: "))
    list1.append(values1)

old_value = int(input("Enter the value to replace: "))
new_value = int(input("Enter the new value: "))

list1 = [new_value if x == old_value else x for x in list1]

print("Updated list:", list1)
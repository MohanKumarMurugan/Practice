# Find the maximum and minimum values in a list.

list1 = []

a = int(input("No of Element in the List : "))
for i in range (a):
    values1 = int(input("values need to add in the list : "))
    list1.append(values1)

maxi = max(list1)
mini = min(list1)

print("Maximum Number is ",maxi , " And Minimum Value is ",mini)
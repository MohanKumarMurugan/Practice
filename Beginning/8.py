# Sort a list of integers in ascending order.

def sorting(a):
    for k in range(1, len(a)):
        j = k
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
    return a

a = []

numbers = int(input("Enter no of elements : "))
for i in range(numbers):
    values = int(input("values need to add in the list : "))
    a.append(values)

print("Sorted List:", sorting(a))

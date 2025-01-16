# Access and print the first, middle, and last elements of a list.

a = []

b = int(input("Enter The beginning : "))
c = int(input("Ending : "))

for i in range (b,c+1):
    a.append(i)

middle = len(a)//2
d = a[middle]


print(a[0]+a[-1]+d)
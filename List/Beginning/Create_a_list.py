# Create a list of 10 numbers and print it.

a = []

b = int(input("Enter The beginning : "))
c = int(input("Ending : "))

for i in range (b,c+1):
    a.append(i)

print(a)
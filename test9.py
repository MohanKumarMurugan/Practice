a = []

for i in range(1,11,2):

    a.append(i)

print(a)


def add(a):
    b=0
    for j in a:
        
        b=b+j
    return b


print(add(a))
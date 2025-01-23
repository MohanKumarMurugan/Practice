# Write a program to check if a list is sorted.

def is_sorted(a):
      for i in range(len(a) - 1):

        if a[i] > a[i + 1]:
            return False
        return True



list1 = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

print(is_sorted(list1))

#Palindrome Number

def is_palindrome(a):
    temp = a
    rev = 0

    while a > 0:
        dig = a % 10
        rev = rev * 10 + dig
        a //= 10

    return temp == rev

a = int(input("Enter a value: "))

if is_palindrome(a):
    print("It is palindrome number!")
else:
    print("It is not a palindrome number!")

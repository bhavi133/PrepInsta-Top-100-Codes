Link : https://prepinsta.com/python-program/find-a-number-is-palindrome-or-not/

def palindrome(num):
    n = num
    result = 0
    while num > 0:
        remainder = num % 10
        result = (result * 10) + remainder
        num = num // 10
    if num == result:
        print(f"{n} is a palindrome number")
    else:
        print(f"{n} is not a palindrome number")

num = int(input("Input a number : "))
palindrome(num)

Link : https://prepinsta.com/python-program/to-find-the-reverse-of-a-given-number/

def reverse(num):
    result = 0
    while num > 0:
        remainder = num % 10
        result = (result * 10) + remainder
        num = num // 10
    return result

num = int(input("Input a number : "))
print(reverse(num))

Link : https://prepinsta.com/python-program/to-find-a-number-is-armstrong-or-not/

num = int(input("Input a number : "))
sum = 0
n = num
while n > 0:
    digit = n % 10
    sum += digit ** 3
    n = n // 10

if num == sum:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")

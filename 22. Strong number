Link : https://prepinsta.com/python-program/to-check-whether-a-number-is-a-strong-number-or-not/

def factorial(n):
    if n <= 1:
        return 1
    else:
        fact = n * factorial(n - 1)
    return fact

n = int(input("Input a number : "))
sum = 0
for i in str(n):
    sum = sum + factorial(int(i))

if sum == n:
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a strong number")

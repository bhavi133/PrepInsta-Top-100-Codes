Link : https://prepinsta.com/python-program/to-check-abundant-number/

n = int(input("Input a number : "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum > n:
    print(f"{n} is an abundant number")
else:
    print(f"{n} is not an abundant number")

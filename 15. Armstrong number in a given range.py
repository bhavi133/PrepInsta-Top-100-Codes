Link : https://prepinsta.com/python-program/armstrong-numbers-between-two-intervals/

r1 = int(input("Input upper limit : "))
r2 = int(input("Input lower limit : "))

for i in range(r1, r2):
    n = i
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit ** 3
        n = n // 10

    if sum == i:
        print(i)

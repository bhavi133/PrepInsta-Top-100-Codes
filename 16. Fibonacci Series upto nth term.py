Link : https://prepinsta.com/python-program/find-fibonacci-series-up-to-n/

def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c, end=" ")

n = int(input("Input a number : "))
fibonacci(n)

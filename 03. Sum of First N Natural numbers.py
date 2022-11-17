Link : https://prepinsta.com/python-program/find-the-sum-of-first-n-natural-numbers/

def sum(n):
    return int(n*(n+1)/2)

n = int(input("Input a number : "))
print(sum(n))

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

n = int(input("Input a number : "))
print(sum(n))

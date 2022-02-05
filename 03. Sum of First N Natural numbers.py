Link : https://prepinsta.com/python-program/find-the-sum-of-first-n-natural-numbers/

n = int(input("Input a number : "))
print(int(n*(n+1)/2))

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

n = int(input("Input a number : "))
print(sum(n))

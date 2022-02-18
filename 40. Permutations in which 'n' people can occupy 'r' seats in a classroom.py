Link : https://prepinsta.com/python-program/permutations-in-which-n-people-can-occupy-r-seats-in-a-classroom/

from math import factorial

n = int(input("Input the number of students : "))
r = int(input("Input the number of seats : "))
nume = factorial(n)
deno = factorial(n-r)
result = nume // deno
print("Total number of ways : ", result)

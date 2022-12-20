Link : https://prepinsta.com/python-program/to-find-a-number-is-armstrong-or-not/

Code 1 :
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

Code 2 :
    
def armstrongNumber(n):
    l1 = list(map(int, str(n)))
    y = len(l1)
    l2 = list(map(lambda x:x**y, l1))
    if(sum(l2) == n):
        return 'Yes'
    else:
        return 'No'

print(armstrongNumber(1634))

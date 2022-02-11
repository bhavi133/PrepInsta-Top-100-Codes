Link : https://prepinsta.com/python-program/to-check-whether-two-numbers-are-friendly-pair/

x = int(input("Input a number : "))
y = int(input("Input a number : "))
sum1 = 0
sum2 = 0
for i in range(1, (x//2)+1):
    if x % i == 0:
        sum1 = sum1 + i

for i in range(1, (y//2)+1):
    if y % i == 0:
        sum2 = sum2 + i

if sum1 == y and sum2 == x:
    print("Friendly pair")
else:
    print("Not a friendly pair")

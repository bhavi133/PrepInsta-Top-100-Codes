Link : https://prepinsta.com/python-sum-of-numbers-in-a-given-range-in-python/

n1 = int(input("Input upper limit : "))
n2 = int(input("Input lower limit : "))
sum = 0
for i in range(n1, n2+1):
    sum += i
print(sum)

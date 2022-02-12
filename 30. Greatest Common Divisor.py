Link : https://prepinsta.com/python-program/find-gcd-of-two-numbers/

def greatest_common_divisor(n1, n2):
    if n1 > n2:
        small = n2
    else:
        small = n1
    for i in range(1, small+1):
        if (n1 % i == 0) and (n2 % i == 0):
            gcd = i
    return gcd

n1 = int(input("Input first number : "))
n2 = int(input("Input second number : "))
print(f"GCD of {n1} and {n2} is : ", greatest_common_divisor(n1, n2))

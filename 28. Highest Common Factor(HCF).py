Link : https://prepinsta.com/python-program/find-hcf-of-two-numbers/

def highest_common_factor(n1, n2):
    hcf = 1
    for i in range(1, min(n1, n2)):
        if (n1 % i == 0) and (n2 % i == 0):
            hcf = i
    return hcf

n1 = int(input("Input first number : "))
n2 = int(input("Input second number : "))
print(f"HCF of {n1} and {n2} is : ", highest_common_factor(n1, n2))

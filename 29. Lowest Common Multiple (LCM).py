Link : https://prepinsta.com/python-program/find-lcm-of-two-numbers/

def lowest_common_multiple(n1, n2):
    hcf = 1
    for i in range(1, max(n1, n2)):
        if (n1 % i == 0) and (n2 % i == 0):
            hcf = i
    lcm = (n1 * n2) // hcf
    return lcm

n1 = int(input("Input first number : "))
n2 = int(input("Input second number : "))
print(f"LCM of {n1} and {n2} is : ", lowest_common_multiple(n1, n2))

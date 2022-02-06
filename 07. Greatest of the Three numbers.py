Link : https://prepinsta.com/python-program/find-the-largest-number-among-three-numbers/

def max_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3

num1 = int(input("Input first number : "))
num2 = int(input("Input second number : "))
num3 = int(input("Input third number : "))
print(max_of_three(num1, num2, num3))

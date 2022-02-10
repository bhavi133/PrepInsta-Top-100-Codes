Link : https://prepinsta.com/python-program/to-check-automorphic-number/

number = int(input("Input a number : "))
length = len(str(number))
square = number ** 2
last_digits = square % pow(10, length)

if last_digits == number:
    print(f"{number} is an automorphic number")
else:
    print(f"{number} is not an automorphic number")

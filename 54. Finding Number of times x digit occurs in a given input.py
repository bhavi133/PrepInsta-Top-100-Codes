Link : https://prepinsta.com/python-program/count-number-of-times-x-digit-occurs-in-each-and-every-number-from-0-to-n/

number = int(input("Input a number : "))
digit = int(input("Input a digit : "))
ctr = 0
for i in str(number):
    if i == str(digit):
        ctr += 1
print(ctr)

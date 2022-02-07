Link : https://prepinsta.com/python-program/find-sum-of-digits-of-a-number/

def sum_of_digits(num):
    sum = 0
    for i in num:
        sum = sum + int(i)
    return sum

num = input("Input a number : ")
print(sum_of_digits(num))

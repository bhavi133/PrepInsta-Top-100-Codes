Link : https://prepinsta.com/wp-content/uploads/2020/12/Harshad-number.webp

n = int(input("Input a number : "))
result = 0
for i in str(n):
    result = result + int(i)

if n % result == 0:
    print(f"{n} is a harshad number")
else:
    print(f"{n} is not a harshad number")

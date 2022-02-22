Link : https://prepinsta.com/python-program/can-a-number-be-expressed-as-a-sum-of-two-prime-numbers/

num = int(input('Input a number : '))
arr = []
for i in range(2, num):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        arr.append(i)

flag = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] + arr[j] == num):
            flag = 1
            print(str(arr[i]) + " and " + str(arr[j]) + ' are prime numbers when added gives ' + str(num))
            break
if(flag == 0):
    print('No Prime numbers can give sum of ' + str(num))

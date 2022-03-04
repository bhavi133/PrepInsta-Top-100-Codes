Link : https://prepinsta.com/python-program/finding-repeating-elements-in-an-array/

def duplicates(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k, v in dic.items():
        if v > 1:
            print(k, end=" ")

arr = [10, 20, 40, 30, 50, 20, 10, 20]
duplicates(arr)


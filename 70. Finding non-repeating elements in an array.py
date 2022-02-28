Link : https://prepinsta.com/python-program/find-non-repeating-elements-in-an-array/

def unique(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k, v in dic.items():
        if v <= 1:
            print(k, end=" ")

arr = [10, 20, 70, 90, 80, 20, 10, 20]
unique(arr)

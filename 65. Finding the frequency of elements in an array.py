Link : https://prepinsta.com/python-program/finding-the-frequency-of-elements-in-an-array-using-python/

def frequency(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k, v in dic.items():
        print(k, v)

arr = [10, 30, 10, 20, 10, 20, 30, 10] 
frequency(arr)

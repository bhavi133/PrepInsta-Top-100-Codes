Link : https://prepinsta.com/python-program/find-the-smallest-and-largest-element-in-an-array-using-python/

def smallest_largest(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i <= min:
            min = i
        if i > max:
            max = i
    print(min)
    print(max)

arr = [10, 89, 9, 56, 4, 80, 8]
smallest_largest(arr)

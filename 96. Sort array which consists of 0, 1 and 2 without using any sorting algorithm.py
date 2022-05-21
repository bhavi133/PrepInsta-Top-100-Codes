Link : https://prepinsta.com/python-program/sort-array-which-consists-of-0-1-and-2-without-using-any-sorting-algo/

def sort(arr):
    zeros = [i for i in arr if i == 0]
    ones = [i for i in arr if i == 1]
    twos = [i for i in arr if i == 2]
    return zeros + ones + twos

arr = [1, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1]
print("Before sorting : ", arr)
print("After sorting : ", sort(arr))

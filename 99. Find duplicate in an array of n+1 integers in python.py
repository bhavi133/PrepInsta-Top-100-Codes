Link : https://prepinsta.com/python-program/find-duplicate-in-an-array-of-n1-integers/

def duplicate(arr):
    nums = []
    for i in arr:
        if arr.count(i) > 1 and i not in nums:
            nums.append(i)
    for i in sorted(nums):
        print(i, end=" ")

arr = [-1, 8, 1, 8, -1, 5, 1, -3]
duplicate(arr)

Link : https://prepinsta.com/python-program/removing-duplicates-elements-from-an-array/

def remove_duplicates(arr):
    for i in arr:
        if arr.count(i) <= 1:
            print(i, end=" ")

arr = [10, 20, 70, 90, 80, 20, 10, 20]
remove_duplicates(arr)

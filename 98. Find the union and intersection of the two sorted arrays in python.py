Link : https://prepinsta.com/python-program/find-the-union-and-intersection-of-the-two-sorted-arrays/

def union(arr1, arr2):
    new_arr = []
    for i in arr1:
        if i not in new_arr:
            new_arr.append(i)
    for i in arr2:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr
    
def intersection(arr1, arr2):
    new_arr = []
    for i in arr1:
        if i in arr2:
            new_arr.append(i)
    return new_arr

arr1 = [1, 2, 3, 4]
arr2 = [4, 5, 6, 7]
print("Union of two arrays : ", union(arr1, arr2))
print("Intersection of two arrays : ", intersection(arr1, arr2))

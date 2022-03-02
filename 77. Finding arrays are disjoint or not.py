Link : https://prepinsta.com/python-program/find-whether-arrays-are-disjoint-or-not/

def is_disjoint(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if (arr1[i] == arr2[j]):
                return False
    return True

arr1 = [10, 5, 3, 4, 6]
arr2 = [8, 7, 9, 3]
print(arr1)
print(arr2)
print(is_disjoint(arr1, arr2))

Link : https://prepinsta.com/python-program/find-common-elements-in-3-sorted-arrays/

def find_common_element(array1, array2, array3):
    for i in array1:
        if i in array2 and i in array3:
            print(i)

array1 = [1, 2, 3]
array2 = [2, 3, 4]
array3 = [3, 4, 5]
find_common_element(array1, array2, array3)

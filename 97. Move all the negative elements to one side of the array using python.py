Link : https://prepinsta.com/python-program/move-all-the-negative-elements-to-one-side-of-the-array/

def find(arr):
    negative = [i for i in arr if i < 0]
    positive = [i for i in arr if i >= 0]
    return negative + positive

arr = [0, 1, 3, -1, 4, -3, -5, -6, 3, 7]
print("Original array : ", arr)
print("After moving all the negative elements to one side of the array : ", find(arr))

def find(arr):
    negative = [i for i in arr if i < 0]
    positive = [i for i in arr if i >= 0]
    negative.sort()
    positive.sort()
    return negative + positive

arr = [0, 1, 3, -1, 4, -3, -5, -6, 3, 7]
print("Original array : ", arr)
print("After moving all the negative elements to one side of the array : ", find(arr))

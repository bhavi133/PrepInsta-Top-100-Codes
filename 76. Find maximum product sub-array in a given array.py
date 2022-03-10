Link : https://prepinsta.com/python-program/find-maximum-product-sub-array-in-a-given-array/

def maximum_product(arr, n):
    result = arr[0]
    for i in range(n):
        mul = arr[i]
        for j in range(i+1, n):
            result = max(result, mul)
            mul *= arr[j]
        result = max(result, mul)
    return result

arr = [1, -2, -3, 0, 7, -8, -2]
print(maximum_product(arr, len(arr)))

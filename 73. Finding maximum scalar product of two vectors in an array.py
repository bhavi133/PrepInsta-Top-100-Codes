Link : https://prepinsta.com/python-program/to-find-maximum-scalar-product-of-two-vectors-in-an-array/#:~:text=Dot%20product%20is%20an%20algebraic

arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]
arr1.sort()
arr2.sort()
product = 0
for i in range(len(arr1)):
    product += arr1[i] * arr2[i]
print(product)

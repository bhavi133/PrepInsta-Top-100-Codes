Link : https://prepinsta.com/python-program/finding-minimum-scalar-product-of-two-vectors/

arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]
arr1.sort()
arr2.sort(reverse=True)
product = 0
for i in range(len(arr1)):
    product += arr1[i] * arr2[i]
print(product)

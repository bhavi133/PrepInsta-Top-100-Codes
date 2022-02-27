Link : https://prepinsta.com/python-program/calculate-the-sum-of-elements-in-an-array-using-python/

def sum_of_elements(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = [10, 89, 9, 56, 4, 80, 8]
print(sum_of_elements(arr))   

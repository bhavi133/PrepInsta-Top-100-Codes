Link : https://prepinsta.com/python-program/counting-the-number-of-even-and-odd-elements-in-an-array/

def even_and_odd(arr):
    even_count = 0
    odd_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

arr = [10, 89, 9, 56, 4, 80, 8, -1]
result = even_and_odd(arr)
print("Count of even numbers is an array : ", result[0])
print("Count of odd numbers is an array : ", result[1])

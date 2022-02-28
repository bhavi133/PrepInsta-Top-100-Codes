63. Sort first half in ascending order and second half in descending order

Link : https://prepinsta.com/python-program/program-to-sort-first-half-in-ascending-order-and-second-half-in-descending-order-in-an-array/

arr = [10, 89, 9, 56, 4, 80, 8, -1]
arr.sort()
print(arr[:((len(arr))//2)+1] + arr[:(len(arr)//2):-1])


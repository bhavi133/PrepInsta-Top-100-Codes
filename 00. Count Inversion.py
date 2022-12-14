Link : https://prepinsta.com/python-program/counting-inversion/

def inversion(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                count += 1
    return count


array = [6, 3, 5, 2, 7]
print("There are", inversion(array), "possible inversion")

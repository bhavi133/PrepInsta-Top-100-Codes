Link : https://prepinsta.com/python-program/for-counting-distinct-elements-in-an-array/

def count_distinct(arr):
    lst = []
    for i in arr:
        if i not in lst:
            lst.append(i)
    return len(lst)
    
arr = [10, 20, 40, 30, 50, 20, 10, 20]
print(count_distinct(arr))

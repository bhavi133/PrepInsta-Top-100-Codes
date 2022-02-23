Link : https://prepinsta.com/python-program/to-find-prime-numbers-between-1-too-100/

def prime():
    for i in range(2, 101):
        count = 0
        for j in range(2, i//2 + 1):
            if i % j == 0:
                count += 1
                break
        if count == 0 and i != 1:
            print(i, end=" ")

prime()

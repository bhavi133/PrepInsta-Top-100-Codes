Link : https://prepinsta.com/python-program/calculating-the-length-of-string-without-using-length-function/

def length(str):
    ctr = 0
    for i in str:
        ctr += 1
    return ctr

str = 'PrepInsta'
print(length(str))

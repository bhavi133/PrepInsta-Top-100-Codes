Link : https://prepinsta.com/python-program/to-replace-all-0s-with-1-in-a-given-integer/

num = int(input("Input a number : "))
str1 = str(num)
lst = []
for i in str1:
    if i == '0':
        lst.append('1')
    else:
        lst.append(i)

string = ""
for i in lst:
    string = string + i
print(int(string))

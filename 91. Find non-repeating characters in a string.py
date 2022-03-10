Link : https://prepinsta.com/python-program/find-non-repeating-characters-in-a-string/

string = "prepinsta"
str = ""
for i in string:
    if string.count(i) > 1:
        pass
    else:
        str += i
print(str)

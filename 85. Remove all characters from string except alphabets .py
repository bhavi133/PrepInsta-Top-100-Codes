Link : https://prepinsta.com/python-program/remove-all-character-from-string-except-alphabets/

string = "#Justice!For@Jessica123"
str = ""
for i in string:
    if (ord(i) >= 65 and ord(i) < 90) or (ord(i) >= 97 and ord(i) < 122):
        str += i
print(str)

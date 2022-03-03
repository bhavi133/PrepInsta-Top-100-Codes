Link : https://prepinsta.com/python-program/reverse-a-string/

def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str

string = "PrepInsta"
print(reverse(string))

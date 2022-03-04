Link : https://prepinsta.com/python-program/toggle-each-character-in-a-string/

def toggle_string(string):
    str = ""
    for i in string:
        if i.isupper():
            i = i.lower()
            str = str + i
        else:
            i = i.upper()
            str = str + i
    return str
    
str = 'PrepInsta'
print(toggle_string(str))

Link : https://prepinsta.com/python-program/to-remove-brackets-from-an-algebraic-expression/

def remove_brackets(expression):
    str = ""
    for i in expression:
        if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
            pass
        else:    
            str += i
    return str

expression = '(a-b)+[c*d]+{e/f}'
print(remove_brackets(expression))

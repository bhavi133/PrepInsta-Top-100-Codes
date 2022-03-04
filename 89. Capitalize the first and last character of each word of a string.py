Link : https://prepinsta.com/python-program/capitalize-the-first-and-last-letter-of-each-word-of-a-string/

def capitalize(string):
    return string[0].upper() + string[1:-1] + string[-1].upper() 

string = "prepinsta"
print(capitalize(string))

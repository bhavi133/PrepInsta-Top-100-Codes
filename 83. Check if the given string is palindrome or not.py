Link : https://prepinsta.com/python-program/to-check-whether-a-string-is-a-palindrome-or-not/

def is_palindrome(string):
    string = string.lower()
    if string == string[::-1]:
        print(f"{string} is a palindrome string")
    else:
        print(f"{string} is not a palindrome string")

string = 'malayalam'
is_palindrome(string)

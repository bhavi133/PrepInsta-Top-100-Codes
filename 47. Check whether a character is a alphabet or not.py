Link : https://prepinsta.com/python-program/to-check-whether-a-character-is-alphabet-or-not/

char = input("Input a character : ")
x = ord(char)
if (65 <= x <= 90 or 97 <= x <= 122):
    print("Character is a alphabet")
else:
    print("Character is not a alphabet")

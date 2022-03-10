Link : https://prepinsta.com/python-program/check-if-two-strings-are-anagram-or-not/

string1 = "Listen"
string2 = "Silent"
string1 = sorted(string1.lower())
string2 = sorted(string2.lower())
if string1 == string2:
    print("Strings are anagram")
else:
    print("Strings are not anagram")

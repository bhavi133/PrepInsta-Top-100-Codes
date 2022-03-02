Link : https://prepinsta.com/python-program/to-remove-the-vowels-from-a-string/

def remove_vowels(string):
    str = ""
    vowels = list('aeiouAEIOU')
    for i in string:
        if i not in vowels:
            str = str + i
    return str

str = 'PrepInsta'
print(remove_vowels(str))

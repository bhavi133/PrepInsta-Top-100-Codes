Link : https://prepinsta.com/python-program/count-the-number-of-vowels-in-a-string/

def count_vowels(str):
    vowels = list('aeiou')
    ctr = 0
    for i in str:
        if i in vowels:
            ctr += 1
    return ctr

str = "prepinsta"
print(count_vowels(str))

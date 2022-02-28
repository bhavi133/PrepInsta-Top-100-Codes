Link : https://prepinsta.com/python-program/find-the-longest-palindrome-in-an-array/

def is_palindrome(word):
    word = str(word)
    return word == word[::-1]

arr = [1, 232, 5545455, 909090, 161]
print(max(word for word in set(arr) if is_palindrome(word)))


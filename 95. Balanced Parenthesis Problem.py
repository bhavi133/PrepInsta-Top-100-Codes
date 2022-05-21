Link : https://prepinsta.com/python-program/program-to-check-the-balance-of-parenthesis/

def balanced_parenthesis(string):
    while (len(string) != 0):
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
    if len(string) == 0:
        return True
    else:
        return False

string = input()
print(balanced_parenthesis(string))

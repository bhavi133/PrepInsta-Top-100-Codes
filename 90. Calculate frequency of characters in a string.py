Link : https://prepinsta.com/python-program/calculate-frequency-of-a-characters-in-a-string/

def frequency(string):
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

string = "prepinsta"
print(frequency(string))

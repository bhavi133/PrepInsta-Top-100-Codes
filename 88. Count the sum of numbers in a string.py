Link : https://prepinsta.com/python-program/count-the-sum-of-numbers-in-a-string/

def sum_of_numbers(string):
    sum = 0
    for i in string:
        if i.isdigit():
            sum += int(i)
    return sum

string = "12Prep20insta68"
print(sum_of_numbers(string))

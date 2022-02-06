Link : https://prepinsta.com/python-program/check-leap-year-or-not/

def leap_year(year):
    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

year = int(input("Input a year : "))
print(leap_year(year))

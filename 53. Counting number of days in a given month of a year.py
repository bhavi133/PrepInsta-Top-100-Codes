Link : https://prepinsta.com/python-program/to-count-the-number-of-days-in-a-given-month-of-a-year/

year = int(input("Input a year : "))
month = int(input("Input a month : "))
if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print("Number of days is 29")
elif month == 2:
    print("Number of days is 28")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Number of days is 31")
else:
    print("Number of days is 30")

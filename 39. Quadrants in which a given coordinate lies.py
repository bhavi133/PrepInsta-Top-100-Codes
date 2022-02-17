Link : https://prepinsta.com/python-program/quadrants-in-which-coordinates-lie/

x = int(input("Input a value for X-axis : "))
y = int(input("Input a value for Y-axis : "))
if x > 0 and y > 0:
    print("X and Y lie at first quadrant")
elif x < 0 and y > 0:
    print("X and Y lie at second quadrant")
elif x < 0 and y < 0:
    print("X and Y lie at third quadrant")
elif x > 0 and y < 0:
    print("X and Y lie at fourth quadrant")
else:
    print("X and Y lie at origin")

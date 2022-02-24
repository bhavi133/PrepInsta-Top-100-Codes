Link : https://prepinsta.com/python-program/find-roots-of-a-quadratic-equation/

from math import sqrt

a = int(input("Input value of a : "))
b = int(input("Input value of b : "))
c = int(input("Input value of c : "))
if a == 0:
    print("a cannot be zero")
else:
    val = (b * b) - (4 * (a * c))
    root = sqrt(abs(val))
    if val > 0:
        print("Two real roots")
        print((-b + root) / (2 * a))
        print((-b - root) / (2 * a))
    elif val == 0:
        print("One real root")
        print(-b / (2 * a))
    else:
        print("No Real Root")
        print(- b / (2 * a), " + i", root)
        print(- b / (2 * a), " - i", root)

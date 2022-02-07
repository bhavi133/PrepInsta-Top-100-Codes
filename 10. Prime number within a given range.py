Link : https://prepinsta.com/python-program/prime-numbers-in-a-given-range/

def prime(lower_range, upper_range):
    for i in range(lower_range, upper_range+1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)


lower_range = int(input("Input lower limit : "))
upper_range = int(input("Input upper limit : "))
print("The prime numbers between", lower_range, "and", upper_range, "are:")
prime(lower_range, upper_range)

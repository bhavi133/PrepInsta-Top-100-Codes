Link : https://prepinsta.com/program-to-check-if-the-given-number-is-prime-or-not/

def prime(n):
    if n == 1:
        print("1 is neither prime nor composite")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")


n = int(input("Input a number : "))
prime(n)

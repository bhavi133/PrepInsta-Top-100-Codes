Link : https://prepinsta.com/python-program/finding-maximum-number-of-handshakes/

n = int(input("Input the number of people : "))
number_of_handshakes = int((n - 1) * n) // 2
print(f"Maximum number of handshakes possible for {n} handshakes is : ", number_of_handshakes)

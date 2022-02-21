Link : https://prepinsta.com/python-program/addition-of-two-fractions/

f1_nume = int(input("Input the numerator for 1st fraction : "))
f1_deno = int(input("Input the denominator for the 1st fraction : "))
f2_nume = int(input("Input the numerator for 2nd fraction : "))
f2_deno = int(input("Input the denominator for the 2nd fraction : "))

if f1_deno == f2_deno:
    fraction = f1_nume + f2_nume
    print("Addition of two fractions : ", str(fraction) + "/" + str(f1_deno))
else:
    fraction = (f1_nume * f2_deno) + (f2_nume * f1_deno)
    print('Addition of fractions are : ', str(fraction) + '/' + str(f1_deno * f2_deno))

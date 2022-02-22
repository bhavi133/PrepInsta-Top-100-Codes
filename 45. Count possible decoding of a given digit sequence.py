Link : https://prepinsta.com/python-program/to-count-possible-decoding-of-a-given-digit-sequence/

def decoding(str1, s):
    if len(str1) == 0:
        print(s)
    else:
        for i in range(len(patterns)):
            if str1[:len(patterns[i])] == patterns[i]:
                decoding(str1[len(patterns[i]):], s + letters[i])

patterns= ["0", "10", "001", "010", "001"]
letters= "ABCDE"
decoding("001010", "")

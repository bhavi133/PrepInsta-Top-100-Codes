Link : https://prepinsta.com/python-program/count-common-subsequence-in-two-strings/

str1 = "ABC"
str2 = "AB"
len1, len2 = len(str1), len(str2)
var = [[0 for i in range(len1+ 1)] for i in range(len2 + 1)]
for i in range(1, len1+1):
    for j in range(1, len2+1):
         if(str1[i-1] == str2[j-1]):
             var[i][j] = 1 + var[i][j-1] + var[i-1][j]
         else:
             var[i][j] = var[i][j-1] + var[i-1][j] - var[i-1][j-1]
print(var[len1][len2])

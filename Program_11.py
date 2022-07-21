#!/usr/bin/env python

# if program is palndrom or not

def pal (num):
    x = num [ : : -1]
    if x == num :
        print(num, " given string is palandrom ")
    else:
        print(num, " given string is not a palandorm ")

str1 = input(" Enter String :")
print(pal(str1))
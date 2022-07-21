#! /usr/bin/env python

# multiplication table

from math import factorial

from cupshelpers import Printer


num = int(input("Enter a numbe:"))

factorial = 1

if num < 0:
    print("sorry, factorial does not exist for negative numbers")
elif num ==0 :
    print("the factorial or 0 is 1")
else:
    for i in range(1, num):
        factorial = factorial * i
        print(" the factorial of ", num , "is", factorial)
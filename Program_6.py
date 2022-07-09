#!/usr/bin/env python

# Positive Negative Checking using nested if

num = int(input("Ente a Num Vale: "))

if num >= 0:
    if num == 0:
        print("{0} is equal to Zero".format(num))
    else:
        print("{0} is a Positive Number ".format(num))
else:
    print("{0} is Negative Number ".format(num))
print("Program Completed")
#! /usr/bin/env python

# sum of natural numbers

num = int(input("Enter a number:"))

if num < 0:
    print(" Enter Positive Numbers Only")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("the sum is", sum)

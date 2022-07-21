#!/usr/bin/env python

# factorial number 
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)

value = int(input("enter a number: "))
print(fact(value))
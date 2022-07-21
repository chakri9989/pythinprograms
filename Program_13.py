#! /usr/bin/env python

#  tables Program

num = int(input(" Enter table number"))

for i in range(1, 11) :
    table = num * i
    print(num,"*",i,"=",table)
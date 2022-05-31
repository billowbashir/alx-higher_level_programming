#!/usr/bin/python3
def uppercase(str):
    
    for i in str:
        print("{:c}".format(ord(i)-32), end="")

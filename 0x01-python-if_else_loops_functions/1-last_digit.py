#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if int(str(number)[-1]) > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,int(str(number)[-1])), end = "")
elif int(str(number)[-1]) == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number,int(str(number)[-1])), end = "")
elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number,int(str(number)[-1])), end = "")

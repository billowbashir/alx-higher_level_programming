#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit=int(str(number)[-1]) if number > 0 else int(str(number)[-1])*-1
print("Last digit of {} is {}".format(number, lastDigit))
if lastDigit > 5:
    print(" and is greater than 5")
elif lastDigit == 0:
    print(" and is 0")
elif lastDigit < 6 and lastDigit != 0:
    print(" and is less than 6 and not 0")

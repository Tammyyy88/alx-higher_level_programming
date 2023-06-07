#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# using the if elif statement to perform checks
# check if number is positive
if number > 0:
    print("{} is positive".format(number))
# check if it's zero
elif number == 0:
    print("{} is zero".format(number))
# check if it's negative
else:
    print("{} is negative".format(number))

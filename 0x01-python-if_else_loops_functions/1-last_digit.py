#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_int = number % 10

if last_int < 6 and last_int != 0:
#    negated_int = -(last_int)
#    if number < 0:
#        print("Last digit of {number} is -{last_int} and is less than 6 and not 0")
    print(f"Last digit of {number} is {last_int} and is less than 6 and not 0")
elif last_int == 0:
    print(f"Last digit of {number} is {last_int} and is 0")
elif last_int > 5:
   print(f"Last digit of {number} is {last_int} and is greater than 5")

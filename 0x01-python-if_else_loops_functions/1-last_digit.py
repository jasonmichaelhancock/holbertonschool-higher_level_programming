#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number2 = number * -1
else:
    number2 = number
digit = number2%10
if digit > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'.format(number, digit))
elif digit == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(number, digit))
else:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.format(number, digit))
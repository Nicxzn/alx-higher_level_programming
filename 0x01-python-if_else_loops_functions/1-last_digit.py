#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print("Last digit of", number, "is", last_digit, "and is" + (" greater than 5" if last_digit > 5 else " less than 6"))

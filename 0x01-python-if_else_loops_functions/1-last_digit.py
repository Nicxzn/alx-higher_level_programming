#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Extract the last digit of the number
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
# Print the result
print("Last digit of", number, "is", last_digit, "and is" + (" greater than 5" if last_digit > 5 else (" less than 6 and not 0" if last_digit != 0 else " 0")))

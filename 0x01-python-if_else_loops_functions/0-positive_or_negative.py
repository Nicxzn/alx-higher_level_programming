#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE

print(number, "is" + (" positive" if number > 0 else (" zero" if number == 0 else " negative")))

#!/usr/bin/env/python3
def islower(c):
    # Check if the ASCII value of c is within the range of lowercase letters (97 to 122)
    return 97 <= ord(c) <= 122
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('z'))  # True
print(islower('Z'))  # False
print(islower('9'))  # False

#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the character to uppercase using ASCII values
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        # Print the uppercase character without newline
        print(uppercase_char, end='')
    # Print a newline after printing the entire string in uppercase
    print()

# Test the function
uppercase("Hello, World!")

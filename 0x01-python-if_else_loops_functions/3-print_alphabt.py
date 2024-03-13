#!/usr/bin/python3
for ascii_value in range( 97, 123):
    # Convert ASCII value to character
    letter = chr(ascii_value)
    # Check if letter is not 'q' and not 'e'
    if letter != 'q' and letter != 'e':
        # Print the letter without newline
        print("{}"letter, end='')

"""
Program: cast_to_integer.py
Author: Daniel Meeker
Last date modified: 06/01/2020


The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

num = input("Please enter a number or phrase and I "
            "will attempt to convert it to an integer: ")
num = float(num)  # First convert to float.
num = int(num)  # Then convert to int.
print(num)

"""
input    expected    result
65          65          65
6.5         6           6
Hello     error     ValueError: could not convert string to float
"""

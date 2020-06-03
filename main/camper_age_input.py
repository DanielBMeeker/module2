"""
Program: camper_age_input.py
Author: Daniel Meeker
Date: 06/03/2020

This program demonstrates Test Driven Development
in Python with a simple function and unit test.
"""


def convert_to_months(years):
    months = 12
    months *= years
    return months


if __name__ == '__main__':
    # get user input
    age_in_years = input('Please enter your age (in years): ')
    # call the function and save the result in a variable
    age_in_months = convert_to_months(int(float(age_in_years)))
    # print out the results
    print(str(age_in_years) + ' years is equal to ' + str(age_in_months) + ' months.')

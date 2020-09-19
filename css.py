"""
file: css.py
description: gets all of the inputs for the CSS code
language: python3
author: Ilyana Prince
"""


def test_colors():
    """
    Function creates a list of all the valid colors in HTML
    :return: a list of colors
    """
    color_lst = []
    with open("colors") as fd:
        for line in fd:
            line = line.strip()
            color_lst.append(line.lower())  # makes every letter lowercase
        return color_lst


valid_colors = test_colors()  # sets test_colors() to a variable


def all_color(color):
    """
    Function to check if the color given is a valid color
    :param color: color from user input
    :return: the color if it is valid
    """
    for each in valid_colors:
        if color == each:  # checks to see if the color is in the list and is therefore valid
            return color


def css_font(font):
    """
    Function to return the corresponding font from the given number
    :param font: an integer
    :return: corresponding font
    """
    font_dict = {1: "Arial", 2: "Comic Sans", 3: "Lucida Grande", 4: "Tahoma", 5: "Verdana", 6: "Helvetica",
                 7: "Times New Roman"}  # dictionary of fonts
    for key in font_dict:  # goes through the dictionary
        try:
            if int(font) == key:  # if the integer is equal to the integer key in the dictionary
                return font_dict[int(font)]  # returns the corresponding font
        except ValueError:  # checks for errors
            pass

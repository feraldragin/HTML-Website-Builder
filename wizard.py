"""
file: wizard.py
description: Contains all of the user input functions that are mainly used in wizard mode
language: python3
author: Ilyana Prince
"""
from css import *
import turtle


def turtle_font():
    """
    Helper function that creates the turtle pop up with the font displays
    """
    x = -75  # starting x coordinate
    y = 100  # starting y coordinate
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.write("Arial", font=("Arial", 14, "normal"))
    turtle.up()
    turtle.goto(x, y-20)
    turtle.down()
    turtle.write("Comic Sans MS", font=("Comic Sans MS", 14, "normal"))
    turtle.up()
    turtle.goto(x, y-40)
    turtle.down()
    turtle.write("Luicda Grande", font=("Luicda Grande", 14, "normal"))
    turtle.up()
    turtle.goto(x, y-60)
    turtle.down()
    turtle.write("Verdana", font=("Verdana", 14, "normal"))
    turtle.up()
    turtle.goto(x, y-80)
    turtle.down()
    turtle.write("Helvetica", font=("Helvetica", 14, "normal"))
    turtle.up()
    turtle.goto(x, y-100)
    turtle.down()
    turtle.write("Times New Roman", font=("Times New Roman", 14, "normal"))
    turtle.hideturtle()
    turtle.done()


def user_title():
    """
    Function that gets the title of the website from the user
    :return: the website title
    """
    title = str(input("What would you like the title to be? "))  # creates variable that stores the title string
    return title


def back_color():
    """
    Function that gets the background color of the website from the user
    Also checks to make sure the color the user inputs is a valid color in HTML
    :return: the background color
    """
    color = str(input("Choose the name of a color, or in format '#XXXXXX' for the background: "))  # creates variable
    if color == '':  # ensures the user picks a valid color
        print("Invalid color")
        return back_color()
    elif all_color(color) is None:  # ensures the user picks a valid color
        print("Invalid color")
        return back_color()
    else:
        return all_color(color)  # runs the color through the all_color function


def user_font():
    """
    Function that gets the font of the website from the user
    Runs the helper turtle function if the user requests
    Also checks to make sure the font given is a valid font
    :return: font of the website
    """
    print("Now choose a font")
    show_font = input("Would you like to see the fonts? ")  # asks the user if they want to see the turtle window
    if show_font == 'yes' or show_font == "":  # yes or enter gives the user the turtle pop up window
        turtle_font()
        print("Close the window then select the font")
    print("1. Arial\n2. Comic Sans MS\n3. Lucida Grande\n4. Tahoma\n5. Verdan\n6. Helvetica\n7. Times New Roman")
    font = input("What font would you like to use? ")  # asks the user for the font which must be

    if font == "":  # makes sure the font is valid
        print("Invalid font")
        return user_font()
    elif font is None:  # makes sure the font is valid
        print("Invalid font")
        return user_font()
    else:
        try:  # makes sure the font entered is the number in the list
            font = int(font)
            if css_font(font) is None:  # makes sure the number is a valid number
                print("Invalid font")
                return user_font()
            else:
                return css_font(font)  # runs the entered color through the css_font function
        except ValueError:  # checks for error
            print("Invalid font")
            return user_font()


def par_color():
    """
    Function that gets the paragraph color from the user
    Also checks to make sure the color is a valid color in HTML
    :return: the paragraph color for the website
    """
    color = str(input("Choose the name of a color, or in format '#XXXXXX' for the paragraph: "))  # asks for the color
    if color == '':  # ensures the color entered is valid
        print("Invalid color")
        return par_color()
    if all_color(color) is None:  # ensures the color entered is valid
        print("Invalid color")
        return par_color()
    else:
        return all_color(color)  # runs the entered color through the all_color function


def heading_color():
    """
    Function that gets the heading color from the user
    Also makes sure the color is a valid color in HTML
    :return: the heading color for the website
    """
    color = input("Choose the name of a color, or in format '#XXXXXX' for the heading: ")  # color for the heading
    if color == '':  # ensures the color is a valid color
        print("Invalid color")
        return heading_color()
    elif all_color(color) is None:  # ensures the color is a valid color
        print("Invalid color")
        return heading_color()
    else:
        return all_color(color)  # runs the color through the all_color function


def user_title_par():
    """
    Function that gets the title of a paragraph in the website
    :return: the title of the paragraph
    """
    title = str(input("What would you like the paragraph title to be? "))
    return title


def user_par_content():
    """
    Function that gets what the paragraph is supposed to say
    :return: the paragraph content
    """
    content = str(input("What would you like the paragraph to say? "))
    return content


def user_image():
    """
    Function that gets an image for the website
    :return: the image name
    """
    image = input("What picture would you like to use? ")
    return image

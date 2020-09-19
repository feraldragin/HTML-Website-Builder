"""
file: different_modes.py
description: Writes the HTML and CSS code for wizard and website mode
language: python3
author: Ilyana Prince
"""

from wizard import *
from web_site_mode import *
import sys


def wizard_mode():
    """
    Function that writes the HTML and CSS for the website mode.
    """
    tags_dict = {"title": ("<title>", "</title>"), "heading": ("<h1>", "</h1>", "<h2>", "</h2>"),
                 "paragraph": ("<p>", "</p>"), "image": ("width: ", "<img src=", " alt= ", ">")}
    # Dictionary for all the HTML tags

    title = user_title()  # sets title to what user_title returns in wizard.py
    back = back_color()  # sets back to what back_color returns in wizard.py
    font = user_font()  # sets font to what user_font returns in wizard.py
    paragraph_color = par_color()  # sets paragraph_color to what par_color returns in wizard.py
    head_color = heading_color()  # sets head_color to what heading_color returns in wizard.py
    par_title = user_title_par()  # sets par_title to what user_title_par returns in wizard.py
    content = user_par_content()  # sets content to what user_par_content returns in wizard.py
    picture = user_image()  # sets picture to what user_image returns in wizard.py

    html = "<!DOCTYPE html> <html> <head>" + tags_dict["title"][0] + title + tags_dict["title"][1] + "</head> <body>" + \
           tags_dict["heading"][0] + title + tags_dict["heading"][1] + tags_dict["heading"][2] + par_title + \
           tags_dict["heading"][3] + tags_dict["paragraph"][0] + content + tags_dict["paragraph"][1] + \
           "<center>" + tags_dict["image"][1] + '"' + picture + '"' + tags_dict["image"][2] + '""' + \
           tags_dict["image"][3] + "</center>"  # string for the HTML code using the variable and the dictionary

    extra_image_q = input("Would you like to add another picture?")  # asks the user if they want another picture

    while extra_image_q == "yes" or extra_image_q == "":  # while loop for as long as the user wants another picture
        extra_image = input("What picture would you like to use?")
        html = html + tags_dict["image"][1] + '"' + extra_image + '"' + tags_dict["image"][2] + '""' + \
            tags_dict["image"][3]  # adds the image the the HTML string
        extra_image_q = input("Would you like to add another picture?")

    extra_par_q = input("Would you like to add another paragraph?")  # asks the user if they want another paragraph

    while extra_par_q == "yes" or extra_image_q == "":  # while loop for as long as the user wants another paragraph
        extra_title = input("What would you like the title to be?")
        extra_par = input("What would you like the paragraph to say?")
        html = html + tags_dict["heading"][2] + extra_title + tags_dict["heading"][3] + tags_dict["paragraph"][0] + \
               extra_par + tags_dict["paragraph"][1]  # adds the extra paragraph to the HTML string
        extra_par_q = input("Would you like to add another paragraph?")

    css = "<style> body {background-image: linear-gradient(180deg, " + back + ", white);} .center { display: block; " \
          "margin-left: auto; margin-right: auto; } h1   {color:" + head_color + "; font-family:" + font + "; text-ali" \
          "gn:center; } h2   {color: " + head_color + "; font-family:" + font + "; text-align: justify; } p {color:" \
          + paragraph_color + "; font-family:" + font + "; padding: 30px; text-align: justify; background-color: white" \
          "; box-shadow: 4px 0 2px -2px rgba(0,0,0,0.4); font-size: 14px; }</style> </body> </html>"
    # string for the CSS code

    website = html + css  # combines the HTML and the CSS code
    with open("test.html", "w") as f:
        f.write(website)  # writes the website in an HTML file


def website_mode():
    """
    Function that gets the HTML and CSS code for website mode
    """
    files = sys.argv[1:]  # files from the command line
    html = '<!DOCTYPE html> <html> <head>'  # starter tags for the
    file_name = ""
    back = back_color()  # sets back to what back_color returns in wizard.py
    font = user_font()  # sets font to what user_font returns in wizard.py
    paragraph_color = par_color()  # sets paragraph_color to what par_color returns in wizard.py
    head_color = heading_color()  # sets head_color to what heading_color returns in wizard.py

    css = "<style> body {background-image: linear-gradient(180deg, " + back + ", white);} .center { display: block" \
          "; margin-left: auto; margin-right: auto; } h1   {color:" + head_color + "; font-family:" + font + ";" \
          "text-align:center; } h2   {color: " + head_color + "; font-family:" + font + "; text-align: justify; " \
          "} p {color:" + paragraph_color + "; font-family:" + font + "; padding: 30px; text-align: justify; bac" \
          "kground-color: white; box-shadow: 4px 0 2px -2px rgba(0,0,0,0.4); font-size: 14px; }</style> </body>" \
          "</html>"  # string for the CSS code

    for names in files:  # loops through the names of each file
        place_name = "<a href= \" " + str(names) + ".html\" >"  # sets the code for links into a variable
        test_title = read_file(names)  # sets the list from read_file to a variable

        for each in test_title:  # loops through each entry of the list
            if each == test_title[0]:  # looks for the title of the web page
                title = each  # sets the title of the web page to the variable
        file_name = place_name + title + "</a>  ---  " + file_name  # adds the web page title to the link variable

    for i in files:  # loops through each file
        lines = read_file(i)  # reads the file
        for each in lines:  # goes through each section of the list lines
            if each == lines[0]:
                html = html + "<title>" + each + "</title> </head> <body> <h1> " + each + "</h1> " + file_name
                # adds the title and the the title tags to the HTML string
            elif each == "!new_paragraph":  # every time !new_paragraph shows up it gets rid of it
                each = each.strip("!new_paragraph")
            elif "!title" in each:  # if !title is contained in any entry in the list
                each = each.strip("!title")  # gets rid of !title
                html = html + "<h2>" + each + "</h2>" + "<p>"  # adds title and corresponding HTML tags to the string
            elif "!image" in each:  # if !image is contained in any entry in the list
                each = each.strip("!image")  # gets rid of !image
                image_lst = each.split()  # splits the rest of the entry
                if len(image_lst) <= 1:  # if the number of entries in the new list is less than or equal to 1
                    width = "100%"  # width is 100% since no width was specified
                else:
                    width = image_lst[1]  # width was specified and is put in the width variable
                html = html + "</p>" + "<center> <img src=" + '"' + image_lst[
                    0] + '"' + "alt= \"\"" + "style=\"width:" + width + "\"></center>"  # adds image info and tags
            else:
                html = html + each + " "  # adds any other information into the HTML string

        website = html + css  # combines the HTML and CSS code

        with open(i + ".html", "w") as f:
            f.write(website)  # writes the code into an HTML file
        html = '<!DOCTYPE html> <html> <head>'  # resets the HTML string for the next file

"""
file: website_mode.py
description: Reads a file and puts the contents into a list. Used for web site mode
language: python3
author: Ilyana Prince
"""


def read_file(file):
    """
    Function that reads a file and puts the contents in a list
    :param file: the file in the command line that has the contents for a website
    :return: the contents in the file as a list
    """
    with open(file, errors='ignore') as fd:  # opens the file
        lst = []
        for line in fd:
            line = line.strip()
            lst.append(line)  # puts each line as an entry in the list
        return lst




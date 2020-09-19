"""
file: html_builder.py
description: decides whether or not to run wizard or website mode and then calls those functions from the other files
language: python3
author: Ilyana Prince
"""

from different_modes import *
import sys


def main():
    """
    Main function
    Decides whether to run wizard or website mode
    """
    if len(sys.argv) > 1:  # checks to see if there are any files in the command line
        website_mode()
    else:
        wizard_mode()


if __name__ == '__main__':
    main()

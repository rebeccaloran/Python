# -*- coding: utf-8 -*-
# File: ex8.py
# Description: Printing, Printing
# Python 2.7.5 (default, May 12 2013, 12:27:12) 
#

# sets 4 [ %r ] formatters to the variable [ formatter ]
formatter = "%r %r %r %r"

# prints [ formatter ] with the format resolved with the integers `(1, 2, 3, 4)'
print formatter % (1, 2, 3, 4)
# prints [ formatter ] with the format resolved with the strings `("one", "two", "three", "four")'
print formatter % ("one", "two", "three", "four")
# prints [ formatter ] with the format resolved with the boolean values `(True, False, False, True)'
print formatter % (True, False, False, True)
# prints [ formatter ] with the format resolved with the variables `(formatter, formatter, formatter, formatter)'
print formatter % (formatter, formatter, formatter, formatter)
# prints [ formatter ] with the format resolved with the strings separated by a comma to produce output on the 
# same line, using text indenting to increase readability.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )

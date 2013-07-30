# -*- coding: utf-8 -*-
# File: ex6.py
# Description: Strings and Text
#
# [ x ] and [ y ] are cryptic because the author of this tutorial wishes to express the annoyance of {magic variables}
# Assigns the string to [ x ], with [ %d ] represented by the number  `10'
x = "There are %d types of people." % 10
# Assigns the string `binary' to [ binary ]
binary = "binary"
# assigns the string `don\'t' to [ do_not ]
# // I escape the [ ' ] to avoid confusion, best to be consistent and just always escape escaped characters. 
do_not = "don\'t"
# Assigns the string to [ y ], with [ %s ] and [ %s ] being represented by [ (binary, do_not) ]
y = "Those who know %s and those who %s" % (binary, do_not)
# Prints [ x ]
print x
# Prints [ y ]
print y
# Prints the string, with [ %r ] represented by [ x ]
print "I said: %r" % x
# Prints the string, with [ %s ] represented by [ y ]
print "I also said: '%s'." % y

# Assigns [ hillarious ] the boolean value of `False'
hillarious = False
# Assigns [ joke_evaluation ] the string, initiating [ %r ]
joke_evaluation = "Isn't that joke so funny?! %r"
# Finalizes [ %r ] with [ hillarious ] concatenated after [ joke_evaluation ] 
print joke_evaluation % hillarious 

# Assigns the string to [ w ]
w = "This is the left side of..."
# Assigns the string to [ e ]
e = "a string with a right side."

# Prints [ e ] concantenated after [ w ]
print w + e

# -*- coding: utf-8 -*-
# File: ex10.py
# Description: What was that?
# Python 2.7.5 (default, May 12 2013, 12:27:12) 
#

# Escaped Characters
# -==- Example -==-
# "I am 6'2\" tall."  # escape double-quote [ " ] inside string
# 'I am 6\'2" tall. " 	# escape single-quote [ ' ] inside string
#
# triple-quotes also work


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat



###########################################################
# | Escape	| 	| What it does. 		|
#---------------------------------------------------------#
# | \\		|	| Backslash ()  		|
#---------------------------------------------------------#
# | \'		| 	| Single-quote (')		|
#---------------------------------------------------------#
# | \"		|	| Double-quote (")		|
#---------------------------------------------------------#
# | \a		|	| ASCII bell (BEL)		|	
#---------------------------------------------------------#
# | \b		|	| ASCII backspace (BS)		|
#---------------------------------------------------------#
# | \f		|	| ASCII formfeed (FF)		|
#---------------------------------------------------------#
# | \n		|	| ASCII linefeed (LF)		|
#---------------------------------------------------------#
# | \N{name}	|	| {Unicode character}		|
#---------------------------------------------------------#
# | \r ASCII	|	| Carriage Return (CR)		|
#---------------------------------------------------------#
# | \t ASCII	|	| Horizontal Tab (TAB)		| 
#---------------------------------------------------------#
# | \uxxxx	| 	| Unicode 16-bit hex 		| 
#---------------------------------------------------------#
# | \Uxxxxxxxx	|	| Unicode 32-bit hex		|
#---------------------------------------------------------#
# | \v		|	| ASCII vertical tab (VT)	|
#---------------------------------------------------------#
# | \ooo	|	| octal value ooo		|
#---------------------------------------------------------#
# | \xhh	| 	| hex value hh			|
#---------------------------------------------------------#

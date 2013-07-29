# -*- coding: utf-8 -*-
# File: ex5.py
# Description: More Variables and Printing
# Python 2.7.5 (default, May 12 2013, 12:27:12) 
#





name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %.0f centimeters tall." % (height * 2.54)
print "He's %.0f kilograms heavy." % (weight * 0.5)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it _exactly_ right
print "If I add %d, %.0fcm, and %.0fkg I get %.0f." % (
    age, (height * 2.54), (weight * 0.5) , age + (height * 2.54)  + (weight * 0.5)
    )



###########################################################
#Distance
# 1 inch   =	 2.54 cm
# 1 foot	 =	 0.3 meters
# 1 yard	 =	 0.9 meters
# 1 mile	 =	 1.6 kilometers
# Weight
# 1 ounce	 =	 28.4 grams
# 1 pound	 =	 0.5 kilograms
# Volume
# 1 teaspoon	 =	 4.9 milliliters
# 1 cup	  	 =	 237 milliliters
# 1 pint	 =	 473 milliliters
# 1 quart	 =	 0.9 liters
# 1 gallon	 =	 3.79 liters
# Temperature
#
# To convert from degrees C to degrees F
#
# (deg C x 9/5) + 32
#
# To convert from degrees F to degrees C
#
# (deg F – 32) x 5/9

# -*- coding: utf-8 -*-
# File: ex4.py
# Description: Variables and Names
# Python 2.7.5 (default, May 12 2013, 12:27:12) 
#






# sets `cars' variable to 100
cars = 100
# defines a floating point variable as the `space_in_a_car' variable
space_in_a_car = 4.0
# sets `drivers' variable to 30
drivers = 30
# sets `passengers' variable to 90
passengers = 90
# formula to determine how many cars are unused
cars_not_driven = cars - drivers
# assigns drivers to the cars which are used
cars_driven = drivers
# formula to determine the amount of space available for passengers
carpool_capacity = cars_driven * space_in_a_car
# formula to determine the average passengers per car by dividing `passengers' by `cars_driven'
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."



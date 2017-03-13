# Exercice No4 Of the LPTHW book
# this bunch defines the vraibles
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
# this bunch calculates the variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Here we print to the screen the results
print "there are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

from sys import argv

script, first, second, third = argv

print "The script is called :", script
print "your first variable is :", first
print "your second variable is :", second
print "your third variable is :", third

x = raw_input("what is yout age :")
y = raw_input(" what is yout name :")

print "Well hello there %s, your are %s old" % (y, x)

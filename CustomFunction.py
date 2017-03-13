# creates a function that use assigned variables


def add(a, b):
    print "Let's add %s + %s" % (a, b)
    return a + b

print "Plase add two numbers for addition"
_a = int(raw_input("enter a first number: "))
_b = int(raw_input("enter a second number: "))
Display = add(_a, _b)

print "equals = %d" % (Display)

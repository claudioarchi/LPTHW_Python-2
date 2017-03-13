def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def substract(a, b):
    print "SUSBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just fonctions"

age = add(30, 50)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type this anyway
print "Here is a puzzle"

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do this by hand?"

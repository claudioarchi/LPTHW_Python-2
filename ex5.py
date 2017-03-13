name = 'Claudio Nunez'
age = 43 #Not a lie
height = 69 #Inches
weight = 160 #punds
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
Tocm = 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "or %d centimetres" % (height * Tocm)
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print  "His teeth are usually %s depending on the cofee." % teeth

#this line is a bit tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

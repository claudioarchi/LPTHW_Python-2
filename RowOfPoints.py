# Create a row of points with (x, y) as user input
x = int(raw_input(">: "))
y = int(raw_input(">: "))

while x < 50 and y < 100:
    x += 1
    y += 1
    print "(%r,%r)" % (x, y)

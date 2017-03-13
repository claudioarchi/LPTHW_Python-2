# this will calculate site density based on a given surface project
def density(project, area):
    x = project / area
    print ("\t<< the density of your project is : %r >>" % x)


area = float(raw_input("input site area:"))
project = float(raw_input("input total project area:"))

density(project, area)

allowedDensity = raw_input("input allowed density :")

if allowedDensity < density:
    print "Your are ok"
elif allowedDensity > density:
    print "not possible"

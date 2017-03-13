# this will calculate site density based on a given surface project

#  Ask for primary data
SiteArea = float(raw_input("what's the site area in m.ca.:"))
allowedDensity = float(raw_input("what the density allowed:"))
ProjectArea = float(raw_input("what's the total brut area of your project in m. ca.:"))

project_density = ProjectArea / SiteArea
print ("the desity of your project is : %r" % project_density)

# Calculate the approuval of the project
if project_density > allowedDensity:
    print ("Your project cannot be constructed.")
elif project_density <= allowedDensity:
    print ("Your project is allowed to be build.")
else:
    print ("you are ok.")

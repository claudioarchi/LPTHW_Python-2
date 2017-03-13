from sys import argv

# defines the values for the arguments
script, filename = argv

# variable txt with the command to open a file (the name of the file to open)
txt = open(filename)

# tells me the name of the file I just open
print "Here's your file %r: " % filename
# this fonctions reads the var txt just opened
print txt.read()

# asks for the filename again as inoput form user
print "type the filename again :"
file_again = raw_input("> ")

# opens the file with the filename given by user
txt_again = open(file_again)

# prints the file just opened
print txt_again.read()
txt_again.close()
txt.close()

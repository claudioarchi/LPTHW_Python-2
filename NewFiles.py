# This will create one txt file , asks for some context and then
# copy the file to an other one

print "This will create a file and then copy it to a different one"

# Request input from user
print "Give a name to your file"
FirstFile = raw_input("Filename :")
# Request txt from user
Content = raw_input("please add some text :")

# Write to new file (Target)
Target = open(FirstFile, 'w').write(Content)

# Now lets copy it
print "Give a name to your new file"
SecondFile = raw_input("New Filename :")
indata = open(FirstFile).read()
NewTarget = open(SecondFile, 'w').write(indata)

from sys import argv

scrip, filename = argv
txt = open(filename).read()
print "This is the content of your file :"
print txt

print "Now let's add a line :"
_content = raw_input("write something:")  # content to be written in the file
print "You added : %s" % (_content)

txt = open(filename, 'a')  # in append mode it will get to the last line
txt.write("\n" + _content)

txt.close()

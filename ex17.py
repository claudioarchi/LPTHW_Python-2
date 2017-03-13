from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do this in one line, how?
indata = open(from_file).read()
# in_file = open(from_file)
# indata = in_file.read()

print indata

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
# print "Ready, hot RETURN to continue, CTRL-C to abort."
# raw_input()

out_file = open(to_file, 'w').write(indata)
# out_file.write(indata)

# out_file.close()
# indata.close()

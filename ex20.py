from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline(),   # The coma at the end makes the print
    # output to single interlines

current_file = open(input_file)

print "First let's open the whole file : \n"

print_all(current_file)

print "Now lets rewind, kind of like a tape."

rewind(current_file)   # the rewind is necessary as
# needs to go bak in order to count tghe lines

print "Lets print three lines: \n"

current_line = 1
print_a_line(current_line, current_file)  # calls the function print_a_line

current_line += 1  # the += signs adds a value to the variable
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

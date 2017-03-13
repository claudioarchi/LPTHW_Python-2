def count(letters):
    print letters
    print "your phrase contains %d letters.\n" % len(letters)
    # this len function counts spaces as characters


print "lets input some words"
Input = raw_input("type your letters :")
count(Input)

print "now with math."
x = (10 * "w")
count(x)

print "now with strings and math"
y = ("hello " + "my baby" + " Clara")
count(y)

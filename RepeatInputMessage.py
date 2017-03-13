# this  function will repeat some message from the user a given number of times
def repetitions(message, Nbr):
    print message * Nbr


# Here I declare the variable to be used in the fonction
# The _charcater means an input from the user
print "Please input a message"
_message = raw_input("message: ") + "\n"

print "Please input a number of repetitions"
_Nbr = int(raw_input("Number of repetitions: "))

repetitions(_message, _Nbr)

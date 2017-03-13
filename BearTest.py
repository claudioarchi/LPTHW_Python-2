from sys import exit

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door"
    print "How are you going to move the bear?"
    bear_moved = False
    print "\t>>>>>Var0: %r" % bear_moved

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            print "\t>>>>>Var1: %r" % bear_moved
            exit(0)#dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "\t>>>>>Var2: %r" % bear_moved
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            print "\t>>>>>Var3: %r" % bear_moved
            exit(0)#dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            print "\t>>>>>Var4: %r" % bear_moved
            exit(0)#gold_room()
        else:
            print "\t>>>>>5: %r" % bear_moved
            print "I got no idea what that means."


bear_room()

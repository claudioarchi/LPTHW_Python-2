print ("You entre a dark room with two doors.Do you go through door #1 or door #2?")

door = raw_input("> ")

if door == "1":
    print ("There's a giant bear here eating a cheese cake. What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream at the bear.")
    print ("3. Suck the bear")

    bear = raw_input("> ")

    if bear == "1":
        print ("The bear eats you face off. Good job!")
    elif bear == "2":
        print ("The bear east your legs. Good job!")
    elif bear == "3":
        print ("You choose %s. You are a sucker!" % bear)
    else:
        print ("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print ("you stare into the endless abys at Cthulhu's retina.")
    print ("1. Blueberries")
    print ("2. Yello jaket clothespins.")
    print ("3. Understanding revolvers yelling melodies.")

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print ("Your body survives powered by a mind jello. Good job!")
    else:
        print ("The insanity rots your eyes into a pool of muck. Good job")

else:
    print ("You stumble around and fall on a knife and die. Good job!")

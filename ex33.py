i = 0
numbers = []

while i < 6:
    print ("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print ("Numbers now:", numbers)
    print ("At the bottom i is %d" % i)


print "The numbers: "

for num in numbers:
    print num

# these are the study drills bellow:


def study_1(n):
    i = 0
    numbers1 = []

    while i < n:
        print ("index: %d" % i)
        numbers1.append(i)
        i = i + 1

    print numbers1


def study_2(n):
    i = 0
    numbers2 = []

    while i < n:
        print ("index: %d" % i)
        numbers2.append(i)
        i = i + 1

    print numbers2


# Here the inc will give the increment ratio
def study_3(n, inc):
    i = 0
    numbers3 = []

    while i < n:
        print ("index: %d" % i)
        numbers3.append(i)
        i = i + inc

    print numbers3


def study_5(n, inc):
    numbers5 = range(0, n, inc)
    for i in numbers5:
        print ("Item : %d" % i)

    print numbers5


def study_6(n, inc):
    for i in range(0, n, inc):
        print ("Item : %d" % i)


study_1(4)
study_2(12)
study_3(8, 2)
study_5(8, 2)
study_6(35, 2)

# This will be a text game
# The game is based on a simple permit procedure
# architectural project. The user will be propted with a series of questions
# its inputs will be passed through functions with boolean tests in order
# to complete the game

from sys import exit


def docs():
    print ("You need at least 3 documents")
    print ("Please input the name of your documents:")
    docs = []
    doc1 = raw_input("\twhat's your first document:")
    doc2 = raw_input("\twhat's your second document:")
    doc3 = raw_input("\twhat's your third document:")
    docs.append(doc1)
    docs.append(doc2)
    docs.append(doc3)

    print ("These are your submitted documents:")

    for i, doc in enumerate(docs, 1):
        print "\tdocument %d : %s" % (i, doc)
    print "\t", ("-") * 10
    density()


def density():
    print("""We need to verify if the project's within the bounds of density regulations.""")
    print ("The allowed density is : 12")
    project_area = raw_input("Please input project's total area: ")
    site_area = raw_input("Please input site's total area: ")
    allowed_density = 12.0
    project_density = int(project_area) / int(site_area)

    if project_density <= allowed_density:
        print ("your project density is: %d" % project_density)
        print ("You are good to go!")
        print "\t", ("-") * 10
        define()
    elif project_density > allowed_density:
        print ("your project density is: %d" % project_density)
        print ("\tThe allowed density is %d:" % allowed_density)
        end("Your project does not comply with ciy regulations.\nDo your work and please come back.")


def define():
    print ("You need to define your project aesthetics")
    print ("input the main aesthetics caracteristics of your project.")
    print ("be precise and use the right word:")
    print ("\tHint: BEAUTY IS IN THE EYE OF THE BEHOLDER")
    keep = False

    while True:
        answer = raw_input("> ")

        if answer == "beautifull":
            end("Nicelly done!")
        elif answer == "nice" and not keep:
            print("This is not the right description. AGAIN!")
        elif answer == "simple" and not keep:
            print("You are a bad architect.AGAIN!")
        else:
            end("NOT. You should learn how to present your project SUCKER!")


def end(endsession):
    print endsession, ", bye!"
    exit(0)


def start():
    print ("You are going to submit your project for approuval")
    print ("Are your documents ready?")
    answer = raw_input("> ")

    if "yes" in answer:
        docs()
    elif "no" in answer:
        end("\tReturn to do your job!")


start()

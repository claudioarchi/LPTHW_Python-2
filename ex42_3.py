import sys
print(sys.version)


# Animal is-a object
class Animal(object):
    def __init__(self, species):
        self.species = species

    def animal_type(self):
        print ("%s" % (self.species))

    def animal_action(self):
        if self.species == "Feline":
            print ("A %s drinks milk" % (self.species))

        elif self.species == "Canine":
            print ("A %s likes meat and water" % (self.species))

        elif self.species == "Bird":
            print ("A %s it flies and likes seeds" % (self.species))

        else:
            print ("A %s is not an animal I recognize" % (self.species))


cat = Animal("Feline")
cat.animal_type()
cat.animal_action()

olga = Animal("Canine")
olga.animal_type()
olga.animal_action()

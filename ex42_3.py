import sys
print(sys.version)


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


Animal_list = {
    'lion': 'carnivora', 'bat': 'mammal', 'anaconda': 'reptile',
    'salmon': 'fish', 'whale': 'cetaceans', 'spider': 'arachnida',
    'grasshopper': 'insect', 'aligator': 'reptile', 'rat': 'rodents',
    'bear': 'mammal', 'frog': 'amphibian', 'turtles': 'testudines'
}

_input = raw_input("> ")
# print "A %s is a %s " % (_input, Animal_list[_input])

cat = Animal(_input)
cat.animal_type()
cat.animal_action()

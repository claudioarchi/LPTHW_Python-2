import sys
print(sys.version)


class Animal(object):
    def __init__(self, some_input):
        self.some_input = some_input

    def animal_type(self, choice):
        self.choice = choice
        Animal_list = {
            'lion': 'carnivora', 'bat': 'mammal', 'anaconda': 'reptile',
            'salmon': 'fish', 'whale': 'cetaceans', 'spider': 'arachnida',
            'grasshopper': 'insect', 'aligator': 'reptile', 'rat': 'rodents',
            'bear': 'mammal', 'frog': 'amphibian', 'turtles': 'testudines'
        }

        if choice in Animal_list:
            print "A %s is a %s" % (choice, Animal_list[choice])
        else:
            print ">> %s << is not in the provided list" % (choice)


print ("\tChoose an animal from the list bellow to know it's species:")
Animal_choice = [
    'lion -', 'bat -', 'anaconda -', 'salmon -', 'whale -', 'spider -',
    'grasshopper -', 'aligator -', 'rat -', 'bear -', 'frog -',
    'turtles'
]

for i in Animal_choice:
    print i,

_input = raw_input("> ")
some_animal = Animal(_input)
some_animal.animal_type(_input)

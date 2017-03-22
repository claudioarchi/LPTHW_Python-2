# This code will print a prompt to Choose an animal to know its species

Animal_list = {
    'lion': 'carnivora', 'bat': 'mammal', 'anaconda': 'reptile',
    'salmon': 'fish', 'whale': 'cetaceans', 'spider': 'arachnida',
    'grasshopper': 'insect', 'aligator': 'reptile', 'rat': 'rodents',
    'bear': 'mammal', 'frog': 'amphibian', 'turtles': 'testudines'
}

print "Choose an animal from the list bellow"

for i in Animal_list.keys():
    print "%s -" % i,

while True:
    choice = raw_input("> ")
    if choice in Animal_list:
        print "%s is a %s" % (choice, Animal_list[choice])
    else:
        print ">>>%s<<< is not in the list, Bye" % (choice)
        break

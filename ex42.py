# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, type):


# is-a
class Dog(Animal):

    def __init__(self, name):
        # has-a name
        self.name = name


# is-a
class Cat(Animal):

    def __init__(self, name):
        # self has-a name of some sort
        self.name = name


# is-a
class Person(object):

    def __init__(self, name):
        # self has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# is-a
class Employee(Person):

    def __init__(self, name, salary):
        # has-a hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # self has some salary
        self.salary = salary


# is-a
class Fish(object):
    pass


# is-a
class Salmon(Fish):
    pass


# is-a
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-a pet
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()

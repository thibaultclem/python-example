#
# Introduction to Object Oriented Programing (OOP) with Python
#

## Class, Instance, Object, Attribute and Method
print "\n#Class, Instance, Object, Attribute and Method \n"

# Simple Python class: PartyAnimal
class PartyAnimal:
    # attributes
    x = 0
    name = ""
    # constructor
    def __init__(self, nam):
        self.name = nam
        print self.name,"constructed"
    # deletor
    def __del__(self):
        print self.name,"destructed"
    # methods
    def party(self):
        self.x = self.x + 1
        print self.name,"party count =",self.x

# Create a PartyAnimal instance/object
john = PartyAnimal("John")

# Create another PartyAnimal instance
bob = PartyAnimal("bob")

# Call method of an object
john.party()
john.party()
john.party()
bob.party()


## Inheritance
print "\n#Inheritance \n"

# Simpe class FootballFan (child) inherit PartyAnimal (parent)
# It has all the capabilities of PartyAnimal and more
class FootballFan(PartyAnimal):
    # child attribute
    points = 0
    # child methods
    def touchdown(self):
        self.points = 7
        # child inherit parent method:
        self.party()
        # child inherit parent attribute:
        print self.name,"points",self.points

# Create FootballFan instance
jacky = FootballFan("jacky")

# Call Football fan method
jacky.touchdown()

## Utils methods
print "\n#Utils methods for instance \n"

#Print type of an instance
print "Type",type(john)

# Print available method of an object
print "Dir",dir(john)

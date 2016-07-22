
#Objects Worksheet
#Girls Who Code SIP 2016
#AOL DC


class Monster():
    """
    Instance is a monster with a name, height, and a weight.
    """
    def __init__(self, name, height, weight):
        """
        Initializes a Monster instance.
        
        Parameter name: The name of the monster.
        Precondition: name is a string.
    
        Parameter height: The height of the monster.
        Precondition: height is a float.
        
        Parameter weight: The weight of the monster.
        Precondition: weight is a float.
        """
        self.name = name
        self.height = height
        self.weight = weight
    
    def makeSpookySound(self, noise):
        """
        Returns: The monster declares its name and yells a given noise as a string.
        """
        return "I am " + self.name + ". " + noise + "!"
    
    def getScarinessLevel(self):
        """
        Returns: The scariness level of the monster as a float.
        """
        return self.height * self.weight
    
class HauntedHouse():
    """
    Instance is a haunted house with an address and a list of resident Monsters.
    """
    def __init__(self, address, residents):
        """
        Initializes a HauntedHouse instance.
        
        Parameter address: The address of the haunted house.
        Precondition: address is a string
        
        Parameter residents: The Monsters living in the haunted house.
        Precondition: residents is a list of Monster objects.
        """
        self.address = address
        self.residents = residents
    
    def spook(self):
        """
        Calls makeSpookySound for each resident of the Haunted House.
        """
        for monster in residents:
            monster.makeSpookySound("roar")
            

monster1 = Monster("Sully", 100, 200)
print(monster1.getScarinessLevel())

monster2 = Monster("Mike", 50, 100)
monster3 = Monster("No name", 123, 43.3)
haunted = HauntedHouse("100 Spooky Lane", [monster1, monster2, monster3])
haunted.spook()


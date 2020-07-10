from random import randint

class Product:
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5, identifier = randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            print("Not so stealable")
        elif ratio >= 0.5 or ratio < 1.0:
            print("Very Stealable")
            return
    def explode(self):
        calc = self.flammability * self.weight
        if calc < 10:
            print("Fizzle")
        elif calc >= 10 or calc < 50:
            print("boom")
            return
class BoxingGlove(Product):
    """ Child class inheritance from Product Class
    """
    def __init__(self, name, price = 10, weight = 10, flammability = 0.5, identifier = randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    def explode(self):
        """
        Overriding the previous method from parent class
        """
        calc = self.flammability * self.weight
        if calc < 10:
            print("its a glove")
        elif calc >= 10 or calc < 50:
            print("its a glove")
            return
    def punch(self):
        """ Returns a statement based on conditions
        """
        pounds = self.weight
        if pounds < 5:
            print("Hey that hurt!")
        elif pounds >= 5 or pounds < 15:
            print("OUCH")
            return
        
        

        




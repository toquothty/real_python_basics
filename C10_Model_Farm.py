# Chapter 10 Challenge: Model a Farm
# 
# 1 - Must have at least 4 classes, a parent Animal and three child animals
#
# 2 - Each class should have attributes and at least one method that models animal specific behavior
# i.e. running, sleeping, flying, etc
#
# 3 - KISS. Utilize inheritance. Output details about the animals and their details.

class Animal:
    
    def __init__(self, name, total_animals, shelter):
        self.name = name
        self.total_animals = total_animals
        self.shelter = shelter
        
    def produces(self, product):
        return f"{self.name}, there are {self.total_animals} and they produce {product}"

    def transport(self, transport_type):
        return f"{self.name} gets around by {transport_type}, they live in {self.shelter}"


        
class Chicken(Animal):

    def produces(self, product = ("Eggs")):
        return super().produces(product)

    def transport(self, transport_type = ("Wings")):
        return super().transport(transport_type)

class Horse(Animal):

    def produces(self, product = ("Labor")):
        return super().produces(product)

    def transport(self, transport_type = ("Legs")):
        return super().transport(transport_type)

class Cow(Animal):

    def produces(self, product = ("Milk and Meat")):
        return super().produces(product)

    def transport(self, transport_type = ("Legs")):
        return super().transport(transport_type)

chickens = Chicken("Chickens", 87, "Coop")
horses = Horse("Horses", 4, "Barn")
cows = Cow("Cows", 11, "Barn")

print(chickens.produces() +  "\n"  + chickens.transport() + "\n")
print(cows.produces() +  "\n"  + cows.transport() + "\n")
print(horses.produces() +  "\n"  + horses.transport() + "\n")
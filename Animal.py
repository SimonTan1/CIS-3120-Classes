class Animal:

    def __init__(self, name):
        self.__name = name
        print("name of the animal is", self.__name)

    def talk(self, speak=None):
        self.speak = speak
        if self.speak == "yes":
            print("the animal is capable of speach")
        else:
            print("the animal is not capable of speach")

    def weight(self, w):
        self.weight = w
        if self.weight > 100:
            print("animal is heavier than 100 lbs")
        else:
            print("animal is under 100 pounds")

    def age(self, years):
        self.age = years
        print("i am", self.age, "years old")

    def gender(self, gen):
        animal_gender = {
            "male": "xy",
            "female": "xx"
        }
        print(f"the animal has {animal_gender[gen]} chromosomes")

    def species(self, species):
        self.species = species
        print("the species is", self.species)




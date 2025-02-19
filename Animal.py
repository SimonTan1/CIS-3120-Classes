class Animal:
    species1 = "Homo Sapiens"
    
    def __init__(self, name):
        self.__name = name
        print("hello, i am", self.__name)

    def talk(self):
        print("hi")
        print("I can talk")
     
    def weight(self, w):
        self.weight = w
        if self.weight > 100:
            print("i am heavier than 100 lbs")
        else:
            print("i am under 100 pounds")
            
    def species(self):
        print(self.species1)
 
    def limbs(self, n):
        self.limbs = n
        print ("i have", self.limbs, "limbs")
        legs = self.limbs/2
        print (legs,"of them are legs")
    
    

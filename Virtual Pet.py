# Jamie Hilton
# 09/06/2015
# Virtual Pet v1.0

class VirtualPet:
    def __init__(self):
        self.name = None
        self.size = 0
        self.age = 0
        self.energy = 50
        self.foods = ["Taco", "Orange Juice", "People", "mtn dew"]
        self.mood = 5
        print("I have been born")

    def eat(self, food):
        if food in self.foods:
            if food == self.foods[0]:
                print("Nom")
                self.energy = self.energy + 10
                print("Energy + 10") 
                self.mood = self.mood + 1
                print("Mood + 1")
                self.size = self.size + 1
                print("Size + 1")
            elif food == self.foods[1]:
                print("gulp")
                self.energy = self.energy + 5
                print("Energy + 5")
                self.mood = self.mood + 1
                print("Mood + 1")
            elif food == self.foods[2]:
                print("Yum")
                self.energy = self.energy + 20
                print("Energy + 20")
                self.mood = self.mood + 2
                print("Mood + 2")
                self.size = self.size + 5
                print("Size + 5")
            elif food == self.foods[3]:
                print("Glug, glug")
                self.energy = self.energy + 50
                print("Energy + 50")
                self.mood = self.mood + 1
                print("Mood + 1")
                self.size = self.size + 2
                print("Size + 2")
            else:
                print("I hate that!")
                self.mood = self.mood - 1
                print("Mood -1")
def Mood(pet_one):
    if pet_one.mood > 4:
        mood = "Happy"
    else:
        mood = "Grumpy"
    print("I am {0}".format(mood))


# Main Program

pet_one = VirtualPet()

pet_one.name = input("Whats my name?: ")

print("Hi there!")

print("My name is {0}".format(pet_one.name))

food = input("What can I eat or drink: ")

pet_one.eat(food)


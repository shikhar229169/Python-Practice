class Cat:
    def __init__(self, name, breed, power, cuteness, wins):
        self.name = name
        self.breed = breed
        self.power = power
        self.cuteness = cuteness
        self.wins = wins
    
    def __str__(self):
        return f"{self.name} is a {self.breed} cat with {self.power} power and {self.cuteness} cuteness"

    def meow(self):
        return f"Meow from {self.name}"
    
    def __lt__(self, otherKitty):
        # the magnitude for comparison will be 100% of power, but 50% of cutness
        myMagnitude = self.power + self.cuteness/2
        otherMagnitude = otherKitty.power + otherKitty.cuteness/2
        return myMagnitude < otherMagnitude
    
    def catFight(self, otherKitty):
        if self > otherKitty:
            print(f"{self.name} wins!")
            self.wins += 1
            self.power += 2
        elif (otherKitty > self):
            print(f"{otherKitty.name} wins!")
            otherKitty.wins += 1
            otherKitty.power += 2
        else:
            print(f"Seems like the cats are in love with each other (Cat licks each other)!")
    

# __main__
cat1 = Cat("Badi Billi", "Persian", 50, 100, 0)
cat2 = Cat("Choti Billi", "Persian", 40, 120, 0)

# print(cat1)
# print(cat2)

# print(cat1.meow())
# print(cat2.meow())

cat1.catFight(cat2)
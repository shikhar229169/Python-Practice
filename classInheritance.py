class Zombie:
    def __init__(self, zombieId, name, attributes):
        self.zombieId = zombieId
        self.name = name
        self.attributes = attributes

    def __str__(self):
        return f"Zombie Id: {self.zombieId}, Zombie Name: {self.name}, attributes: {self.attributes}"
    


# ZombieFight class inherits from Zombie class
# To inherit a class, we need to specify the parent class name in the class definition
# So, ZombieFight will be referred to as child class, and Zombie class is parent class for this example
class ZombieFight(Zombie):
    def __init__(self, zombieId, name, attributes, zombiePower, wins, loss):
        self.zombiePower = zombiePower
        self.wins = wins
        self.loss = loss
    
        # Calling the parent class constructor  
        Zombie.__init__(self, zombieId, name, attributes)
    
    # Overriding __str__ method of Zombie class
    def __str__(self):
        return f"Zombie Id: {self.zombieId}, Zombie Name: {self.name}, attributes: {self.attributes}, zombiePower: {self.zombiePower}, wins: {self.wins}, loss: {self.loss}"

    def attack(self, opponentZombie):
        if self.zombiePower > opponentZombie.zombiePower:
            self.wins += 1
            opponentZombie.loss += 1
            self.zombiePower += opponentZombie.zombiePower
            return f"{self.name} won the fight"
        elif self.zombiePower < opponentZombie.zombiePower:
            self.loss += 1
            opponentZombie.wins += 1
            opponentZombie.zombiePower += self.zombiePower
            return f"{opponentZombie.name} won the fight"
        else:
            return "It is a tie! No winner"
        
# Creating ZombieFight object
zombie1 = ZombieFight(1, "Zombie1", "Angry", 100, 0, 0)
zombie2 = ZombieFight(2, "Zombie2", "Furious", 80, 0, 0)

print("Initial Zombie State-")
print(zombie1)
print(zombie2)

print("--------------------------------------------------------------------")

# Calling attack method
attackResult = zombie1.attack(zombie2)
print("Attack Result: ", attackResult)

print("--------------------------------------------------------------------")

# Printing zombie1 and zombie2 objects
print("Final Zombie State-")
print(zombie1)
print(zombie2)
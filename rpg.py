#Big project - RPG
import random

health = 100
defense = 0
attack = 5
chances = [10, 20, 30, 40, 50]
battleMobs = ["dragon", "goblin"]

def dragon():
    DRAGONHEALTH = 300
    DRAGONDEFENSE = 150
    DRAGONATTACK = 40


def battle(mob):
    ans = input("Attack, Heal or Flee? (A/H/F) ")
    if ans == "a" or "A":
        pass
    if ans == "h" or "H":
        pass
    if ans == "f" or "F":
        pass
    else:
        print("Type in a correct answer!")
        battle(random.choice(battleMobs))

def mainloop():
    global health
    global defense
    global attack
    ans2 = input("Explore or Heal? (E/H) ")
    battleChance = random.choice(chances)
    if ans2 == "e" or "E":
        if battleChance == 10:
            mobsChance = random.choice(battleMobs)
            print("You have started a battle against a " + mobsChance)
            battle(mobsChance)
        elif battleChance == 20:
            pass                                            # Token / Coin type currency
    elif ans2 == "h" or "H":
        if health < 100:
            health += 10
            print("You now have " + str(health) + " health")
        else:
            print("You have full health")
    else:
        print("Please choose e or h")





a = True
while True:
    mainloop()
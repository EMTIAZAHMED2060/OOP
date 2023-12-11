class Monster:
    monster_count = 0

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.alive = True
        Monster.monster_count += 1

    @staticmethod
    def monsterCount():
        return Monster.monster_count

    def get_details(self):
        return f"Name: {self.name}\nPower: {self.power}\nAlive: {self.alive}"

    def attack(self, *defenders):
        if not self.alive:
            print(f"Cannot attack. {self.name} is not alive.")
            return

        if not defenders:
            print("No monsters to attack.")
            return

        for defender in defenders:
            if not defender.alive:
                print(f"Cannot attack {defender.name}. It is not alive.")
                continue

            if self.power > defender.power:
                defender.alive = False
                print(f"Attack successful. {self.name} defeated {defender.name}.")
                Monster.monster_count -= 1
            else:
                print(f"Attack unsuccessful. {self.name} was defeated by {defender.name}.")

monster1 = Monster('Godzilla', 40)
monster2 = Monster('Hydra', 30)
monster3 = Monster('KingKong', 50)
print(f"Number of monsters alive:{Monster.monsterCount}")
print('1--------------------------------')
print(monster1.get_details())
print('2--------------------------------')
print(monster2.get_details())
print('3--------------------------------')
print(monster3.get_details())
print('4--------------------------------')
monster1.attack()
print('5--------------------------------')
monster1.attack(monster2)
print('6--------------------------------')
monster1.attack(monster2, monster3)
print('7--------------------------------')
print(f"Number of monsters alive:{Monster.monsterCount}")
print('8--------------------------------')
print(monster2.get_details())
print('9--------------------------------')
monster2.attack(monster1)
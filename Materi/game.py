class Hero:

    def __init__(self, nama, attack, hp, armor):
        self.nama = nama
        self.attack = attack
        self.hp = hp
        self.armor = armor

    def serang(self, lawan):
        print(f"{self.nama} menyerang {lawan.nama}!")
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_power):
        damage = max(0, attack_power - self.armor)
        self.hp = max(0, self.hp - damage)
        print(f"{self.nama} menerima {damage} damage dari {lawan.nama}.")
        print(f"Sisa HP {self.nama}: {self.hp}\n")


hero1 = Hero("Knight", 25, 100, 10)
hero2 = Hero("Archer", 30, 80, 5)
hero3 = Hero("Mage", 35, 70, 3)

hero1.serang(hero2)
hero2.serang(hero3)
hero3.serang(hero1)
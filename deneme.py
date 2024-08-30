import random

# Karakter sınıfı
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        damage_dealt = random.randint(1, self.damage)
        target.health -= damage_dealt
        print(f"{self.name} attacked {target.name} for {damage_dealt} damage.")

    def is_alive(self):
        return self.health > 0

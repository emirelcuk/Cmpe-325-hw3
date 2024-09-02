import random

# Karakter sınıfı
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        # Rastgele bir hasar değeri hesapla
        damage_dealt = random.randint(0, self.damage)
        target.health -= damage_dealt  # Hedefin sağlığından hasar düşülür
        print(f"{self.name} attacked {target.name} for {damage_dealt} damage.")

    def is_alive(self):
        # Karakterin hayatta olup olmadığını kontrol et
        return self.health > 0

# Karakter örnekleri
character1 = Character("Warrior", 100, 20)
character2 = Character("Goblin", 50, 10)

# Karakter saldırı örneği
character1.attack(character2)

# Sağlık durumunu kontrol etme
print(f"{character2.name} is alive: {character2.is_alive()}")

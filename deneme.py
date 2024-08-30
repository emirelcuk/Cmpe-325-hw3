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

# Oyuncu sınıfı
class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15)
        self.inventory = []

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")

    def show_inventory(self):
        if self.inventory:
            print("Inventory:", ", ".join(self.inventory))
        else:
            print("Inventory is empty.")

# Düşman sınıfı
class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

# Oda sınıfı
class Room:
    def __init__(self, name, description, item=None, enemy=None):
        self.name = name
        self.description = description
        self.item = item
        self.enemy = enemy

    def enter(self, player):
        print(f"\nYou have entered the {self.name}.")
        print(self.description)

        if self.item:
            print(f"You found a {self.item}.")
            player.pick_item(self.item)
            self.item = None

        if self.enemy and self.enemy.is_alive():
            print(f"A {self.enemy.name} is here!")
            self.combat(player, self.enemy)

    def combat(self, player, enemy):
        while player.is_alive() and enemy.is_alive():
            action = input("Do you want to (a)ttack or (r)un? ").lower()
            if action == "a":
                player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(player)
            elif action == "r":
                print("You ran away!")
                break
            else:
                print("Invalid action.")

        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")

# Oyun sınıfı
class Game:
    def __init__(self):
        self.player = Player("Hero")
        self.rooms = self.create_rooms()
        self.current_room = 0

    def create_rooms(self):
        rooms = [
            Room("Hall", "A dark and spooky hall.", "sword"),
            Room("Library", "Filled with old books and secrets.", enemy=Enemy("Goblin", 30, 10)),
            Room("Kitchen", "Smells like rotten food.", "shield"),
            Room("Armory", "Old weapons are scattered around.", "armor"),
            Room("Dungeon", "Cold and damp, with chains on the walls.", enemy=Enemy("Orc", 50, 12)),
            Room("Treasure Room", "Glittering with gold and jewels.", "treasure"),
        ]
        return rooms

    def play(self):
        print("Welcome to the Adventure Game!")
        print("Explore the rooms, collect items, and fight enemies.")

        while self.player.is_alive() and self.current_room < len(self.rooms):
            room = self.rooms[self.current_room]
            room.enter(self.player)
            self.current_room += 1

        if self.player.is_alive():
            print("Congratulations! You've completed the adventure!")
        else:
            print("You have been defeated. Game over.")

    def show_status(self):
        print(f"\n{self.player.name}'s Health: {self.player.health}")
        self.player.show_inventory()

# Oyunu başlatan fonksiyon
def start_game():
    game = Game()
    game.play()

if __name__ == "__main__":
    start_game()

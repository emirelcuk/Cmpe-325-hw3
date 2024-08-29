import random
import random
from collections import defaultdict

def markov_chain(text, state_size=2):
    """Builds a Markov chain model from the given text."""
    words = text.split()
    model = defaultdict(list)
    
    for i in range(len(words) - state_size):
        state = tuple(words[i:i + state_size])
        next_word = words[i + state_size]
        model[state].append(next_word)
    
    return model

def generate_sentence(model, state_size=2, length=15):
    """Generates a random sentence from a Markov chain model."""
    state = random.choice(list(model.keys()))
    sentence = list(state)
    
    for _ in range(length - state_size):
        next_words = model.get(state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        sentence.append(next_word)
        state = tuple(sentence[-state_size:])
    
    return ' '.join(sentence)


sample_text = """Artificial intelligence is the simulation of human intelligence processes by machines, 
especially computer systems. These processes include learning, reasoning, and self-correction."""
markov_model = markov_chain(sample_text, state_size=2)


random_sentence = generate_sentence(markov_model, state_size=2, length=10)
print("Generated Sentence:", random_sentence)

def game(game_list):
    health = 10  
    score = 0 
    index1 = 0 
    isim = "emir"
    for x in game_list: 
        if health > 0:
            print("---------------")
            print("Game list:", game_list) 
            friends = list(filter(lambda x: x == 0, game_list))
            enemies = list(filter(lambda x: x == 1, game_list))
            print(f"There are {len(friends)} friends and {len(enemies)} enemies")
            print(f"Your health is {health}")
            print(f"Your score is {score}")
            print("---------------")
            current_item = game_list[index1]
            index1=index1+1
            if current_item == 0:
                print("You see a friend")
            elif current_item == 1:
                print("You see an enemy")
            else:
                print("You see a button")

            print("1 - Interact")
            print("2 - Ignore")

            choice = int(input("What will you do? "))
            if current_item == 0:
                if choice==1:
                    health_gain = random.randint(1, 3)
                    score -= 1
                    health = min(health + health_gain, 10)
            elif current_item == 1:
                if choice==1:
                    health_loss = random.randint(1, 3)
                    score += 1
                    health -= health_loss
            else:  # Button
                button_effect = random.choice(["friend_to_enemy", "enemy_to_friend"])

                if button_effect == "friend_to_enemy":
                    game_list = list(map(lambda x: 1 if x == 0 else x, game_list))
                    print("All friends became enemies!")

                else:
                    game_list = list(map(lambda x: 0 if x == 1 else x, game_list))
                    print("All enemies became friends!")


        if health <= 0:
            print("You died")
            break
    if health>0:
        print("You won")

g_list=input("Enter a list : ")
#   my_list = [random.choice([0, 1, 2]) for _ in range(5)]   this function can be used for creating random list
integer_list=[]
for i in g_list: #user inputs list elements and the elements are converted to int value from char.
    integer_list.append(int(i))
game(integer_list)

def game(game_list):
    health = 10  
    score = 0 
    index1 = 0 
    isim = "emir"
    for x in game_list: 
        if health > 0:
            print("---------------")
            print("Game list:", game_list) 
            friends = list(filter(lambda x: x == 0, game_list))
            enemies = list(filter(lambda x: x == 1, game_list))
            print(f"There are {len(friends)} friends and {len(enemies)} enemies")
            print(f"Your health is {health}")
            print(f"Your score is {score}")
            print("---------------")
            current_item = game_list[index1]
            index1=index1+1
            if current_item == 0:
                print("You see a friend")
            elif current_item == 1:
                print("You see an enemy")
            else:
                print("You see a button")



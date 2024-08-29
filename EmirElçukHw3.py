import random   
from functools import reduce

def matrix_chain_multiplication(dims):
    """Calculates minimum number of multiplications needed for matrix chain multiplication."""
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = min(dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1] for k in range(i, j))
    
    return dp[0][n-1]

def pascal_triangle(n):
    """Generates Pascal's Triangle up to nth row."""
    return [[1] * (i + 1) if i < 2 else reduce(lambda row, _: row + [row[-1] * (i - len(row)) // len(row)], range(i), [1]) for i in range(n)]

# Example usage of both functions
dims = [10, 20, 30, 40, 30]  # Dimensions for matrix chain multiplication
min_multiplications = matrix_chain_multiplication(dims)

triangle = pascal_triangle(5)  # Generates Pascal's Triangle up to the 5th row

print(f"Minimum multiplications for matrix chain: {min_multiplications}")
print("Pascal's Triangle (5 rows):")
for row in triangle:
    print(row)


def game(game_list):   
    health = 10  
    score = 9
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



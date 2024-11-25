import random
import pygame
import math

def main():
    monster_dict = {
        'location': 0,
        "active": False,
        "noise_location": ["left","right","front","behind"]
    }
    while True:
        choice = input(" c: Change location \n q: Quit \n w: Where is monster? \n")
        if choice == "c":
            rand_num = random.uniform(0, 1)
            monster_dict['location'] = move_monster(monster_dict['location'], rand_num)
            print("The monster has moved \n")
        elif choice == "w":
            print(f"Monster is in sector {monster_dict['location']}")
        elif choice == "q":
            break
        else:
            print("Invalid statement")

def move_monster(current_location, rand_num):
    moves={
        0: [(1, 5/10), (2, 5/10)],
        1: [(3, 7/10), (0, 3/10)],
        2: [(0, 2/10), (3, 4/10), (4, 4/10)],
        3: [(2, 4/10), (1, 1/10), (5, 3/10), (7, 3/10), (6, 2/10)],
        4: [(6, 7/10), (2, 3/10)],
        5: [(3, 2/10), (7, 4/10), (4, 4/10)]
    }
    possible_moves = moves.get(current_location)
    
    if not possible_moves:
        return current_location
    cumulative_probability = 0
    for location, prob in possible_moves:
        cumulative_probability += prob
        if rand_num <= cumulative_probability:
            return location
    return current_location

if __name__ == "__main__":
    main()
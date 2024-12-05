import random
import pygame  # type: ignore
import math
import sys

pygame.init()
pygame.font.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cameras Offline")
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Ariel', 40)

options = ["Play", "Quit"]  
user_input = ""
input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 120, 300, 50)
current_menu = "main"
sound_effect = pygame.mixer.Sound('monster_growl.wav')


monster_dict = {
        'location': 0,
        "active": False,
        "noise_location": ['front','behind','left','right']
    }

def draw_menu():
    screen.fill(BLACK)

    title_text = font.render("Cameras Offline", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(title_text, title_rect)

    instructions_text = font.render("Type 'play' to start or 'quit' to exit:" , True, WHITE)
    instructions_rect = instructions_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
    screen.blit(instructions_text, instructions_rect)

    input_surface = font.render(user_input, True, WHITE)
    screen.blit(input_surface, input_rect)

    pygame.display.flip()
def death():
    global current_menu
    screen.fill(BLACK)

    title_text = font.render("You Died", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(title_text, title_rect)

def draw_text():
    global current_menu
    screen.fill(BLACK)

    title_text = font.render("Cameras Offline", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(title_text, title_rect)

    if current_menu == "main":
        instructions_text = font.render("Type: Sound, Shock, Map_view", True, WHITE)
    elif current_menu == "sound_menu":
        instructions_text = font.render("Sound Menu: Type 'back' to return", True, WHITE)
    elif current_menu == "shock_menu":
        instructions_text = font.render("Shock Menu: Type 'back' to return", True, WHITE)
    elif current_menu == "map_menu":
        instructions_text = font.render("Map Menu: Type 'back' to return", True, WHITE)

    instructions_rect = instructions_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
    screen.blit(instructions_text, instructions_rect)

    input_surface = font.render(user_input, True, WHITE)
    screen.blit(input_surface, input_rect)

    pygame.display.flip()


def mainmenu_handle_input():
    global user_input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.lower() == "play":
                    game_loop()
                elif user_input.lower() == "quit":
                    print("Exiting program..")
                    pygame.quit()
                    sys.exit()
                else:
                    user_input = ""
            
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            else:
                user_input += event.unicode

def gamemenu_handle_input(events, screen):
    global monster_dict
    global user_input, current_menu 
    global sound_effect
    action = None

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                action = user_input.lower()
                user_input = ""  
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]  
            else:
                user_input += event.unicode 

    if current_menu == "main":
        if action == "sound":
            current_menu = "sound_menu"  
        elif action == "shock":
            current_menu = "shock_menu" 
        elif action == "map_view":
            current_menu = "map_menu"  
        elif action is not None:
            print(f"Invalid action: {action}")

    elif current_menu == "sound_menu":
        if action == "back":
            current_menu = "main" 
        elif action in [str(num) for num in range(0, 13)]:
            direct = monster_dict["noise_location"]
            num = random.randint(1,3)
            print(direct[num])
            play_sound_direction(monster_dict["location"], action, sound_effect, direct[num] )
    elif current_menu == "shock_menu":
        if action == "back":
            current_menu = "main" 
        elif action in [str(num) for num in range(0, 13)]:
            shock_monster(monster_dict["location"], action)

    elif current_menu == "map_menu":
        if action == "back":
            current_menu = "main" 
    return action 

def game_loop():
    global user_input, current_menu
    start_time = pygame.time.get_ticks()
    global monster_dict
    user_input = ""
    running = True
    clock = pygame.time.Clock()

    while running:
        elapsed_time = pygame.time.get_ticks() - start_time
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gamemenu_handle_input(events, screen) 
        draw_text()

        if elapsed_time > 5000:
            if monster_dict["location"] == 12:
                death()
                pygame.display.flip()
                pygame.time.wait(2000)
                running = False
            else:
                rand_num = random.uniform(0, 1)
                monster_dict['location'] = move_monster(monster_dict['location'], rand_num)
                start_time = pygame.time.get_ticks()
                print(f"Monster is at {monster_dict['location']}")

        pygame.display.flip()
        clock.tick(30)


def move_monster(current_location, rand_num):
    moves = {
        0: [(1, 5/10), (2, 5/10)],
        1: [(3, 7/10), (0, 3/10)],
        2: [(0, 2/10), (3, 4/10), (4, 4/10)],
        3: [(2, 4/10), (1, 1/10), (5, 3/10), (7, 3/10), (6, 2/10)],
        4: [(6, 7/10), (2, 3/10)],
        5: [(3, 2/10), (7, 4/10), (4, 4/10)],
        6: [(3, 2/10), (4, 2/10), (8, 6/10)],
        7: [(3, 1/10), (5, 2/10), (8, 4/10), (9, 3/10)],
        8: [(6, 2/10), (7, 2/10), (11, 6/10)],
        9: [(5, 2/10), (7, 2/10), (10, 6/10)],
        10: [(10, 5/10), (12, 5/10)],
        11: [(11, 5/10), (12, 5/10)]
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

def shock_monster(monster_location, input_location):
    global monster_dict
    if monster_location == int(input_location):
        monster_dict["location"] = 0
        pygame.mixer.Sound('monster_hurt.wav').play()


def play_sound_direction(monster_location, input_location, sound, direction):
    if monster_location == int(input_location):
        if direction == 'left':
            pygame.mixer.Sound('monster_growlL.wav').play()
        elif direction == 'right':
            pygame.mixer.Sound('monster_growR.wav').play()
        elif direction == 'behind':
            sound.set_volume(0.5) 
            sound.play()
        else:
            sound.set_volume(1.0) 
            sound.play()

def main_menu():
    while True:
        draw_menu()
        mainmenu_handle_input()
        pygame.time.Clock().tick(30)
main_menu()

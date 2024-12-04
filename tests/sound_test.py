import time
import pygame # type: ignore

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('computer.mp3')
    pygame.mixer.music.set_volume(0.1) 
    pygame.mixer.music.play(loops=-1, start=0.0)
    sound_effect = pygame.mixer.Sound('door.wav')
    
    while True:
        time.sleep(1)
        choice = input("Enter d for door or q for quit: ").lower()
        if choice == "d":
            compass = input("Which direction: ").lower() 
            if compass in ["left", "right", "front", "behind"]:
                play_sound_direction(sound_effect, compass)
            else:
                print("Invalid input")
        elif choice == "q":
            pygame.mixer.music.stop()
            pygame.quit()
            break
        else:
            print("Invalid input")

def play_sound_direction(sound, direction):
    if direction == 'left':
        pygame.mixer.Sound('doorL.wav').play()
    elif direction == 'right':
        pygame.mixer.Sound('doorR.wav').play()
    elif direction == 'behind':
        sound.set_volume(0.5) 
        sound.play()
    else:
        sound.set_volume(1.0) 
        sound.play()
    

if __name__== "__main__":
    main()



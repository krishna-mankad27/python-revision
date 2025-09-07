import time
import datetime
import pygame

def setalarm(t):
    print(f"alarm set for {t}")
    sound_path = "C:/Users/krishna/Downloads/sound.mp3"
    run = True
    while run :
        now = datetime.datetime.now().strftime("%H:%M:%S")
        
        print(now)
        time.sleep(1) 
        if now == t:
            print("wake up!!")
            run = False
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
if __name__ == "__main__":
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(now)
    alarm = input("enter time (HH:MM:SS): ")
    setalarm(alarm)
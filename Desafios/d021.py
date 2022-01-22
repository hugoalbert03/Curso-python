#TENTATIVA 1
import time
import pygame
print("processando...")
time.sleep(3)
print("Executando :)")
pygame.init()
pygame.mixer.music.load('audio.ogg')
pygame.mixer.music.play()
time.sleep(347)
pygame.event.wait()

#TENTATIVA 2
#from playsound import playsound
#playsound('audio.ogg')

#TENTATIVA 3
#import os
#print(os.getcwd('audio.ogg'))

#TENTATIVA 4
#import playsound
#playsound.playsound('audio.ogg')
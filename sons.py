import pygame
pygame.mixer.init()

pygame.mixer.music.load('son/musique_de_fond.mp3')
pygame.mixer.music.play(-1)

son_joue = False # permet de jouer le son de defait que une fois
son_gambling = pygame.mixer.Sound('son/lets_go_gambling.mp3')
son_fall = pygame.mixer.Sound('son/fall.mp3')
tire_balle = pygame.mixer.Sound('son/balle.mp3')
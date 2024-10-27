import pygame
from random import randint
from objets_et_variables import *
from img import *


fond2 = pygame.image.load('images/casino.jpg').convert()

def dessiner_bouton(fenetre, message:str, x: int, y:int, largeur:int, hauteur:int, couleur_fond:tuple, couleur_texte:tuple, taille:int):
    '''
    Permet de dessiner un bouton.
    Paramètres:
        - fenetre : la fenetre pygame concernée
        - message (str) : Le texte à écrire
        - x (float or int) : la position x du bouton
        - y (float or int) : la position y du bouton
        - largeur (float or int) : la largeur du bouton
        - hauteur (float or int) : la hauteur du bouton
        - couleur_fond (tuple) : la couleur de fond du bouton
        - couleur_texte (tuple) : la couleur du texte du bouton
        - taille (int) : la taille de la police d'écriture
    '''
    pygame.draw.rect(fenetre, couleur_fond, (x, y, largeur, hauteur))
    police = pygame.font.Font('police.ttf', taille)
    texte = police.render(message, True, couleur_texte)
    fenetre.blit(texte, (x + 10, y + (hauteur - texte.get_height()) // 2))


def dessiner_zone_texte(fenetre, rect, texte:str, actif:bool):
    '''
    Permet de dessiner une zone de texte.
    Paramètres:
        - fenetre : la fenetre pygame concernée
        - rect : Le rectangle à dessiner, contenant la position x et y, ainsi que la largeur et la hauteur
        - texte (str) : Le texte à écrire
        - actif (bool) : Le booléen indiquant si le champ est actif (ssi on peut écrire)
    '''
    pygame.draw.rect(fenetre, blanc, rect)
    couleur = gris
    if actif:
        couleur = noir
    pygame.draw.rect(fenetre, couleur, rect, 2)
    police = pygame.font.Font('police.ttf', 25)
    texte_surface = police.render(texte, True, noir)
    fenetre.blit(texte_surface, (rect.x + 5, rect.y + 5))









import pygame
import numpy
from fonctions import *
from Ecrans import Ecran

class Emplacement(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('machine_a_sou/pomme_doree.png') #image par default a changer
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def set_image(self, image):
        self.image = image

class EcranMachineASous:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('machine_a_sou/slot.png')
        self.image_test = pygame.image.load('machine_a_sou/orange.png')
        self.hauteur_emplacement = 150
        self.emplacement_x_milieu = 400/3 + 43
        self.emplacement_x_gauche = self.emplacement_x_milieu - self.image_test.get_width() -10
        self.emplacement_x_droite = self.emplacement_x_milieu + self.image_test.get_width() +8
        self.emplacements = pygame.sprite.Group()
        self.emplacement_gauche = Emplacement(self.emplacement_x_gauche, self.hauteur_emplacement)
        self.emplacement_milieu = Emplacement(self.emplacement_x_milieu, self.hauteur_emplacement)
        self.emplacement_droite = Emplacement(self.emplacement_x_droite, self.hauteur_emplacement)
        # rangement des emplacements dans le groupe
        self.emplacements.add(self.emplacement_gauche)
        self.emplacements.add(self.emplacement_milieu)
        self.emplacements.add(self.emplacement_droite)
    def affiche(self):
        '''
        Permet d'afficher l'écran du mini-jeu Machine à sous.
        '''
        fenetre.fill(blanc)
        fenetre.blit(self.fond, (0, 0))
        self.emplacements.draw(fenetre)
        comic = pygame.font.SysFont("comicsansms", 30)
        text = comic.render(str(joueur1.get_cagnotte()) + " pièces", True, blanc)
        fenetre.blit(text, (10, 0))
        dessiner_bouton(fenetre, "Retour", 340, 20, 50, 50, blanc, noir, 15)
    def lancement(self):
        '''
        Permet de lancer la machine à sous.
        '''
        fruits_dict = {
            "cerise": pygame.image.load('machine_a_sou/cerise.png'),
            "pomme": pygame.image.load('machine_a_sou/pomme.png'),
            "orange": pygame.image.load('machine_a_sou/orange.png'),
            "pasteque": pygame.image.load('machine_a_sou/pasteque.png'),
            "pomme_dore": pygame.image.load('machine_a_sou/pomme_doree.png')
        }
        fruits = ["pomme", "cerise", "orange", "pasteque", "pomme_dore"]
        proba_fruits = [0.2, 0.25, 0.4, 0.12, 0.03]

        fruits_dict_gains = {
            "orange": 500,
            "cerise": 1000,
            "pomme": 2300,
            "pasteque": 4000,
            "pomme_dore": 1000000
        }
        global jetons
        hasard = numpy.random.choice(fruits, 3, p=proba_fruits)
        
        # Récupérer les images directement depuis le dictionnaire
        self.emplacement_gauche.set_image(fruits_dict[hasard[0]])
        self.emplacement_milieu.set_image(fruits_dict[hasard[1]])
        self.emplacement_droite.set_image(fruits_dict[hasard[2]])

        if hasard[0] == hasard[1] == hasard[2]:
            fruit = hasard[0]
            jetons_gagnes = fruits_dict_gains[fruit]
            joueur1.modifier_cagnotte(jetons_gagnes)

ecran_machine_a_sous = EcranMachineASous()
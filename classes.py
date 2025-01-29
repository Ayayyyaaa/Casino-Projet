# classes.py
import pygame
from img import fenetre

print("Chargement de classes.py")

class Joueur:
    def __init__(self, pseudo=''):
        self.pseudo = pseudo
        self.cagnotte = 200000
        self.roulette_active = False
        self.mdp = ' '
        self.code_cb = None
        self.num_cb = None
        self.inventaire = {'Biere' : 0, 'Whisky' : 0}
        self.heros = ['Night Hero']
        self.gains = {'Roulette': 1.0, 'Blackjack': 1.0, 'Pile ou Face': 1.0}
        self.probas = {'Roulette':0,'Blackjack':1.0,'Pile ou Face': 1.0}
    def get_pseudo(self):
        return self.pseudo
    def get_cagnotte(self):
        return self.cagnotte
    def get_roulette_active(self):
        return self.roulette_active
    def get_mdp(self):
        return self.mdp
    def get_code_cb(self):
        return self.code_cb
    def get_num_cb(self):
        return self.num_cb
    def get_heros(self):
        return self.heros
    def get_inventaire(self):
        return self.inventaire
    def get_gains(self):
        return self.gains
    def get_probas(self):
        return self.probas
    def set_pseudo(self, pseudo):
        self.pseudo = pseudo
    def set_cagnotte(self, cagnotte):
        self.cagnotte = cagnotte
    def modifier_cagnotte(self, montant):   
        """
        Permet de modifier la cagnotte à partir d'un montant
        montant(int) : le montant qu'on ajoute à la cagnotte
        """
        self.cagnotte += montant
    def set_roulette_active(self, actif):
        self.roulette_active = actif
    def set_mdp(self, mdp):
        self.mdp = mdp
    def set_code_cb(self, code):
        self.code_cb = code
    def set_num_cb(self, num):
        self.num_cb = num
    def ajouter_inventaire(self,article):
        if article in self.inventaire.keys():
            self.inventaire[article] += 1
        else:
            self.inventaire[article] = 1
    def set_heros(self,heros):
        self.heros = heros
    def ajouter_heros(self,heros):
        self.heros.append(heros)
    def set_inventaire(self,inventaire):
        self.inventaire = inventaire
    def set_gains(self,jeu,gains):
        self.gains[jeu] = gains
    def set_probas(self,jeu,probas):
        self.probas[jeu] = probas


class Coin:
    def __init__(self, pos_x, pos_y):
        self.tourne_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('pieces/coin-1.png.png'))
        self.sprites.append(pygame.image.load('pieces/coin-2.png.png'))
        self.sprites.append(pygame.image.load('pieces/coin-3.png.png'))
        self.sprites.append(pygame.image.load('pieces/coin-4.png.png'))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.actuel_sprite = 0
        self.image = self.sprites[self.actuel_sprite]
    def activer_rotation(self):
        self.tourne_animation = True
    def get_image(self):
        return self.image
    def get_pos(self):
        return(self.pos_x,self.pos_y)
    def update(self, speed):
        '''Permet d'effectuer l'animation de la rotation de la piece.'''
        if self.tourne_animation:
            self.actuel_sprite += speed
            if int(self.actuel_sprite) >= len(self.sprites):
                self.actuel_sprite = 0
        self.image = self.sprites[int(self.actuel_sprite)]


class Bouton:
    def __init__(self, largeur, hauteur, x, y):
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
    def get_largeur(self):
        return self.largeur
    def get_hauteur(self):
        return self.hauteur
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_largeur(self, largeur):
        self.largeur = largeur
    def set_hauteur(self, hauteur):
        self.hauteur = hauteur
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y


class Button:
    def __init__(self, image1, image2, x, y):
        self.image1 = image1 
        self.image2 = image2  
        self.rect = self.image2.get_rect(topleft=(x, y))  # Rectangle pour la position
        self.mask = pygame.mask.from_surface(self.image2)  # Masque pour les collisions 

    def collision(self, souris_pos):
        '''Permet de vérifier si le clic est dans la zone du bouton'''
        # Convertir la position du clic dans le référentiel de l'image du bouton
        x = souris_pos[0] - self.rect.x
        y = souris_pos[1] - self.rect.y

        # Vérifier si le clic est dans le rectangle et dans le masque
        if 0 <= x < self.rect.width and 0 <= y < self.rect.height:
            return self.mask.get_at((x, y))
        return False

    def draw(self, surface, mouse_pos):
        '''Permet de dessiner le bouton et de gérer le changement d'image en fonction du clic'''
        if self.collision(mouse_pos):
            surface.blit(self.image1, self.rect.topleft)
        else:
            surface.blit(self.image2, self.rect.topleft)

    def get_pos(self):
        return (self.rect.x, self.rect.y)

class Clic:
    def __init__(self):
        self.clic = (0,0)
    def get_clic(self):
        return self.clic
    def set_clic(self,clic):
        self.clic = clic

class Curseur:
    def __init__(self):
        self.actif = False
        self.frames = [pygame.image.load(f'images/Inventaire/_a_UI_Flat_Select01a_{i}.png') for i in range(1,5)]
        self.x = 0
        self.y = 0
        self.frame = 0
    def get_actif(self):
        return self.actif
    def get_pos(self):
        return (self.x, self.y)
    def get_frame(self):
        return int(self.frame)
    def set_pos(self, pos):
        self.frame = 0
        self.x = pos[0]
        self.y = pos[1]
    def set_actif(self, actif):
        self.actif = actif
    def update(self, speed):
        if int(self.frame) < len(self.frames)-1:
            self.frame += speed
        fenetre.blit(self.frames[int(self.frame)], (self.x, self.y))

class Biere:
    def __init__(self):
        self.nom = 'Biere'
    def get_nom(self):
        return self.nom
    def boire(self,joueur1):
        joueur1.set_gains('Roulette',0.9)
        joueur1.set_probas('Roulette',-1)

class Whisky:
    def __init__(self):
        self.nom = 'Whisky'
    def get_nom(self):
        return self.nom
    def boire(self,joueur1):
        joueur1.set_gains('Blackjack',1.1)
# classes.py
import pygame


class Joueur:
    def __init__(self, pseudo='Babibel'):
        self.pseudo = pseudo
        self.cagnotte = 200000
        self.roulette_active = False
        self.mdp = None
        self.code_cb = None
        self.num_cb = None
        self.inventaire = {'Chope de Bière' : 0, 'Bouteille de Whisky' : 0}

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
    
    def set_pseudo(self, pseudo):
        self.pseudo = pseudo

    def set_cagnotte(self, cagnotte):
        self.cagnotte = cagnotte

    def modifier_cagnotte(self, montant):   
        """
        permet de modifier la cagnotte à partir d'un montant
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
        self.inventaire[article] += 1


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


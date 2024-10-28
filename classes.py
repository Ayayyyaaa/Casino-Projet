# classes.py
import pygame


class Joueur:
    def __init__(self, pseudo='Babibel', cagnotte=2000, roulette_active=False):
        self.pseudo = pseudo
        self.cagnotte = cagnotte
        self.roulette_active = roulette_active

    def get_pseudo(self):
        return self.pseudo

    def get_cagnotte(self):
        return self.cagnotte

    def get_roulette_active(self):
        return self.roulette_active

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


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.tourne_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('pieces/coin-1.png.png'))
        self.sprites.append(pygame.image.load('pieces/coin-2.png.png'))
        self.sprites.append(pygame.image.load('pieces/coin-3.png.png'))
        self.sprites.append(pygame.image.load('pieces/coin-4.png.png'))

        self.actuel_sprite = 0
        self.image = self.sprites[self.actuel_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def activer_rotation(self):
        self.tourne_animation = True

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


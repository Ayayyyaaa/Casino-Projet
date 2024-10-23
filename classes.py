# classes.py
import pygame
from random import randint



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


class Ecran:
    def __init__(self, actif=False):
        self.actif = actif

    def get_actif(self):
        return self.actif

    def set_actif(self, actif):
        self.actif = actif


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



class Pistolet_blanc(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.tourne_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('pistolet_blanc/vide.png'))
        i = 0
        for i in range(3):
            self.sprites.append(pygame.image.load('pistolet/pf-1.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-2.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-3.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-14.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-4.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-5.png.png'))
        for j in range(1,10):
            self.sprites.append(pygame.image.load(f'pistolet_blanc/pbf-{j}.png'))

        self.actuel_sprite = 0
        self.image = self.sprites[self.actuel_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def activer_rotation(self):
        """
        permet d'activer l'animation de rotation du barillet de la roulette russe
        """
        self.tourne_animation = True

    def desactiver_rotation(self):
        """
        permet de désactiver la rotation du barillet de la roulette russe
        """
        self.tourne_animation = False

    def update(self, speed, joueur):
        """
        permet de jouer l'animation 
        speed(float): la vitesse de l'animation
        joueur(object): l'objet joueur1
        """
        if self.tourne_animation:
            self.actuel_sprite += speed
            if int(self.actuel_sprite) >= len(self.sprites):
                self.actuel_sprite = 0
                joueur.modifier_cagnotte(joueur.get_cagnotte()//2)
                self.tourne_animation = False
        self.image = self.sprites[int(self.actuel_sprite)]



class Pistolet(pygame.sprite.Sprite):   #classe spéciale de pygame pour les objets de jeu
    def __init__(self, pos_x, pos_y, son):
        super().__init__()
        self.tourne_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('pistolet/vide.png'))
        self.son = son
        for i in range(3):
            self.sprites.append(pygame.image.load('pistolet/pf-1.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-2.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-3.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-14.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-4.png.png'))
            self.sprites.append(pygame.image.load('pistolet/pf-5.png.png'))
        for j in range(6,14):
            self.sprites.append(pygame.image.load(f'pistolet/pf-{j}.png.png'))
        

        self.actuel_sprite = 0
        self.image = self.sprites[self.actuel_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def activer_rotation(self):
        """permet d'activer l'animation
        """
        self.tourne_animation = True

    def update(self, speed,joueur):
        """
        permet de jouer l'animation 
        speed(float): la vitesse de l'animation
        joueur(object): l'objet joueur1
        """
        if self.tourne_animation:
            self.actuel_sprite += speed
            if self.actuel_sprite == 21:
                self.son.play()
            if int(self.actuel_sprite) >= len(self.sprites):
                self.actuel_sprite = 0
                joueur.set_cagnotte(0)
                self.tourne_animation = False
        self.image = self.sprites[int(self.actuel_sprite)]


class Emplacement(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('machine_a_sou/pomme_doree.png') #image par default a changer
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def set_image(self, image):
        self.image = image

class Piece:
    def __init__(self):
        self.cote = None
        self.choix = None

    def get_cote(self):
        return self.cote

    def get_choix(self):
        return self.choix

    def set_cote(self,cote):
        self.cote = cote

    def set_choix(self, choix):
        self.choix = choix

    def victoire(self):
        """
        permet de determiner si le joueur a gagné
        """
        if self.get_cote() == self.get_choix():
            return True
        else:
            return False


class Pile_ou_face(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('pistolet_blanc/vide.png'))
        for j in range(1,17):
            self.sprites.append(pygame.image.load(f'Pile_ou_face/Piece animation ({j}).png'))
        self.sprites.append(pygame.image.load(f'Pile_ou_face/Piece animation (1).png'))

        self.actuel_sprite = 0
        self.image = self.sprites[self.actuel_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y-100]

    def activer_animation(self):
        """
        permet d'activer l'animation
        """
        self.animation = True

    def desactiver_animation(self):
        """
        permet de desactiver l'animation
        """
        self.animation = False

    def pile_ou_face(self):
        """
        permet de randomiser le coté de la piece
        """
        cote = randint(1, 2)
        if cote == 1:
            piece.set_cote('Face')
        else:
            piece.set_cote('Pile')

    def update(self, speed, joueur, piece):
        """
        permet de jouer l'animation 
        speed(float): la vitesse de l'animation
        joueur(object): l'objet joueur1
        pièce(objet): aled la docu cest chiant quand y a enormement de def aleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeed
        """
        if self.animation:
            self.actuel_sprite += speed
            if int(self.actuel_sprite) >= len(self.sprites):
                self.actuel_sprite = 0
                self.pile_ou_face()
                if piece.victoire():
                    print(piece.get_choix(), piece.get_cote())
                    print('vict')
                    piece.set_choix(None) 
                    joueur.modifier_cagnotte(100)
                else:
                    joueur.modifier_cagnotte(-100)
                    print('def')
                    print(piece.get_choix(), piece.get_cote())
                self.animation = False
        self.image = self.sprites[int(self.actuel_sprite)]

piece = Piece()
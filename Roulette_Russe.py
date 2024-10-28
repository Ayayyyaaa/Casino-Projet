import pygame
from random import randint
from sons import tire_balle


class RouletteRusse:
    def __init__(self, pos_x, pos_y,son):
        self.tourne_animation_vict = False
        self.tourne_animation_def = False
        self.sprites_vict = []
        self.sprites_def = []
        self.frame = 0
        self.son = son
        self.sprites_vict.append(pygame.image.load('pistolet_blanc/vide.png'))
        self.sprites_def.append(pygame.image.load('pistolet_blanc/vide.png'))
        i = 0
        for i in range(3):
            self.sprites_vict.append(pygame.image.load('pistolet/pf-1.png.png'))
            self.sprites_vict.append(pygame.image.load('pistolet/pf-2.png.png'))
            self.sprites_vict.append(pygame.image.load('pistolet/pf-3.png.png'))
            self.sprites_vict.append(pygame.image.load('pistolet/pf-13.png.png'))
            self.sprites_vict.append(pygame.image.load('pistolet/pf-4.png.png'))
            self.sprites_vict.append(pygame.image.load('pistolet/pf-5.png.png'))
        for j in range(1,10):
            self.sprites_vict.append(pygame.image.load(f'pistolet_blanc/pbf-{j}.png'))
        for i in range(3):
            self.sprites_def.append(pygame.image.load('pistolet/pf-1.png.png'))
            self.sprites_def.append(pygame.image.load('pistolet/pf-2.png.png'))
            self.sprites_def.append(pygame.image.load('pistolet/pf-3.png.png'))
            self.sprites_def.append(pygame.image.load('pistolet/pf-13.png.png'))
            self.sprites_def.append(pygame.image.load('pistolet/pf-4.png.png'))
            self.sprites_def.append(pygame.image.load('pistolet/pf-5.png.png'))
        for j in range(6,14):
            self.sprites_def.append(pygame.image.load(f'pistolet/pf-{j}.png.png'))

        self.actuel_sprite = 0
        self.image = self.sprites_def[self.actuel_sprite]
        self.pos_x = pos_x
        self.pos_y = pos_y

    def rouletterusse(self,joueur1):
        '''
        Permet de déterminer quelle balle sort du pistolet, puis active l'animation du pistolet (mort) ou celle du pistolet_blanc (victoire)
        '''
        if joueur1.get_roulette_active():
            proba = 1
            if joueur1.get_cagnotte() > 800000:
                proba = 5
            elif joueur1.get_cagnotte() > 500000:
                proba = 4
            elif joueur1.get_cagnotte() > 100000:
                proba = 3
            elif joueur1.get_cagnotte() > 50000:
                proba = 2
            else:
                proba = 1
            balle = randint(1, 6)
            if balle <= proba: 
                self.activer_rotation_def()
            else:  
                self.activer_rotation_vict()


    def activer_rotation_vict(self):
        """
        permet d'activer l'animation de rotation du barillet de la roulette russe
        """
        self.tourne_animation_vict = True

    def desactiver_rotation_vict(self):
        """
        permet de désactiver la rotation du barillet de la roulette russe
        """
        self.tourne_animation_vict = False

    def activer_rotation_def(self):
        """
        permet d'activer l'animation de rotation du barillet de la roulette russe
        """
        self.tourne_animation_def = True

    def desactiver_rotation_def(self):
        """
        permet de désactiver la rotation du barillet de la roulette russe
        """
        self.tourne_animation_def = False

    def update_vict(self, speed, joueur):
        """
        permet de jouer l'animation de victoire
        speed(float): la vitesse de l'animation
        joueur(object): l'objet joueur1
        """
        if self.tourne_animation_vict:
            self.actuel_sprite += speed
            if int(self.actuel_sprite) >= len(self.sprites_vict):
                self.actuel_sprite = 0
                joueur.modifier_cagnotte(joueur.get_cagnotte()//2)
                self.tourne_animation_vict = False
            self.image = self.sprites_vict[int(self.actuel_sprite)]
        

    def update_def(self, speed, joueur):
        """
        permet de jouer l'animation  de defaite
        speed(float): la vitesse de l'animation
        joueur(object): l'objet joueur1
        """
        if self.tourne_animation_def:
            self.actuel_sprite += speed
            if self.actuel_sprite == 21:
                self.son.play()
            if int(self.actuel_sprite) >= len(self.sprites_def):
                self.actuel_sprite = 0
                joueur.set_cagnotte(0)
                self.tourne_animation_def = False
            self.image = self.sprites_def[int(self.actuel_sprite) % len(self.sprites_def)]


    def get_image(self):
        return self.image
    def get_pos(self):
        return(self.pos_x,self.pos_y)

pistolet = RouletteRusse(110, 120, tire_balle)


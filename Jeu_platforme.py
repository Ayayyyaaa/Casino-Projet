import pygame
from objets_et_variables import *
import sys

class Voiture:
    def __init__(self):
        self.x = 40
        self.y = 600
        self.saut = False
        self.cd = False
        self.sprites = [pygame.image.load(f'Jeu_platforme/Voiture/_a_frm{i},40.png').convert_alpha() for i in range(4)]
        self.sprites_saut = [pygame.image.load(f'Jeu_platforme/Voiture/Saut/_a_frm{i},40.png').convert_alpha() for i in range(3)]
        self.frame = 0
        self.speed = 0.45
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_frame(self):
        return int(self.frame)
    def get_sprites(self):
        return self.sprites
    def get_saut(self):
        return self.saut
    def set_cd(self, cd):
        self.cd = cd
    def get_cd(self):
        return self.cd
    def set_frame(self, frame):
        self.frame = frame
    def set_saut(self, saut):
        self.saut = saut
    def set_y(self,y):
        self.y = y
    def get_sprites_saut(self):
        return self.sprites_saut
    def anim(self):
        self.frame += self.speed
        if int(self.frame) >= len(self.sprites):
            self.frame = 0
    def anim_saut(self):
        self.frame += self.speed
        if int(self.frame) >= len(self.sprites_saut):
            self.frame = 0

class Pique:
    def __init__(self,img='Jeu_platforme/Obs/pic.png'):
        self.x = 1600
        self.y = 600
        self.actif = False
        self.img = pygame.image.load(img).convert_alpha()
        self.mask = pygame.mask.from_surface(self.img)
    def get_actif(self):
        return self.actif
    def set_actif(self,actif):
        self.actif = actif
    def get_y(self):
        return self.y
    def get_x(self):
        return self.x
    def modif_x(self,x):
        self.x = x
    def affiche(self):
        fenetre.blit(self.img, (self.x, self.y))
    def get_mask(self):
        return self.mask

class Decor:
    def __init__(self,h,img='Jeu_platforme/Decor/pente1.png'):
        self.x = 1600
        self.y = 600
        self.hauteur = h
        self.actif = False
        self.img = pygame.image.load(img).convert_alpha()
        self.mask = pygame.mask.from_surface(self.img)
    def get_actif(self):
        return self.actif
    def set_actif(self,actif):
        self.actif = actif
    def get_y(self):
        return self.y
    def get_x(self):
        return self.x
    def get_hauteur(self):
        return self.hauteur
    def modif_x(self,x):
        self.x = x
    def affiche(self):
        fenetre.blit(self.img, (self.x, self.y))
    def get_mask(self):
        return self.mask
    def get_img(self):
        return self.img
        
class BabelRace:
    def __init__(self):
        self.fond = pygame.image.load('images/arene.png').convert_alpha()
        self.run = False
        self.reussi = False
        self.fond_x = 0
        self.sol = 600
        self.x_simule = 40
    def actif(self, etat):
        self.run = etat
    def get_actif(self):
        return self.run
    def def_sol(self, img, x, obj,h,s): 
        sol = 600 # Niveau de sol initial
        image_rect = img.get_rect(topleft=(obj.get_x(), obj.get_y()))
        relative_x = x - image_rect.x

        if 0 <= relative_x < image_rect.width:
            top_y = None

            for y in range(image_rect.height):
                pixel = img.get_at((relative_x, y))
                if pixel.a > 0:  # Vérification de la transparence
                    if top_y is None:
                        top_y = y
                    if top_y is not None:
                        # Calculer la hauteur par rapport au bas de la pente
                        hauteur_surface = image_rect.y + top_y
                        return hauteur_surface-h  # Si un point est trouvé, retourner la hauteur de la surface

        if s < sol:
            return s+5
        else:
            return sol  # Si aucun point n'est trouvé, retourner le sol par défaut
        
    def lancer(self):
        self.largeur, self.hauteur = 1700, 700
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.clock = pygame.time.Clock()
        self.x_simule = 0
        self.pentes={pente1:200, pente2:1050}
        while self.run:
            fenetre.fill((0, 0, 0))
            self.x_simule += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        voiture.set_frame(0)
                        voiture.set_saut(True)
            if voiture.get_saut():
                voiture.set_y(voiture.get_y() - 7)
                if voiture.get_y() < self.sol-240:
                    voiture.set_saut(False)
                    voiture.set_cd(True)
            elif voiture.get_y() <= self.sol:
                voiture.set_y(voiture.get_y() + 5)
            else:
                voiture.set_cd(False)
            if self.x_simule >= 100:
                pic1.set_actif(True)
            
            if pic1.get_actif():
                pic1.modif_x(pic1.get_x() - 10)
                pic1.affiche()
                if pic1.get_x() <= -100:
                    pic1.set_actif(False)
                    pic1.modif_x(4500)
                    pic1.set_actif(True)
            for pente, pos in self.pentes.items():
                if self.x_simule >= pos:
                    pente.set_actif(True)
                if pente.get_actif():
                    pente.modif_x(pente.get_x() - 10)
                    pente.affiche()
                    if pente.get_x() <= -800:
                        pente.set_actif(False)
                    # Calculer la hauteur une seule fois
                    hauteur_surface = self.def_sol(pente.get_img(), voiture.get_x(), pente, 90,self.sol)
                    if hauteur_surface is not None:
                        self.sol = hauteur_surface
                        if not voiture.get_saut() and not voiture.get_cd():
                            voiture.set_y(self.sol)
            if voiture.get_saut():
                voiture.anim_saut()
                image = voiture.get_sprites_saut()[voiture.get_frame()]
            else:
                voiture.anim()
                image = voiture.get_sprites()[voiture.get_frame()]
            mask = pygame.mask.from_surface(image)
            offset_x = voiture.get_x() - pic1.get_x()
            offset_y = voiture.get_y() - pic1.get_y()
            mask_overlap = mask.overlap(pic1.get_mask(), (-offset_x, -offset_y))
            fenetre.blit(image,(voiture.get_x(),voiture.get_y()))
            clock.tick(60)
            fenetre.blit(souris, pygame.mouse.get_pos())
            pygame.display.flip()

babelrace = BabelRace()
voiture = Voiture()
pic1 = Pique()
pente1 = Decor(90)
pente2 = Decor(90)
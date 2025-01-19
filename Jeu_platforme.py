import pygame
from objets_et_variables import *
import sys

print("Chargement du jeu de platforme...")

#-------Niveau 1------#
def decor_niveau1():
    pente1 = Decor(90,1600,625,'Sol')
    pente2 = Decor(90,1600,625,'Sol')
    platforme1 = Decor(40,1280,470,'Platforme','Jeu_platforme/decor/platforme.png')
    platforme2 = Decor(20,600,500,'Platforme','Jeu_platforme/decor/platforme2.png')
    return {pente1:200, pente2:800, platforme1:400, platforme2:180}

def obs_niveau1():
    pic1 = Pique(1600,625)
    pic2 = Pique(1600,450)
    pic3 = Pique(1600,625)
    return {pic1:200, pic2:250, pic3:600}

#---------Fin---------#

class Voiture:
    def __init__(self):
        self.x = 40
        self.y = 625
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
    def __init__(self,x,y,img='Jeu_platforme/Obs/pic.png'):
        self.x = x
        self.y = y
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
    def __init__(self,h,x,y,typee,img='Jeu_platforme/Decor/pente1.png'):
        self.x = x
        self.y = y
        self.hauteur = h
        self.actif = False
        self.img = pygame.image.load(img).convert_alpha()
        self.mask = pygame.mask.from_surface(self.img)
        self.typee = typee
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
    def get_typee(self):
        return self.typee
        
class BabelRace:
    def __init__(self):
        self.fond = pygame.image.load('images/arene.png').convert_alpha()
        self.run = False
        self.reussi = False
        self.fond_x = 0
        self.sol = 625
        self.sol2 = 500
        self.x_simule = 40
        self.pentes = decor_niveau1()
        self.obs = obs_niveau1()
    def actif(self, etat):
        self.run = etat
    def get_actif(self):
        return self.run
    def def_sol(self, img, x:int, obj,hauteur_img:int,sol:int) -> int: 
        '''Permet de déterminer la hauteur de l'image et donc le niveau du sol
        Paramètres : 
            - img : Surface sur laquelle on cherche le sol
            - x (int): Position de l'image sur laquelle on cherche le sol
            - obj : Objet sur lequel on cherche le sol
            - hauteur_img (int): Hauteur de l'image
            - sol (int): Niveau du sol initial
        Returns :
            - La hauteur de l'image sur laquelle on cherche le sol
        '''
        assert isinstance(img, pygame.Surface), "L'argument img doit être une surface"
        sol_initial = 625 # Niveau de sol initial
        image_rect = img.get_rect(topleft=(obj.get_x(), obj.get_y()))
        relative_x = x - image_rect.x

        if 0 <= relative_x < image_rect.width:
            img_y = None

            for y in range(image_rect.height):
                pixel = img.get_at((relative_x, y))
                if pixel.a > 0:  # Vérification de la transparence
                    if img_y is None:
                        img_y = y
                    if img_y is not None:
                        # Calculer la hauteur par rapport au bas de la pente
                        hauteur_surface = image_rect.y + img_y
                        return hauteur_surface-hauteur_img  # Si un point est trouvé, retourner la hauteur de la surface

        if sol < sol_initial:
            return sol + 3
        else:
            return sol  # Si aucun point n'est trouvé, retourner le sol par défaut
        
    def lancer(self):
        '''Lancement du jeu
        - plat (bool) : Présence d'une platforme, et donc d'un potentiel 2e sol
        - hauteur_surface (int) : Hauteur de la surface sur laquelle on cherche le sol'''
        self.largeur, self.hauteur = 1700, 700
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.clock = pygame.time.Clock()
        self.x_simule = 0
        plat = False
        hauteur_surface = None
        for decor in self.pentes.keys():
            decor.set_actif(False)
        for obs in self.obs.keys():
            obs.set_actif(False)
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
                if hauteur_surface:
                    print(voiture.get_y(),hauteur_surface)
                if plat and voiture.get_y() >= hauteur_surface - 5:  
                    voiture.set_cd(False)
                    voiture.set_y(hauteur_surface + 15) 
                else:
                    voiture.set_y(voiture.get_y() + 5)
            else:
                voiture.set_cd(False)
            for decor, pos in self.pentes.items():
                if self.x_simule >= pos:
                    decor.set_actif(True)
                if decor.get_actif():
                    decor.modif_x(decor.get_x() - 10)
                    decor.affiche()
                    if decor.get_x() <= -800:
                        decor.set_actif(False)
                        
                    hauteur_surface = self.def_sol(decor.get_img(), voiture.get_x(), decor, decor.get_hauteur(), self.sol)
                    
                    if hauteur_surface is not None:
                        if decor.get_typee() == 'Sol':
                            self.sol = hauteur_surface
                            if not voiture.get_saut() and not voiture.get_cd():
                                voiture.set_y(self.sol)
                        elif decor.get_typee() == 'Platforme':
                            # Vérifier si la voiture est au-dessus de la plateforme
                            voiture_bottom = voiture.get_y() + voiture.get_sprites()[0].get_height()
                            plateforme_top = hauteur_surface
                            
                            if (voiture.get_x() + voiture.get_sprites()[0].get_width() > decor.get_x() and voiture.get_x() < decor.get_x() + decor.get_img().get_width()):
                                
                                # Si la voiture tombe sur la plateforme
                                if voiture_bottom >= plateforme_top and voiture.get_y() < plateforme_top:
                                    if not voiture.get_saut():
                                        plat = True
                                        self.sol2 = hauteur_surface
                                        voiture.set_y(plateforme_top - voiture.get_sprites()[0].get_height() + decor.get_hauteur())
                                else:
                                    # Si la voiture n'est pas sur la plateforme
                                    plat = False
                            else:
                                plat = False

            if voiture.get_saut():
                voiture.anim_saut()
                image = voiture.get_sprites_saut()[voiture.get_frame()]
            else:
                voiture.anim()
                image = voiture.get_sprites()[voiture.get_frame()]
            mask = pygame.mask.from_surface(image)
            for obs,pos in self.obs.items():
                if self.x_simule >= pos and not obs.get_actif():
                    obs.set_actif(True)
                if obs.get_actif():
                    obs.modif_x(obs.get_x() - 10)
                    obs.affiche()
                    if obs.get_x() <= -100:
                        obs.set_actif(False)
                    offset_x = voiture.get_x() - obs.get_x()
                    offset_y = voiture.get_y() - obs.get_y()
                    mask_overlap = mask.overlap(obs.get_mask(), (-offset_x, -offset_y))
                    if mask_overlap:
                        self.run = False
                    
            
            fenetre.blit(image,(voiture.get_x(),voiture.get_y()))
            clock.tick(60)
            fenetre.blit(souris, pygame.mouse.get_pos())
            pygame.display.flip()
        joueur1.set_cagnotte(joueur1.get_cagnotte()/4)
        pygame.display.set_mode((400,400))
        self.actif(False)
        
voiture = Voiture()
babelrace = BabelRace()
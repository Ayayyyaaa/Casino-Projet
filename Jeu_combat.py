import pygame
import sys
import time
from objets_et_variables import *

fond_combat = pygame.image.load('images/enfer.jpg').convert()
mort_boss = [f'Boss/Mort/Mort{i}.png' for i in range(1,8)]
marche_boss_gauche = [f'Boss/Marche/Gauche/Marche{i}.png' for i in range(1,8)]
marche_boss_droite = [f'Boss/Marche/Droite/Marche{i}.png' for i in range(1,8)]
attaque1_boss = [f'Boss/Attaque1/Coup_de_poing{i}.png' for i in range(1,5)]
attaque2_boss = [f'Boss/Attaque2/Faux{i}.png' for i in range(1,8)]
inaction_boss = [f'Boss/Inaction/Inaction{i}.png' for i in range(1,4)]
ulti_boss = [f'Boss/ulti/ulti ({i}).png' for i in range(1,7)]

marche_hero_droite = [f'Hero/Marche/Droite/Hero_course{i}.png' for i in range(1,7)]
marche_hero_gauche = [f'Hero/Marche/Gauche/Hero_course{i}.png' for i in range(1,7)]
attaque_hero_img = [f'Hero/Attaque/Attaque{i}.png' for i in range(1,13)]
degats_hero_img = [f'Hero/Degats/degats{i}.png' for i in range(1,4)]
mort_hero_img = [f'Hero/Mort/_afrm{i},70.png' for i in range(1,23)]

class Boss:
    def __init__(self,img):
        self.image = pygame.image.load(img)
        self.pv = 100
        self.pos_x = 1000
        self.pos_y = 470
        self.cd_img = 0
        self.attaque1_dispo = True
        self.attaque2_dispo = True
        self.cd_attaque1 = 0
        self.cd_attaque2 = 0
        self.victoire = False
        self.cd_ulti = 0
    def get_pv(self):
        return self.pv
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    def get_cd_attaque1(self):
        return time.time() - self.cd_attaque1
    def get_attaque1_dispo(self):
        return self.attaque1_dispo
    def get_cd_attaque2(self):
        return time.time() - self.cd_attaque2
    def get_attaque2_dispo(self):
        return self.attaque2_dispo
    def get_victoire(self):
        return self.victoire
    def get_cd_ulti(self):
        return self.cd_ulti
    def modif_pv(self, nb):
        self.pv += nb
    def modif_pos_x(self, nb):
        self.pos_x += nb
    def modif_pos_y(self, nb):
        self.pos_y += nb
    def modif_img(self, img):
        self.image = pygame.image.load(img)
    def set_cd_img(self):
        self.cd_img = time.time()
    def set_cd_attaque1(self):
        self.cd_attaque1 = time.time()
    def set_attaque1_dispo(self, dispo):
        self.attaque1_dispo = dispo
    def set_cd_attaque2(self):
        self.cd_attaque2 = time.time()
    def set_attaque2_dispo(self, dispo):
        self.attaque2_dispo = dispo
    def set_victoire(self, vict):
        self.victoire = vict
    def set_cd_ulti(self, montant):
        self.cd_ulti = montant

class Hero:
    def __init__(self,img):
        self.image = pygame.image.load(img)
        self.pv = 100
        self.pos_x = 50
        self.pos_y = 540
        self.cd_img = 0
        self.attaque = False
        self.degats_subis = False
        self.victoire = False
    def get_pv(self):
        return self.pv
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    def get_attaque(self):
        return self.attaque
    def get_degats_subis(self):
        return self.degats_subis
    def get_victoire(self):
        return self.victoire
    def modif_pv(self, nb):
        self.pv += nb
    def modif_pos_x(self, nb):
        self.pos_x += nb
    def modif_pos_y(self, nb):
        self.pos_y += nb
    def set_attaque(self, actif):
        self.attaque = actif
    def modif_img(self, img):
        self.image = pygame.image.load(img)
    def set_cd_img(self):
        self.cd_img = time.time()
    def set_degats_subis(self, degats_subis):
        self.degats_subis = degats_subis
    def set_victoire(self):
        self.victoire = True
    
class JeuCombat:
    def __init__(self):
        self.boss = Boss(mort_boss[0])
        self.hero = Hero(marche_hero_droite[0])
        self.boss_sprite_marche = 0
        self.boss_sprite_attaque1 = 0
        self.boss_sprite_attaque2 = 0
        self.boss_sprite_inaction = 0
        self.boss_sprite_mort = 0
        self.boss_sprite_ulti = 0
        self.ulti_anim = False
        self.atk1 = False
        self.atk2 = False
        self.hero_sprite_marche = 0
        self.hero_sprite_attaque = 0
        self.hero_sprite_degats = 0
        self.hero_sprite_mort = 0
        self.reussi = False
        self.run = False

    def actif(self, etat):
        self.run = etat

    def get_actif(self):
        return self.run
    
    def set_reussi(self):
        self.reussi = True

    def get_reussi(self):
        return self.reussi

    def attaque_hero(self,speed):
        if self.hero_sprite_attaque == 10:
            if self.hero.get_pos_x()-120 < self.boss.get_pos_x() < self.hero.get_pos_x() + 120:
                self.boss.modif_pv(-20)
                print(self.boss.get_pv())
        elif int(self.hero_sprite_attaque) == len(attaque_hero_img)-1:
            self.hero_sprite_attaque = 0
            self.hero.set_attaque(False)
        self.hero_sprite_attaque += speed
        self.hero.modif_img(attaque_hero_img[int(self.hero_sprite_attaque)])

    def anim_mort_hero(self,speed):
        if not self.boss.get_victoire():
            self.hero_sprite_mort += speed
            self.hero.modif_img(mort_hero_img[int(self.hero_sprite_mort)])
            if int(self.hero_sprite_mort) == len(mort_hero_img)-1:
                self.hero_sprite_mort = 0
                print("Défaite")
                self.boss.set_victoire(True)

    def animation_marche_hero_droite(self,speed):
        self.hero_sprite_marche += speed
        self.hero.modif_img(marche_hero_droite[int(self.hero_sprite_marche)])
        if int(self.hero_sprite_marche) == len(marche_hero_droite)-1:
            self.hero_sprite_marche = 0

    def animation_marche_hero_gauche(self,speed):
        self.hero_sprite_marche += speed
        self.hero.modif_img(marche_hero_gauche[int(self.hero_sprite_marche)])
        if int(self.hero_sprite_marche) == len(marche_hero_gauche)-1:
            self.hero_sprite_marche = 0

    def degats_hero(self,speed):
        self.hero_sprite_degats += speed
        self.hero.modif_img(degats_hero_img[int(self.hero_sprite_degats)])
        if int(self.hero_sprite_degats) == len(degats_hero_img)-1:
            self.hero_sprite_degats = 0
            self.hero.set_degats_subis(False)

    def anim_mort_boss(self,speed):
        if not self.hero.get_victoire():
            self.boss_sprite_mort += speed
            self.boss.modif_img(mort_boss[int(self.boss_sprite_mort)])
            if int(self.boss_sprite_mort) == len(mort_boss)-1:
                print("victoire")
                self.hero.set_victoire()
    
    def animation_attaque1_boss(self,speed):
        self.boss_sprite_attaque1 += speed
        self.atk1 = True
        self.boss.modif_img(attaque1_boss[int(self.boss_sprite_attaque1)])
        if int(self.boss_sprite_attaque1) == len(attaque1_boss)-1:
            if self.boss.get_pos_x()+120 > self.hero.get_pos_x() > self.hero.get_pos_x() - 120 and self.hero.get_pos_y() > 250:
                self.hero.modif_pv(-5)
                self.hero.set_degats_subis(True)
                print(f'Attaque coup de poing : Pv hero {self.hero.get_pv()}')
            self.boss_sprite_attaque1 = 0
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False

    def animation_attaque2_boss(self,speed):
        self.atk2= True
        self.boss_sprite_attaque2 += speed
        self.boss.modif_img(attaque2_boss[int(self.boss_sprite_attaque2)])
        if int(self.boss_sprite_attaque2) == len(attaque2_boss)-1:
            if self.boss.get_pos_x()+120 > self.hero.get_pos_x() > self.boss.get_pos_x() - 120 and self.hero.get_pos_y() > 250:
                self.hero.modif_pv(-15)
                self.hero.set_degats_subis(True)
                print(f'Attaque faux : Pv hero : {self.hero.get_pv()}')
            self.boss_sprite_attaque2 = 0
            self.atk2 = False
            self.boss.set_cd_attaque2()
            self.boss.set_attaque2_dispo(False)

    def animation_marche_boss_gauche(self,speed):
        self.boss_sprite_marche += speed
        self.boss.modif_img(marche_boss_gauche[int(self.boss_sprite_marche)])
        if int(self.boss_sprite_marche) == len(marche_boss_gauche)-1:
            self.boss_sprite_marche = 0

    def animation_marche_boss_droite(self,speed):
        self.boss_sprite_marche += speed
        self.boss.modif_img(marche_boss_droite[int(self.boss_sprite_marche)])
        if int(self.boss_sprite_marche) == len(marche_boss_droite)-1:
            self.boss_sprite_marche = 0

    def animation_inaction_boss(self,speed):
        self.boss_sprite_inaction += speed
        self.boss.modif_img(inaction_boss[int(self.boss_sprite_inaction)])
        if int(self.boss_sprite_inaction) == len(inaction_boss)-1:
            self.boss_sprite_inaction = 0

    def animation_ulti_boss(self,speed):
        self.boss_sprite_ulti += speed
        self.boss.modif_img(ulti_boss[int(self.boss_sprite_ulti)])
        if int(self.boss_sprite_ulti) == len(ulti_boss)-1:
            self.boss.modif_pv(30)
            self.hero.modif_pv(-30)
            print(self.boss.get_pv())
            self.boss_sprite_ulti = 0
            self.boss.set_cd_ulti(0)
            self.ulti_anim = False

    def patern_boss(self):
        if self.boss.get_pv() <= 30:
            print(time.time()-self.boss.get_cd_ulti())
            # Gestion de la guérison du boss à faible PV
            if self.boss.get_cd_ulti() == 0:
                self.boss.set_cd_ulti(time.time())
            elif time.time() - self.boss.get_cd_ulti() > 7:
                self.ulti_anim = True
                print("help")
                if self.boss.get_pos_x() < 900:
                    self.animation_marche_boss_droite(0.1)
                    self.boss.modif_pos_x(1.2)
                else:
                    self.animation_ulti_boss(0.06)
        # Si le boss se trouve à portée, lancement des attaques
        if not self.ulti_anim:
            if self.hero.get_pos_x() - 80 < self.boss.get_pos_x() < self.hero.get_pos_x() + 100:
                if self.boss.get_attaque1_dispo() and not self.atk2:
                    self.animation_attaque1_boss(0.1)
                elif self.boss.get_attaque2_dispo() and not self.atk1:
                    self.animation_attaque2_boss(0.12)
                else:
                    # Si aucune attaque n'est disponible, lance une animation d'inaction
                    self.animation_inaction_boss(0.1)
            else:
                # Sinon, déplacement pour être à portée du héros
                self.boss_vers_hero()

    def boss_vers_hero(self):
        if self.hero.get_pos_x() - 80 < self.boss.get_pos_x():
            self.animation_marche_boss_gauche(0.1)
            self.boss.modif_pos_x(-1.2)
        elif self.hero.get_pos_x() + 100 > self.boss.get_pos_x():
            self.animation_marche_boss_droite(0.1)
            self.boss.modif_pos_x(1.2)


    def lancer(self):
        # Boucle principale du jeu
        self.largeur, self.hauteur = 1200, 700
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.clock = pygame.time.Clock()
        self.boss.modif_pv(-self.boss.get_pv()+100)
        self.hero.modif_pv(-self.hero.get_pv()+100)
        self.boss.modif_pos_x(-self.boss.get_pos_x()+1000)
        self.hero.modif_img(marche_hero_droite[0])
        while not self.hero.get_victoire() and not self.boss.get_victoire() and self.run:
            self.fenetre.fill((0,0,0))
            #self.fenetre.blit(fond_combat, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        self.hero.set_attaque(True)

            if not self.boss.get_pv() <= 0:
                if self.hero.get_pv() > 0:
                    self.patern_boss()
                else:
                    self.animation_inaction_boss(0)
            else:
                self.anim_mort_boss(0.1)

            if self.hero.get_pv() <= 0:
                self.anim_mort_hero(0.1)

            if self.hero.get_attaque():
                self.attaque_hero(0.25)
            keys = pygame.key.get_pressed()
            if not self.hero.get_attaque() and not self.hero.get_pv() <= 0:
                if keys[pygame.K_LEFT]:
                    if self.hero.get_pos_x() > 0:
                        self.hero.modif_pos_x(-5)
                    self.animation_marche_hero_gauche(0.2)
                if keys[pygame.K_RIGHT]:
                    if self.hero.get_pos_x() < 1000:
                        self.hero.modif_pos_x(5)
                    self.animation_marche_hero_droite(0.2)

            if self.boss.get_cd_attaque1() > 1.5:
                self.boss.set_attaque1_dispo(True)
            if self.boss.get_cd_attaque2() > 4:
                self.boss.set_attaque2_dispo(True)
            if self.hero.get_degats_subis():
                self.degats_hero(0.4)

            self.fenetre.blit(self.boss.image, (self.boss.get_pos_x(), self.boss.get_pos_y()))
            self.fenetre.blit(self.hero.image, (self.hero.get_pos_x(), self.hero.get_pos_y()))
            pygame.display.flip()
            self.clock.tick(60)
        self.actif(False)
        self.largeur, self.hauteur = 400, 400
        pygame.display.set_mode((self.largeur, self.hauteur))
        if self.boss.get_victoire():
            joueur1.set_cagnotte(0)
        else:
            self.set_reussi()
            joueur1.modifier_cagnotte(50000)
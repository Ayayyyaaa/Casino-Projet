import pygame
import time
import sys
from objets_et_variables import *
from sons import son_epee,aie_boss,aie_hero
from random import randint,choice
from fonctions import afficher_ecran_chargement
from SQL import maj_stats, det_id_compte
from boss import *
from heros import *

afficher_ecran_chargement(chargement[8])
print("Chargement du jeu de combat...")

class JeuCombat:
    def __init__(self,j1,j2,nom_boss:str) -> float:
        '''Initialise les attributs du jeu de combat.
        Paramètres :
            - j1 : le héros du joueur1
            - j2 : le boss (joueur2)
            - nom_boss (str) : le nom du boss combattu (joueur2)
        Returns :
            - Le multiplicateur du dictionnaire, avec 1 comme valeur par défaut si la combinaison n'existe pas
        - self.fond : Image du fond du jeu
        - self.fonds : dictionnaire des images des fond du jeu, avec les clés correspondant aux noms des fond du jeu et les valeurs correspondant au sol du fond
        - self.run : booléen indiquant si le jeu est en cours
        - self.vie_hero : Image du compteur de vie du héros
        - self.vie_boss : Image du compteur de vie du boss
        - self.police : police utilisée pour afficher les textes
        - self.dmg : booléen indiquant si un dégât a été subi
        - self.j1 : instance de la classe Hero, héros du joueur 1
        - self.j2 : instance de la classe Boss, boss combattu par le heros du joueur 1
        - self.reussi : booléen indiquant si le combat est réussi
        - self.frame : compteur pour l'animation'''
        self.fond = j2.boss.get_fond()
        self.fonds = {'Temple':0,'Desert':50,'Eglise':15,'Chute':10,'Lave':50,'Pluie':25,'Dojo':20}
        self.run = False
        self.vie_hero = pygame.image.load("images/Jeu de combat/compteur.png")
        self.vie_boss = pygame.image.load("images/Jeu de combat/compteur.png")
        self.police = pygame.font.Font('8-bitanco.ttf', 15)
        self.dmg = False
        self.j1 = j1
        self.j2 = j2
        self.reussi = False
        self.frame = 0
        self.nom_boss = nom_boss
    def actif(self, etat):
        self.run = etat
    def get_actif(self):
        return self.run
    def set_reussi(self):
        self.reussi = True
    def get_reussi(self):
        return self.reussi
    def multis(self, j1, j2):
        '''Fonction qui permet de calculer les multiplicateurs de dégâts en fonction des éléments du boss et du héros.
        Paramètres :
            - j1 : le joueur1 (héros)
            - j2 : le joueur2 (boss)'''
        multis_elements = {
            'Feu': {
                'FeuImmune' : 0,
                'Feu': 0.7,
                'Glace': 1.75,
                'Eau': 1.45,
                'Nature': 1.25,
                'Esprit': 1.1,
                'Air': 0.9,
                'Nuit': 0.8,
                'Foudre' : 1.4
            },
            'Esprit': {
                'Feu': 1.1,
                'Glace': 0.9,
                'Eau': 1.1,
                'Nature': 1.25,
                'Air': 0.8,
                'Esprit': 0.4,
                'Nuit': 1.45,
                'Foudre' : 0.95
            },
            'Air': {
                'Feu': 1.2,
                'Glace': 1.1,
                'Eau': 1.15,
                'Nature': 0.9,
                'Air': 0.6,
                'Esprit': 1.45,
                'Nuit': 1.05,
                'Foudre' : 0.95
            },
            'Nuit': {
                'Feu': 1.65,
                'Glace': 1.05,
                'Eau': 1.1,
                'Nature': 0.9,
                'Air': 1.2,
                'Esprit': 0.75,
                'Nuit': 0.5,
                'Foudre' : 0.85
            },
            'Foudre': {
                'Feu': 1.4,
                'Glace': 1.12,
                'Eau': 1.2,
                'Nature': 0.9,
                'Air': 0.7,
                'Esprit': 1.14,
                'Nuit': 1.05,
                'Foudre' : 0.5
            }
        }
        
        el1 = j1.hero.get_type()
        el2 = j2.boss.get_type()
        
        # Return le multiplicateur du dictionnaire, avec 1 comme valeur par défaut si la combinaison n'existe pas
        return multis_elements.get(el1, {}).get(el2, 1.0)

    def lancer(self):
        '''La boucle principale du jeu, elle permet les déplacements et actions du héros et du boss tant que le combat n'est pas fini.'''
        # Boucle principale du jeu
        self.largeur, self.hauteur = 1200, 700
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.clock = pygame.time.Clock()
        # On réinitialise tout
        self.j2.boss.modif_pv(-self.j2.boss.get_pv()+self.j2.boss.get_pv_base())
        self.j1.hero.modif_pv(-self.j1.hero.get_pv()+self.j1.hero.get_pv_base())
        self.j2.boss.modif_pos_x(-self.j2.boss.get_pos_x()+1000)
        self.j1.hero.modif_pos_x(-self.j1.hero.get_pos_x()+50)
        self.j1.hero.modif_img(self.j1.images_marche_d[0])
        self.j1.hero.set_victoire(False)
        self.j2.boss.set_victoire(False)
        self.j2.boss.set_mort(False)
        self.j1.hero.set_mort(False)
        while not self.j1.hero.get_victoire() and not self.j2.boss.get_victoire() and self.run:
            self.frame += 0.14
            # Permet de détermnier les collisions entre le héros et le boss grace aux sprites de ceux-ci
            mask1 = pygame.mask.from_surface(self.j1.hero.image)
            mask2 = pygame.mask.from_surface(self.j2.boss.image)
            offset_x = self.j2.boss.get_pos_x() - self.j1.hero.get_pos_x()
            offset_y = self.j2.boss.get_pos_y() - self.j1.hero.get_pos_y()
            mask1_overlap = mask1.overlap(mask2, (offset_x, offset_y))
            mask2_overlap = mask2.overlap(mask1, (-offset_x, -offset_y))

            # Mettre à jour les collisions
            self.j1.hero.set_collision(mask1_overlap)
            self.j2.boss.set_collision(mask2_overlap)

            if self.frame >= len(self.fond)-1:
                # On remet tout à 0
                self.frame = 0
            fenetre.blit(self.fond[int(self.frame)],(0,0))
            multis = self.multis(self.j1,self.j2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        if self.j1.hero.get_attaque() and self.j1.hero.get_cd_atk() > 0.5 and not self.j1.hero.get_stun():
                            self.j1.hero.set_combo(True)
                        if self.j1.hero.get_cd_atk() > self.j1.hero.get_cd()[0] and not self.j1.hero.get_cp2() and not self.j1.hero.get_stun():
                            self.j1.reset_frame()
                            self.j1.hero.set_cd_atk()
                            self.j1.hero.set_attaque(True)
                    elif event.key == pygame.K_KP0 and self.j1.hero.get_cd_cp2() > self.j1.hero.get_cd()[1] and not self.j1.hero.get_attaque() and not self.j1.hero.get_stun():
                        self.j1.reset_frame()
                        self.j1.hero.set_cd_cp2()
                        self.j1.hero.set_cp2(True)
                        
            if not self.j2.boss.get_pv() <= 0:
                if self.j1.hero.get_pv() > 0:
                    self.j2.patern_boss(self.j1.hero.get_pos_x(),self.j1)
                else:
                    self.j2.inaction(self.j2.boss.get_speed_anim(),'Gauche')
            else:
                self.j2.mort(0.1,self.j1)

            if self.j1.hero.get_pv() <= 0:
                self.j1.mort(0.1,self.j2)

            keys = pygame.key.get_pressed()
            if not self.j1.hero.get_stun():
                if not self.j1.hero.get_attaque() and not self.j1.hero.get_pv() <= 0:
                    if keys[pygame.K_LEFT]:
                        if self.j1.hero.get_pos_x() > 0:
                            self.j1.hero.modif_pos_x(-self.j1.hero.get_speed())
                        self.j1.marche(self.j1.hero.get_speed_anim()[1],'Gauche',self.j2)
                    if keys[pygame.K_RIGHT]:
                        if self.j1.hero.get_pos_x() < 1000:
                            self.j1.hero.modif_pos_x(self.j1.hero.get_speed())
                        self.j1.marche(self.j1.hero.get_speed_anim()[1],'Droite',self.j2)

            if self.j2.boss.get_poison() != False:
                self.j2.boss.modif_pv(-0.02*multis)
                if time.time() - self.j2.boss.get_poison() > 5:
                    self.j2.boss.set_poison(False)
            if self.j1.hero.get_poison() != False:
                self.j1.hero.modif_pv(-0.02)
                if time.time() - self.j1.hero.get_poison() > 7:
                    self.j1.hero.set_poison(False)

            if self.j2.boss.get_cd_attaque1() > self.j2.boss.get_cd()[0]:
                self.j2.boss.set_attaque1_dispo(True)
            if self.j2.boss.get_cd_attaque2() > self.j2.boss.get_cd()[1]:
                self.j2.boss.set_attaque2_dispo(True)
            if self.j2.boss.get_cd_attaque3() > self.j2.boss.get_cd()[2]:
                self.j2.boss.set_attaque3_dispo(True)


            if self.j1.hero.get_attaque():
                if self.j2.boss.get_pos_x() > self.j1.hero.get_pos_x():
                    self.j1.attaque(self.j1.hero.get_speed_anim()[0],'Droite',self.j2,multis)
                else:
                    self.j1.attaque(self.j1.hero.get_speed_anim()[0],'Gauche',self.j2,multis)

            elif self.j1.hero.get_cp2():
                if self.j2.boss.get_pos_x() > self.j1.hero.get_pos_x():
                    self.j1.cp2(self.j1.hero.get_speed_anim()[0],'Droite',self.j2,multis)
                else:
                    self.j1.cp2(self.j1.hero.get_speed_anim()[0],'Gauche',self.j2,multis)
            elif not self.j1.hero.get_attaque() and not self.j1.hero.get_cp2() and self.j1.hero.get_pv() > 0 and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] or self.j1.hero.get_stun() and self.j1.hero.get_pv() > 0:
                self.j1.inaction(self.j2)

            #mask1_surface = mask1.to_surface(setcolor=(255, 255, 255), unsetcolor=(0, 0, 0))
            #mask2_surface = mask2.to_surface(setcolor=(255, 255, 255), unsetcolor=(0, 0, 0))
            #fenetre.blit(mask2_surface, (self.j2.boss.get_pos_x(), self.j2.boss.get_pos_y()-self.fonds[self.j2.boss.get_nomfond()]))
            #fenetre.blit(mask1_surface, (self.j1.hero.get_pos_x(), self.j1.hero.get_pos_y()-self.fonds[self.j2.boss.get_nomfond()]))
            self.fenetre.blit(self.j2.boss.image, (self.j2.boss.get_pos_x(), self.j2.boss.get_pos_y()-self.fonds[self.j2.boss.get_nomfond()]))
            self.fenetre.blit(self.j1.hero.image, (self.j1.hero.get_pos_x(), self.j1.hero.get_pos_y()-self.fonds[self.j2.boss.get_nomfond()]))
            '''if isinstance(self.j2, Pandora) and self.j2.minion:          #Cas du boss Pandora, qui invoque des serviteurs pour ce battre, mais le boss comporte des problèmes donc il n'est pas actif
                mask3 = pygame.mask.from_surface(self.j2.minion.boss.image)
                offset_x = self.j2.minion.boss.get_pos_x() - self.j1.hero.get_pos_x()
                offset_y = self.j2.minion.boss.get_pos_y() - self.j1.hero.get_pos_y()
                mask3_overlap = mask3.overlap(mask1, (offset_x, offset_y))
                self.j2.minion.boss.set_collision(mask3_overlap)
                self.fenetre.blit(
                    self.j2.minion.boss.image,
                    (self.j2.minion.boss.get_pos_x(), self.j2.minion.boss.get_pos_y()-self.fonds[self.j2.boss.get_nomfond()])
                )'''
            self.fenetre.blit(self.vie_hero, (0, -50))
            self.fenetre.blit(self.vie_boss, (950, -50))
            pvheros = self.police.render("Pv du heros : " + str(int(self.j1.hero.get_pv())), True, noir)
            pvboss = self.police.render("Pv du boss : " + str(int(self.j2.boss.get_pv())), True, noir)
            fenetre.blit(pvheros, (60, 70))
            fenetre.blit(pvboss, (1010, 70))
            fenetre.blit(souris, pygame.mouse.get_pos())
            pygame.display.flip()
            self.clock.tick(60)
        self.actif(False)
        self.largeur, self.hauteur = 400, 400
        pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.mixer.music.unload()

        if self.j2.boss.get_victoire():
            joueur1.set_cagnotte(0)
            maj_stats(det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp()),0,1,self.nom_boss)
        elif self.j1.hero.get_victoire():
            self.set_reussi()
            joueur1.modifier_cagnotte(joueur1.get_cagnotte()/4+15000)
            maj_stats(det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp()),1,0,self.nom_boss)
        else:
            pygame.quit()




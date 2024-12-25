import pygame
import time
import sys
from objets_et_variables import *
from sons import son_epee,aie_boss,aie_hero
from random import randint,choice

def distance(j1,j2):
    return j1.hero.get_pos_x()-j2.boss.get_pos_x()
class Boss:
    def __init__(self,pv,largeur,portee,y,speed,speedanim,cd1,cd2,cd3,element,fond,nom_fond):
        self.image = self.image = pygame.image.load('images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png')
        self.pv = pv
        self.pos_x = 1000
        self.pos_y = y
        self.cd_img = 0
        self.attaque1_dispo = True
        self.attaque2_dispo = True
        self.attaque3_dispo = True
        self.cd_attaque1 = 0
        self.cd_attaque2 = 0
        self.cd_attaque3 = 0
        self.victoire = False
        self.cd_ulti = 0
        self.mort = False
        self.pv_base = pv
        self.hitbox = largeur
        self.portee = portee
        self.poison = False
        self.speed = speed
        self.speedanim = speedanim
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.block = False
        self.type = element
        self.fond = fond
        self.nom_fond = nom_fond
    def get_pv(self):
        return self.pv
    def get_pv_base(self):
        return self.pv_base
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
    def get_cd_attaque3(self):
        return time.time() - self.cd_attaque3
    def get_attaque3_dispo(self):
        return self.attaque3_dispo
    def get_victoire(self):
        return self.victoire
    def get_cd_ulti(self):
        return self.cd_ulti
    def get_mort(self):
        return self.mort
    def get_portee(self):
        return self.portee
    def get_poison(self):
        return self.poison
    def get_speed(self):
        return self.speed
    def get_speed_anim(self):
        return (self.speedanim)
    def get_cd(self):
        return (self.cd1,self.cd2,self.cd3)
    def get_block(self):
        return self.block
    def get_fond(self):
        return self.fond
    def get_type(self):
        return self.type
    def get_nomfond(self):
        return self.nom_fond
    def modif_pv(self, nb):
        self.pv += nb
    def modif_pos_x(self, nb):
        self.pos_x += nb
    def modif_pos_y(self, nb):
        self.pos_y += nb
    def modif_img(self, img):
        self.image = img
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
    def set_cd_attaque3(self):
        self.cd_attaque3 = time.time()
    def set_attaque3_dispo(self, dispo):
        self.attaque3_dispo = dispo
    def set_victoire(self, vict):
        self.victoire = vict
    def set_cd_ulti(self, nb):
        self.cd_ulti = nb
    def set_mort(self,mort):
        self.mort = mort
    def set_poison(self,poison):
        self.poison = poison
    def set_block(self,block):
        self.block = block

class Hero:
    def __init__(self,pv,y,speed,spanim1,marche,cd1,cd2,portee,element):
        self.image = None
        self.pv = pv
        self.pv_base = pv
        self.pos_x = 50
        self.pos_y = y
        self.cd_img = 0
        self.attaque = False
        self.victoire = False
        self.cp2 = False
        self.block = False
        self.cd_cp2 = time.time()
        self.cd_atk = time.time()
        self.mort = False
        self.speed = speed
        self.speed_base = speed
        self.speed_anim1 = spanim1
        self.speed_anim4 = marche
        self.combo = False
        self.cd = (cd1,cd2)
        self.portee = portee
        self.poison = False
        self.stun = False
        self.type = element
    def get_pv(self):
        return self.pv
    def get_pv_base(self):
        return self.pv_base
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    def get_attaque(self):
        return self.attaque
    def get_victoire(self):
        return self.victoire
    def get_cp2(self):
        return self.cp2
    def get_cd_cp2(self):
        return time.time() - self.cd_cp2
    def get_cd_atk(self):
        return time.time() - self.cd_atk
    def get_mort(self):
        return self.mort
    def get_speed(self):
        return self.speed
    def get_speed_base(self):
        return self.speed_base
    def get_speed_anim(self):
        return (self.speed_anim1,self.speed_anim4)
    def get_block(self):
        return (self.block)
    def get_combo(self):
        return self.combo
    def get_portee(self):
        return self.portee
    def get_cd(self):
        return self.cd
    def get_poison(self):
        return self.poison
    def get_stun(self):
        return self.stun
    def get_type(self):
        return self.type
    def set_mort(self,mort):
        self.mort = mort
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
    def set_victoire(self,vict):
        self.victoire = vict
    def set_cp2(self, actif):
        self.cp2 = actif
    def set_cd_cp2(self):
        self.cd_cp2 = time.time()
    def set_cd_atk(self):
        self.cd_atk = time.time()
    def set_block(self,block):
        self.block = block
    def set_combo(self,combo):
        self.combo = combo
    def set_speed(self,s):
        self.speed = s
    def set_poison(self,poison):
        self.poison = poison
    def set_stun(self,stun):
        self.stun = stun

class Night_Hero:
    def __init__(self):
        self.hero = Hero(100,540,4,0.25,0.2,1.2,5,80,'Nuit')
        self.images_coup_depee_d = [f'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque{i}.png' for i in range(1,13)]
        self.images_coup_depee_g = [f'images/Jeu de combat/Hero/Attaque/Attaque_Gauche/Attaque{i}.png' for i in range(1,13)]
        self.images_marche_d = [f'images/Jeu de combat/Hero/Marche/Droite/Hero_course{i}.png' for i in range(1,7)] 
        self.images_marche_g = [f'images/Jeu de combat/Hero/Marche/Gauche/Hero_course{i}.png' for i in range(1,7)]
        self.images_parade = [f'images/Jeu de combat/Hero/Block/Block ({i}).png' for i in range(1,19)]
        self.images_mort = [f'images/Jeu de combat/Hero/Mort/_afrm{i},70.png' for i in range(1,23)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0

    def inaction(self,sens):
        return None

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if self.frame >= len(self.images_coup_depee_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                if self.hero.get_pos_x()-140 < j2.boss.get_pos_x() < self.hero.get_pos_x() + 100 and not j2.boss.get_block():
                    # Le boss perd 5 Pv
                    aie_boss.play()
                    j2.boss.modif_pv(-5*multis)
                    print(f"Attaque Épée Héros : Pv boss : {j2.boss.get_pv()}")
                    # Affichage des dégâts subis
                    self.cd_dgt5 = time.time()
                self.frame = 0
                self.hero.set_attaque(False)
            if sens == 'Gauche':
                self.hero.modif_img(self.images_coup_depee_g[int(self.frame)])
            else:
                self.hero.modif_img(self.images_coup_depee_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])
        

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_block(True)
        # On ne joue l'animation que si le héros n'est pas en train d'attaquer
        if not self.hero.get_attaque() and  self.hero.get_pv() > 0:
            self.hero.modif_img(self.images_parade[int(self.frame_parade)])
        # Si toutes les images ont été jouées :
        if int(self.frame_parade) >= len(self.images_parade)-1:
            # On remet tout à 0
            self.frame_parade = 0
            self.hero.set_block(False)
            self.hero.set_cp2(False)
        # Faire progresser les images pour l'animation
        self.frame_parade += speed

    def reset_frame(self):
        self.frame=0

class Spirit_Hero:
    def __init__(self):
        self.hero = Hero(160,490,5,0.12,0.06,3,6,150,'Esprit')
        self.atk1_d = [f'images/Jeu de combat/Spirit_Hero/Droite/Attaque1/_a_frm{i},100.png' for i in range(1,12)]
        self.atk2_d = [f'images/Jeu de combat/Spirit_Hero/Droite/Attaque2/_a_frm{i},100.png' for i in range(12,23)]
        self.atk1_g = [f'images/Jeu de combat/Spirit_Hero/Gauche/Attaque1/_a_frm{i},100.png' for i in range(1,12)]
        self.atk2_g = [f'images/Jeu de combat/Spirit_Hero/Gauche/Attaque2/_a_frm{i},100.png' for i in range(10,21)]
        self.images_marche_d = [f'images/Jeu de combat/Spirit_Hero/Droite/Mvmt/_a_frm{i},100.png' for i in range(1,9)] 
        self.images_marche_g = [f'images/Jeu de combat/Spirit_Hero/Gauche/Mvmt/_a_frm{i},100.png' for i in range(1,9)]
        self.cp2_d = [f'images/Jeu de combat/Spirit_Hero/Droite/Attaque3/_a_frm{i},100.png' for i in range(21,42)]
        self.cp2_g = [f'images/Jeu de combat/Spirit_Hero/Gauche/Attaque3/_a_frm{i},100.png' for i in range(21,42)]
        self.images_mort = [f'images/Jeu de combat/Spirit_Hero/Mort/_a_frm{i},100.png' for i in range(20)] 
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False

    def inaction(self,sens):
        return None

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if not self.atk2:
                if self.frame >= len(self.atk1_d)-1:
                    son_epee.play()
                    print(j2.boss.get_pos_x(),self.hero.get_pos_x())
                    # Si le boss est à portée du héros
                    if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-randint(5,15)*multis)
                        print(f"Attaque Masse Héros : Pv boss : {j2.boss.get_pv()}")
                        # Affichage des dégâts subis
                        self.cd_dgt5 = time.time()
                    if not self.hero.combo:
                        self.frame = 0
                        self.hero.set_attaque(False)
                    else:
                        self.frame = 0
                        self.atk2 = True
                elif sens == 'Gauche':
                    self.hero.modif_img(self.atk1_g[int(self.frame)])
                elif sens == 'Droite':
                    self.hero.modif_img(self.atk1_d[int(self.frame)])
            elif self.atk2:
                if self.frame >= len(self.atk2_d)-1:
                    son_epee.play()
                    # Si le boss est à portée du héros
                    if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-randint(10,20)*multis)
                        print(f"Attaque combo : Pv boss : {j2.boss.get_pv()}")
                        # Affichage des dégâts subis
                        self.cd_dgt5 = time.time()
                    self.frame = 0
                    print(self.hero.get_attaque())
                    self.hero.set_attaque(False)
                    self.hero.set_combo(False)
                    self.atk2 = False
                elif sens == 'Gauche':
                    self.hero.modif_img(self.atk2_g[int(self.frame)])
                elif sens == 'Droite':
                    self.hero.modif_img(self.atk2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if self.frame >= len(self.cp2_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                    # Le boss perd 5 Pv
                    aie_boss.play()
                    j2.boss.modif_pv(-randint(15,40)*multis)
                    print(f"Attaque chargée Héros : Pv boss : {j2.boss.get_pv()}")
                    # Affichage des dégâts subis
                    self.cd_dgt5 = time.time()
                self.frame = 0
                self.hero.set_cp2(False)
            if sens == 'Gauche':
                self.hero.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.hero.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
    
    def reset_frame(self):
        self.frame=0

class Spirit_Warrior:
    def __init__(self):
        self.hero = Hero(200,502,0.8,0.12,0.06,4.5,6,170,'Esprit')
        self.atk1_d = [f'images/Jeu de combat/Spirit_Warrior/Droite/Attaque1/_a_frm{i},100.png' for i in range(1,13)]
        self.atk2_d = [f'images/Jeu de combat/Spirit_Warrior/Droite/Attaque2/_a_frm{i},100.png' for i in range(15,30)]
        self.atk1_g = [f'images/Jeu de combat/Spirit_Warrior/Gauche/Attaque1/_a_frm{i},100.png' for i in range(1,13)]
        self.atk2_g = [f'images/Jeu de combat/Spirit_Warrior/Gauche/Attaque2/_a_frm{i},100.png' for i in range(15,30)]
        self.images_marche_d = [f'images/Jeu de combat/Spirit_Warrior/Droite/Marche/_a_frm{i},100.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Spirit_Warrior/Gauche/Marche/_a_frm{i},100.png' for i in range(8)]
        self.cp2_d = [f'images/Jeu de combat/Spirit_Warrior/Droite/Attaque3/_a_frm{i},100.png' for i in range(33,47)]
        self.cp2_g = [f'images/Jeu de combat/Spirit_Warrior/Gauche/Attaque3/_a_frm{i},100.png' for i in range(33,47)]
        self.images_mort = [f'images/Jeu de combat/Spirit_Warrior/Mort/_a_frm{i},100.png' for i in range(13)] 
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False

    def inaction(self,sens):
        return None

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if not self.atk2:
                if self.frame >= len(self.atk1_d)-1:
                    son_epee.play()
                    # Si le boss est à portée du héros
                    if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-6*multis)
                        print(f"Attaque Masse Héros : Pv boss : {j2.boss.get_pv()}")
                        # Affichage des dégâts subis
                        self.cd_dgt5 = time.time()
                        j2.boss.set_poison(time.time())
                    if not self.hero.combo:
                        self.frame = 0
                        self.hero.set_attaque(False)
                    else:
                        self.frame = 0
                        self.atk2 = True
                elif sens == 'Gauche':
                    self.hero.modif_img(self.atk1_g[int(self.frame)])
                elif sens == 'Droite':
                    self.hero.modif_img(self.atk1_d[int(self.frame)])
            elif self.atk2:
                if self.frame >= len(self.atk2_d)-1:
                    son_epee.play()
                    # Si le boss est à portée du héros
                    if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-15*multis)
                        print(f"Attaque combo : Pv boss : {j2.boss.get_pv()}")
                        # Affichage des dégâts subis
                        self.cd_dgt5 = time.time()
                        j2.boss.set_poison(time.time())
                    self.frame = 0
                    self.hero.set_attaque(False)
                    self.hero.set_combo(False)
                    self.atk2 = False
                elif sens == 'Gauche':
                    self.hero.modif_img(self.atk2_g[int(self.frame)])
                elif sens == 'Droite':
                    self.hero.modif_img(self.atk2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if self.frame >= len(self.cp2_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                    # Le boss perd 5 Pv
                    aie_boss.play()
                    j2.boss.modif_pv(-20*multis)
                    print(f"Attaque chargée Héros : Pv boss : {j2.boss.get_pv()}")
                    # Affichage des dégâts subis
                    self.cd_dgt5 = time.time()
                    j2.boss.set_poison(time.time())
                self.frame = 0
                self.hero.set_cp2(False)
            if sens == 'Gauche':
                self.hero.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.hero.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
    
    def reset_frame(self):
        self.frame=0

class Lancier:
    def __init__(self):
        self.hero = Hero(120,505,3,0.12,0.15,3,6,120,'Esprit')
        self.atk1_d = [f'images/Jeu de combat/Lancier/Droite/Attaque1/_a_frm{i},100.png' for i in range(10)]
        self.atk1_g = [f'images/Jeu de combat/Lancier/Gauche/Attaque1/_a_frm{i},100.png' for i in range(10)]
        self.images_marche_d = [f'images/Jeu de combat/Lancier/Droite/Mvmt/_a_frm{i},100.png' for i in range(0,8)] 
        self.images_marche_g = [f'images/Jeu de combat/Lancier/Gauche/Mvmt/_a_frm{i},100.png' for i in range(0,8)] 
        self.cp2_d = [f'images/Jeu de combat/Lancier/Droite/Charge/_a_frm{i},100.png' for i in range(8)]
        self.cp2_g = [f'images/Jeu de combat/Lancier/Gauche/Charge/_a_frm{i},100.png' for i in range(8)]
        self.images_mort = [f'images/Jeu de combat/Lancier/Mort/_a_frm{i},100.png' for i in range(14)] 
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.charge = False

    def inaction(self,sens):
        return None

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if self.frame >= len(self.atk1_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                    # Le boss perd 5 Pv
                    aie_boss.play()
                    j2.boss.modif_pv(-8*multis)
                    print(f"Attaque Épée Héros : Pv boss : {j2.boss.get_pv()}")
                    # Affichage des dégâts subis
                    self.cd_dgt5 = time.time()
                self.frame = 0
                self.hero.set_attaque(False)
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            if not self.charge:
                self.hero.modif_img(self.images_marche_g[int(self.frame)])
            else:
                if abs(distance(self,j2)) < 4:
                    if not j2.boss.get_block():
                        j2.boss.modif_pv(-20)
                        print(f"Attaque Charge Héros : Pv boss : {j2.boss.get_pv()}")
                    self.charge = False
                    self.hero.set_cp2(False)
                    self.hero.set_speed(4)
                self.hero.modif_img(self.cp2_g[int(self.frame)])
        else:
            if not self.charge:
                self.hero.modif_img(self.images_marche_d[int(self.frame)])
            else:
                if abs(distance(self,j2)) < 4:
                    self.charge = False
                    self.hero.set_cp2(False)
                    self.hero.set_speed(4)
                    if not j2.boss.get_block():
                        j2.boss.modif_pv(-20)
                        print(f"Attaque Charge Héros : Pv boss : {j2.boss.get_pv()}")
                self.hero.modif_img(self.cp2_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            self.charge = True
            self.hero.set_speed(6.5)
            if self.hero.get_cd_cp2() > 3:
                self.charge = False
                self.hero.set_cp2(False)
                self.hero.set_speed(4)
    
    def reset_frame(self):
        self.frame=0

class Assassin:
    def __init__(self):
        self.hero = Hero(75,480,2.5,0.2,0.1,2,1.3,120,'Neutre')
        self.atk1_d = [f'images/Jeu de combat/Assassin/Droite/Attaque1/_a_frm{i},100.png' for i in range(10)]
        self.atk2_d = [f'images/Jeu de combat/Assassin/Droite/Attaque2/_a_frm{i},100.png' for i in range(11,18)]
        self.atk1_g = [f'images/Jeu de combat/Assassin/Gauche/Attaque1/_a_frm{i},100.png' for i in range(10)]
        self.atk2_g = [f'images/Jeu de combat/Assassin/Gauche/Attaque2/_a_frm{i},100.png' for i in range(11,18)]
        self.images_marche_d = [f'images/Jeu de combat/Assassin/Droite/Marche/_a_frm{i},100.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Assassin/Gauche/Marche/_a_frm{i},100.png' for i in range(8)]
        self.images_course_d = [f'images/Jeu de combat/Assassin/Droite/Course/_a_frm{i},70.png' for i in range(8)] 
        self.images_course_g = [f'images/Jeu de combat/Assassin/Gauche/Course/_a_frm{i},70.png' for i in range(8)]
        self.cp2_d = [f'images/Jeu de combat/Assassin/Droite/Saut/_a_frm{i},100.png' for i in range(2,14)]
        self.cp2_g = [f'images/Jeu de combat/Assassin/Gauche/Saut/_a_frm{i},100.png' for i in range(2,14)]
        self.images_mort = [f'images/Jeu de combat/Assassin/Mort/_a_frm{i},100.png' for i in range(16)] 
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if not self.atk2:
                if self.frame >= len(self.atk1_d)-1:
                    son_epee.play()
                    print(j2.boss.get_pos_x(),self.hero.get_pos_x())
                    # Si le boss est à portée du héros
                    if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-8*multis)
                        print(f"Attaque Masse Héros : Pv boss : {j2.boss.get_pv()}")
                        # Affichage des dégâts subis
                        self.cd_dgt5 = time.time()
                    if not self.hero.combo:
                        self.frame = 0
                        self.hero.set_attaque(False)
                    else:
                        self.frame = 0
                        self.atk2 = True
                elif sens == 'Gauche':
                    self.hero.modif_img(self.atk1_g[int(self.frame)])
                elif sens == 'Droite':
                    self.hero.modif_img(self.atk1_d[int(self.frame)])
            elif self.atk2:
                if self.frame >= len(self.atk2_d)-1:
                    son_epee.play()
                    # Si le boss est à portée du héros
                    if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-10*multis)
                        print(f"Attaque combo : Pv boss : {j2.boss.get_pv()}")
                        # Affichage des dégâts subis
                        self.cd_dgt5 = time.time()
                    self.frame = 0
                    print(self.hero.get_attaque())
                    self.hero.set_attaque(False)
                    self.hero.set_combo(False)
                    self.atk2 = False
                elif sens == 'Gauche':
                    self.hero.modif_img(self.atk2_g[int(self.frame)])
                elif sens == 'Droite':
                    self.hero.modif_img(self.atk2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if not self.hero.get_cp2():
            # Si toutes les images ont été jouées :
            self.frame += speed
            if int(self.frame) >= len(self.images_marche_d)-1:
                # On remet tout à 0
                self.frame = 0
            # Faire progresser les images pour l'animation
            if sens == 'Gauche':
                if abs(distance(self,j2)) > 300:
                    self.hero.modif_img(self.images_marche_g[int(self.frame)])
                    self.hero.set_speed(2.5)
                else:
                    self.hero.modif_img(self.images_course_g[int(self.frame)])
                    self.hero.set_speed(6)
            else:
                if abs(distance(self,j2)) > 300:
                    self.hero.modif_img(self.images_marche_d[int(self.frame)])
                    self.hero.set_speed(2.4)
                else:
                    self.hero.modif_img(self.images_course_d[int(self.frame)])
                    self.hero.set_speed(6)

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            self.hero.set_block(True)
            if self.frame >= len(self.cp2_d)-1:
                self.frame = 0
                self.hero.set_cp2(False)
                self.hero.set_block(False)
            if sens == 'Gauche':
                self.hero.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.hero.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,sens):
        return None

class Zukong:
    def __init__(self):
        self.hero = Hero(160,495,3.2,0.18,0.14,4.5,3,170,'Neutre')
        self.atk1_d = [f'images/Jeu de combat/Zukong/Droite/Attaque1/_a_frm{i},60.png' for i in range(19)]
        self.atk1_g = [f'images/Jeu de combat/Zukong/Gauche/Attaque1/_a_frm{i},60.png' for i in range(19)]
        self.images_marche_d = [f'images/Jeu de combat/Zukong/Droite/Marche/_a_frm{i},60.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Zukong/Gauche/Marche/_a_frm{i},60.png' for i in range(8)]
        self.cp2_d = [f'images/Jeu de combat/Zukong/Droite/Attaque2/_a_frm{i},60.png' for i in range(19,32)]
        self.cp2_g = [f'images/Jeu de combat/Zukong/Gauche/Attaque2/_a_frm{i},60.png' for i in range(19,32)]
        self.images_mort = [f'images/Jeu de combat/Zukong/Mort/_a_frm{i},60.png' for i in range(31)] 
        self.inaction_g = [f'images/Jeu de combat/Zukong/Gauche/Inaction/_a_frm{i},80.png' for i in range(14)]
        self.inaction_d = [f'images/Jeu de combat/Zukong/Droite/Inaction/_a_frm{i},80.png' for i in range(14)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if abs(distance(self, j2)) < self.hero.get_portee() and 5 <= self.frame <= 11 and not j2.boss.get_block():
                # Le boss perd 5 Pv
                aie_boss.play()
                j2.boss.modif_pv(-0.25*multis)
                print(f"Attaque Masse Héros : Pv boss : {j2.boss.get_pv()}")
                # Affichage des dégâts subis
                self.cd_dgt5 = time.time()
            if self.frame >= len(self.atk1_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                self.frame = 0
                self.hero.set_attaque(False)
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0 :
            if self.frame >= len(self.cp2_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                if abs(distance(self, j2)) < self.hero.get_portee() and not j2.boss.get_block():
                    # Le boss perd 5 Pv
                    aie_boss.play()
                    j2.boss.modif_pv(-8*multis)
                    print(f"Attaque chargée Héros : Pv boss : {j2.boss.get_pv()}")
                    # Affichage des dégâts subis
                    self.cd_dgt5 = time.time()
                self.frame = 0
                self.hero.set_cp2(False)
            if sens == 'Gauche':
                self.hero.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.hero.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2

class Maehv:
    def __init__(self):
        self.hero = Hero(125,440,3.2,0.18,0.14,5,1,190,'Feu')
        self.atk1_d = [f'images/Jeu de combat/Maehv/Droite/Attaque1/_a_frm{i},60.png' for i in range(33)]
        self.atk1_g = [f'images/Jeu de combat/Maehv/Gauche/Attaque1/_a_frm{i},60.png' for i in range(33)]
        self.images_marche_d = [f'images/Jeu de combat/Maehv/Droite/Marche/_a_{i},60.png' for i in range(10)] 
        self.images_marche_g = [f'images/Jeu de combat/Maehv/Gauche/Marche/_a_{i},60.png' for i in range(10)]
        self.cp2_d = [f'images/Jeu de combat/Maehv/Droite/Attaque3/_a_{i},60.png' for i in range(4)]
        self.cp2_g = [f'images/Jeu de combat/Maehv/Gauche/Attaque3/_a_{i},60.png' for i in range(4)]
        self.images_mort = [f'images/Jeu de combat/Maehv/Mort/_a_{i},60.png' for i in range(11)] 
        self.inaction_g = [f'images/Jeu de combat/Maehv/Gauche/Inaction/_a_{i},80.png' for i in range(14)]
        self.inaction_d = [f'images/Jeu de combat/Maehv/Droite/Inaction/_a_{i},80.png' for i in range(14)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.bonus = 0

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 4 and not j2.boss.get_block():
                if not self.dgt1:
                    aie_boss.play()
                    j2.boss.modif_pv((-6-self.bonus/3)*multis)
                    self.dgt1 = True
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 8 and not j2.boss.get_block():
                if not self.dgt2:
                    aie_boss.play()
                    j2.boss.modif_pv((-10-self.bonus/3)*multis)
                    self.dgt2 = True
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 23 and not j2.boss.get_block():
                if not self.dgt3:
                    aie_boss.play()
                    j2.boss.modif_pv((-15-self.bonus/3)*multis)
                    self.dgt3 = True    
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt1 = False
                self.dgt2 = False
                self.dgt3 = False
                self.bonus = 0
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        keys = pygame.key.get_pressed()
        if self.hero.get_pv() > 0:
            if self.frame >= len(self.cp2_d)-1:
                self.frame = 0
            if self.hero.get_attaque() or self.hero.get_pv() < 0 or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                self.frame = 0
                self.hero.set_cp2(False)
            if sens == 'Gauche':
                self.hero.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.hero.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
            self.bonus += 0.15
            print(self.bonus)
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2

class Zendo:
    def __init__(self):
        self.hero = Hero(130,440,5,0.18,0.14,4.5,3,185,'Air')
        self.atk1_d = [f'images/Jeu de combat/Zendo/Droite/Attaque/_a_{i},60.png' for i in range(38)]
        self.atk1_g = [f'images/Jeu de combat/Zendo/Gauche/Attaque/_a_{i},60.png' for i in range(38)]
        self.images_marche_d = [f'images/Jeu de combat/Zendo/Droite/Marche/_a_{i},60.png' for i in range(6)] 
        self.images_marche_g = [f'images/Jeu de combat/Zendo/Gauche/Marche/_a_{i},60.png' for i in range(6)]
        self.images_mort = [f'images/Jeu de combat/Zendo/Mort/_a_{i},60.png' for i in range(15)] 
        self.inaction_g = [f'images/Jeu de combat/Zendo/Gauche/Inaction/_a_frm{i},60.png' for i in range(14)]
        self.inaction_d = [f'images/Jeu de combat/Zendo/Droite/Inaction/_a_frm{i},60.png' for i in range(14)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 12 and not j2.boss.get_block():
                if not self.dgt1:
                    aie_boss.play()
                    j2.boss.modif_pv(-6*multis)
                    self.dgt1 = True
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 18 and not j2.boss.get_block():
                if not self.dgt2:
                    aie_boss.play()
                    j2.boss.modif_pv(-8*multis)
                    self.dgt2 = True
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 24 and not j2.boss.get_block():
                if not self.dgt3:
                    aie_boss.play()
                    j2.boss.modif_pv(-10*multis)
                    self.dgt3 = True    
                    self.hero.set_block(True)
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 30 and not j2.boss.get_block():
                if not self.dgt4:
                    aie_boss.play()
                    j2.boss.modif_pv(-16*multis)
                    self.dgt4 = True    
                    self.hero.set_block(False)
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt1 = False
                self.dgt2 = False
                self.dgt3 = False
                self.dgt4 = False
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2

class Pureblade:
    def __init__(self):
        self.hero = Hero(100,440,4,0.18,0.14,5.5,1000,185,'Feu')
        self.atk1_d = [f'images/Jeu de combat/Pureblade/Droite/Attaque1/_a_{i},60.png' for i in range(34)]
        self.atk1_g = [f'images/Jeu de combat/Pureblade/Gauche/Attaque1/_a_{i},60.png' for i in range(34)]
        self.images_marche_d = [f'images/Jeu de combat/Pureblade/Droite/Marche/_a_{i},60.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Pureblade/Gauche/Marche/_a_{i},60.png' for i in range(8)]
        self.images_mort = [f'images/Jeu de combat/Pureblade/Mort/_a_{i},60.png' for i in range(20)] 
        self.inaction_g = [f'images/Jeu de combat/Pureblade/Gauche/Inaction/_a_frm{i},80.png' for i in range(10)]
        self.inaction_d = [f'images/Jeu de combat/Pureblade/Droite/Inaction/_a_frm{i},80.png' for i in range(10)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if 5 <= int(self.frame) <= 13 and not j2.boss.get_block():
                aie_boss.play()
                j2.boss.modif_pv(-0.55*multis)
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 23 and not j2.boss.get_block():
                if not self.dgt2:
                    aie_boss.play()
                    j2.boss.modif_pv(-20*multis)
                    j2.boss.set_poison(time.time())
                    self.dgt2 = True
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt2 = False
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2

class Hsuku:
    def __init__(self):
        self.hero = Hero(100,450,5,0.18,0.14,3.5,3,170,'Neutre')
        self.atk1_d = [f'images/Jeu de combat/Hsuku/Droite/Attaque1/_a_{i},70.png' for i in range(24)]
        self.atk1_g = [f'images/Jeu de combat/Hsuku/Gauche/Attaque1/_a_{i},70.png' for i in range(24)]
        self.images_marche_d = [f'images/Jeu de combat/Hsuku/Droite/Marche/_a_{i},70.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Hsuku/Gauche/Marche/_a_{i},70.png' for i in range(8)]
        self.images_mort = [f'images/Jeu de combat/Hsuku/Mort/_a_frm{i},70.png' for i in range(20)] 
        self.inaction_g = [f'images/Jeu de combat/Hsuku/Gauche/Inaction/_a_{i},80.png' for i in range(28)]
        self.inaction_d = [f'images/Jeu de combat/Hsuku/Droite/Inaction/_a_{i},80.png' for i in range(28)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 2 and not j2.boss.get_block():
                if not self.dgt1:
                    aie_boss.play()
                    j2.boss.modif_pv(-6*multis)
                    self.dgt1 = True
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 5 and not j2.boss.get_block():
                if not self.dgt2:
                    aie_boss.play()
                    j2.boss.modif_pv(-6*multis)
                    self.dgt2 = True
            elif int(self.frame) == 12 and not j2.boss.get_block(): 
                if not self.dgt3:
                    aie_boss.play()
                    j2.boss.modif_pv(-8*multis)
                    self.dgt3 = True    
            elif int(self.frame) == 18 and not j2.boss.get_block():
                if not self.dgt4:
                    aie_boss.play()
                    j2.boss.modif_pv(-8*multis)
                    self.dgt4 = True    
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt1 = False
                self.dgt2 = False
                self.dgt3 = False
                self.dgt4 = False
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2

class Sanguinar:
    def __init__(self):
        self.hero = Hero(100,450,5,0.18,0.14,5,3,170,'Neutre')
        self.atk1_d = [f'images/Jeu de combat/Sanguinar/Droite/Attaque1/_a_{i},60.png' for i in range(33)]
        self.atk1_g = [f'images/Jeu de combat/Sanguinar/Gauche/Attaque1/_a_{i},60.png' for i in range(33)]
        self.images_marche_d = [f'images/Jeu de combat/Sanguinar/Droite/Marche/_a_{i},60.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Sanguinar/Gauche/Marche/_a_{i},60.png' for i in range(8)]
        self.images_mort = [f'images/Jeu de combat/Sanguinar/Mort/_a_{i},60.png' for i in range(17)] 
        self.inaction_g = [f'images/Jeu de combat/Sanguinar/Gauche/Inaction/_a_{i},80.png' for i in range(14)]
        self.inaction_d = [f'images/Jeu de combat/Sanguinar/Droite/Inaction/_a_{i},80.png' for i in range(14)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if abs(distance(self, j2)) < self.hero.get_portee() and 5 <= int(self.frame) <= 11 and not j2.boss.get_block():
                aie_boss.play()
                j2.boss.modif_pv(-0.25)
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 16:
                if not j2.boss.get_block() and not self.dgt1:
                    aie_boss.play()
                    j2.boss.modif_pv(-6*multis)
                    self.dgt1 = True
                self.hero.set_block(True)
            elif 20 <= int(self.frame) <= 24 and not j2.boss.get_block(): 
                aie_boss.play()
                j2.boss.modif_pv(-0.38*multis)
            elif int(self.frame) == 26 and not j2.boss.get_block():
                if not self.dgt2:
                    aie_boss.play()
                    j2.boss.modif_pv(-20*multis)
                    self.dgt2 = True    
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt1 = False
                self.dgt2 = False
                self.hero.set_block(False)
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2

class Whistler:
    def __init__(self):
        self.hero = Hero(80,515,6,0.18,0.2,2.5,3,1200,'Feu')
        self.atk1_d = [f'images/Jeu de combat/Whistler/Droite/Attaque1/_a_{i},100.png' for i in range(31)]
        self.atk1_g = [f'images/Jeu de combat/Whistler/Gauche/Attaque1/_a_{i},100.png' for i in range(31)]
        self.images_marche_d = [f'images/Jeu de combat/Whistler/Droite/Marche/_a_{i},100.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Whistler/Gauche/Marche/_a_{i},100.png' for i in range(8)]
        self.images_mort = [f'images/Jeu de combat/Whistler/Mort/_a_{i},100.png' for i in range(20)] 
        self.inaction_g = [f'images/Jeu de combat/Whistler/Gauche/Inaction/_a_{i},100.png' for i in range(18)]
        self.inaction_d = [f'images/Jeu de combat/Whistler/Droite/Inaction/_a_{i},100.png' for i in range(18)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if int(self.frame) == 12 and not j2.boss.get_block():
                if not self.dgt4:
                    dgt = choice([30, 30, 60])
                    if dgt == 60:
                        print("Coup critique !")
                    aie_boss.play()
                    j2.boss.modif_pv(-dgt*multis)
                    self.dgt4 = True    
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt4 = False
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2

class Tethermancer:
    def __init__(self):
        self.hero = Hero(130,410,3.5,0.18,0.14,3.5,3,170,'Feu')
        self.atk1_d = [f'images/Jeu de combat/Tethermancer/Droite/Attaque1/_a_{i},100.png' for i in range(27)]
        self.atk1_g = [f'images/Jeu de combat/Tethermancer/Gauche/Attaque1/_a_{i},100.png' for i in range(27)]
        self.images_marche_d = [f'images/Jeu de combat/Tethermancer/Droite/Marche/_a_{i},100.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Tethermancer/Gauche/Marche/_a_{i},100.png' for i in range(8)]
        self.images_mort = [f'images/Jeu de combat/Tethermancer/Mort/_a_{i},100.png' for i in range(18)] 
        self.inaction_g = [f'images/Jeu de combat/Tethermancer/Gauche/Inaction/_a_{i},100.png' for i in range(17)]
        self.inaction_d = [f'images/Jeu de combat/Tethermancer/Droite/Inaction/_a_{i},100.png' for i in range(17)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if int(self.frame) == 6:
                self.hero.set_block(True)
            elif abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 14:
                if not j2.boss.get_block() and not self.dgt1:
                    aie_boss.play()
                    j2.boss.modif_pv(-22*multis)
                    self.dgt1 = True
                self.hero.set_block(True)
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt1 = False
                self.hero.set_block(False)
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.125

class Aether:
    def __init__(self):
        self.hero = Hero(125,520,4,0.18,0.14,5,1,190,'Air')
        self.atk1_d = [f'images/Jeu de combat/Aether/Droite/Attaque1/_a_{i},100.png' for i in range(26)]
        self.atk1_g = [f'images/Jeu de combat/Aether/Gauche/Attaque1/_a_{i},100.png' for i in range(33)]
        self.images_marche_d = [f'images/Jeu de combat/Aether/Droite/Marche/_a_{i},100.png' for i in range(6)] 
        self.images_marche_g = [f'images/Jeu de combat/Aether/Gauche/Marche/_a_{i},100.png' for i in range(6)]
        self.images_mort = [f'images/Jeu de combat/Aether/Mort/_a_{i},100.png' for i in range(18)] 
        self.inaction_g = [f'images/Jeu de combat/Aether/Gauche/Inaction/_a_{i},100.png' for i in range(12)]
        self.inaction_d = [f'images/Jeu de combat/Aether/Droite/Inaction/_a_{i},100.png' for i in range(12)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.bonus = 0

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if abs(distance(self, j2)) < self.hero.get_portee() and int(self.frame) == 12 and not j2.boss.get_block():
                if not self.dgt1:
                    aie_boss.play()
                    j2.boss.modif_pv((-6-self.bonus)*multis)
                    print(self.bonus)
                    self.dgt1 = True
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
                self.dgt1 = False
                self.bonus = 0
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.bonus = 0
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.2
        self.bonus += 0.25
        print(self.bonus)

class Twilight:
    def __init__(self):
        self.hero = Hero(100,450,8.5,0.15,0.25,5,3,170,'Feu')
        self.atk1_d = [f'images/Jeu de combat/Twilight/Droite/Attaque1/_a_{i},60.png' for i in range(22)]
        self.atk1_g = [f'images/Jeu de combat/Twilight/Gauche/Attaque1/_a_{i},60.png' for i in range(22)]
        self.images_marche_d = [f'images/Jeu de combat/Twilight/Droite/Marche/_a_{i},60.png' for i in range(8)] 
        self.images_marche_g = [f'images/Jeu de combat/Twilight/Gauche/Marche/_a_{i},60.png' for i in range(8)]
        self.images_mort = [f'images/Jeu de combat/Twilight/Mort/_a_{i},60.png' for i in range(19)] 
        self.inaction_g = [f'images/Jeu de combat/Twilight/Gauche/Inaction/_a_{i},80.png' for i in range(14)]
        self.inaction_d = [f'images/Jeu de combat/Twilight/Droite/Inaction/_a_{i},80.png' for i in range(14)]
        self.image = 'images/Jeu de combat/Hero/Attaque/Attaque_Droite/Attaque1.png'
        self.dgt5 = pygame.image.load("images/Jeu de combat/-5.png")
        self.block = pygame.image.load("images/Jeu de combat/Block.png")
        self.frame = 0
        self.frame_mort = 0
        self.frame_parade = 0
        self.cd_dgt5 = 0
        self.cd_block_img = 0
        self.atk2 = False
        self.atk2 = False
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False

    def attaque(self,speed:float,sens,j2,multis):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if abs(distance(self, j2)) < self.hero.get_portee() and 9 <= int(self.frame) <= 16 and not j2.boss.get_block():
                aie_boss.play()
                j2.boss.modif_pv(-0.60*multis)
                j2.boss.set_poison(time.time())
            if self.frame >= len(self.atk1_d)-1:
                self.frame = 0
                self.hero.set_attaque(False)
            elif sens == 'Gauche':
                self.hero.modif_img(self.atk1_g[int(self.frame)])
            elif sens == 'Droite':
                self.hero.modif_img(self.atk1_d[int(self.frame)])
            self.frame += speed

    def mort(self,speed:float,j2):
        '''Permet de jouer l'animation de mort du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.hero.get_mort():
            # Faire progresser les images pour l'animation
            self.frame_mort += speed
            self.hero.modif_img(self.images_mort[int(self.frame_mort)])
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) == len(self.images_mort)-1:
                # On déclare le boss vainqueur, le combat prend fin
                self.hero.set_mort(True)
                j2.boss.set_victoire(True)

    def marche(self,speed:float,sens,j2):
        '''Permet de jouer l'animation de marche du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Si toutes les images ont été jouées :
        self.frame += speed
        if int(self.frame) >= len(self.images_marche_d)-1:
            # On remet tout à 0
            self.frame = 0
        # Faire progresser les images pour l'animation
        if sens == 'Gauche':
            self.hero.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.hero.modif_img(self.images_marche_d[int(self.frame)])

    def cp2(self, speed:float, sens, j2,multis):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.hero.set_cp2(False)
        return None
    
    def reset_frame(self):
        self.frame=0

    def inaction(self,j2):
        if int(self.frame) >= len(self.inaction_d)-1:
            # On remet tout à 0
            self.frame = 0
        if distance(self,j2) < 0:
            self.hero.modif_img(self.inaction_d[int(self.frame)])
        else:
            self.hero.modif_img(self.inaction_g[int(self.frame)])
        self.frame += 0.165

class Hell_Boss:
    def __init__(self):
        self.boss = Boss(140,0,50,470,1.2,0.1,2.5,4.5,0,'Nature',[pygame.image.load(f'images/Jeu de combat/Fonds/Lave/_a_frm{i},100.png') for i in range(8)],'Lave')
        self.images_coup_poing = [pygame.image.load(f'images/Jeu de combat/Boss/Attaque1/Coup_de_poing{i}.png') for i in range(1,6)]
        self.images_coup_faux = [pygame.image.load(f'images/Jeu de combat/Boss/Attaque2/Faux{i}.png') for i in range(1,8)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Boss/Marche/Droite/Marche{i}.png') for i in range(1,8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Boss/Marche/Gauche/Marche{i}.png') for i in range(1,8)]
        self.images_ulti = [pygame.image.load(f'images/Jeu de combat/Boss/Ulti/Ulti ({i}).png') for i in range(1,7)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Boss/Mort/Mort{i}.png') for i in range(1,8)]
        self.images_inaction = [f'images/Jeu de combat/Boss/Inaction/Inaction{i}.png' for i in range(1,4)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.ulti_anim = False
        self.atk1 = False
        self.atk2 = False
    def coup_de_poing(self,speed:float,j1):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        self.atk1 = True
        # Si toutes les images ont été jouées :
        if self.frame >= len(self.images_coup_poing)-1:
            # On remet tout à 0
            self.boss_sprite_attaque1 = 0
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            # Si le héros se trouve à portée du boss :
            if -230 < distance(j1,self) < 50 and not j1.hero.get_block():
                # Le héros perd 10 Pv
                j1.hero.modif_pv(-15)
                aie_hero.play()
                # Image des dégâts subis
                self.cd_dgt10 = time.time()
                print(f'Attaque coup de poing : Pv hero {j1.hero.get_pv()}')
            # Si le héros a bloqué l'attaque :
            if j1.hero.get_block():
                # Image du block
                j1.cd_block_img = time.time()
                print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        self.boss.modif_img(self.images_coup_poing[int(self.frame)])

    def faux(self,speed:float,j1):

        '''Permet de jouer l'attaque avec la faux du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 2 est en train d'être jouée.
        self.atk2= True
        # Si l'animation arrive au coup de l'attaque et que l'attaque n'a pas encore effectué ses dégâts :
        if self.frame >= len(self.images_coup_faux)-1:
            # Si le héros se trouve à portée du boss :
            if -230 < distance(j1,self) < 50 and not j1.hero.get_block():
                # Le héros perd 20 Pv
                j1.hero.modif_pv(-20)
                aie_hero.play()
                # Image des dégâts subis
                self.cd_dgt20 = time.time()
                print(f'Attaque faux : Pv hero : {j1.hero.get_pv()}')
            # Si le héros a bloqué l'attaque :
            elif j1.hero.get_block():
                # Image du block
                j1.cd_block_img = time.time()
                print("Bloqué !")
            # On remet tout à 0
            self.frame = 0
            self.atk2 = False
            self.boss.set_cd_attaque2()
            self.boss.set_attaque2_dispo(False)
        # Faire progresser les images pour l'animation
        self.frame += speed
        self.boss.modif_img(self.images_coup_faux[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])
    def ulti(self,speed:float,j1):
        '''Permet de jouer l'animation du l'ulti du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) > len(self.images_ulti):
            self.frame = 0
        # Animation de l'ulti du boss
        if int(self.frame) >= len(self.images_ulti)-1:
            # Effets de l'ulti du boss : Fait perdre 30 Pv au héros, et le boss regagne 30 Pv.
            self.boss.modif_pv(25)
            j1.hero.modif_pv(-10-j1.hero.get_pv()/4)
            # Image des dégâts subis
            self.cd_dgt20 = time.time()
            self.boss_sprite_ulti = 0
            self.boss.set_cd_ulti(0)
            self.ulti_anim = False
            print(f"Attaque Ultime ! : Pv héros : {j1.hero.get_pv()}")
            print(f"Attaque Ultime ! : Pv boss : {self.boss.get_pv()}")
        self.frame += speed
        self.boss.modif_img(self.images_ulti[int(self.frame)])
    def inaction(self,speed:float,sens):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction)-1:
            self.frame = 0
        self.frame += speed
        self.boss.modif_img(self.images_inaction[int(self.frame)])
    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
                self.atk2 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])
    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(0.08,'Gauche')
            self.boss.modif_pos_x(-1.5)
        elif distance(j1,self) > 0:
            self.marche(0.08,'Droite')
            self.boss.modif_pos_x(1.5)
    def patern_boss(self,xhero,j1):
        if self.boss.get_pv() <= 35:
            # Gestion de la guérison du boss à faible PV
            if self.boss.get_cd_ulti() == 0:
                self.boss.set_cd_ulti(time.time())
            elif time.time() - self.boss.get_cd_ulti() > 4:
                self.ulti_anim = True
                if self.boss.get_pos_x() < 900:
                    self.marche(0.1,'Droite')
                    self.boss.modif_pos_x(1.2)
                else:
                    self.ulti(0.08,j1)
        # Si le boss se trouve à portée, lancement des attaques
        if not self.ulti_anim:
            if self.atk1:
                self.coup_de_poing(0.12,j1)
            elif self.atk2:
                self.faux(0.12,j1)
            elif not self.atk1 and not self.atk2 and not -180 < distance(j1,self) < 50:
                # Sinon, déplacement pour être à portée du héros
                self.boss_vers_hero(j1)
            else:
                self.inaction(0.08,'bla')
            if -180 < distance(j1,self) < 50:
                if self.boss.get_attaque2_dispo() and not self.atk1:
                    if not self.atk2:
                        self.frame = 0
                    self.atk2 = True
                elif self.boss.get_attaque1_dispo() and not self.atk2:
                    if not self.atk1:
                        self.frame = 0
                    self.atk1 = True
            
class Michel:
    def __init__(self):
        self.boss = Boss(100,0,50,360,3,0.15,4,0,0,'Neutre',[pygame.image.load(f'images/Jeu de combat/Fonds/Chute/_a_frm{i},100.png') for i in range(4)],'Chute')
        self.images_attaque1 = [pygame.image.load(f'images/Jeu de combat/LancierBoss/Gauche/Attaque1/_a_frm{i},70.png') for i in range(44,69)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/LancierBoss/Droite/Marche/_a_frm{i},70.png') for i in range(16)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/LancierBoss/Gauche/Marche/_a_frm{i},70.png') for i in range(16)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/LancierBoss/Mort/_a_frm{i},70.png') for i in range(83,100)]
        self.images_inaction = [pygame.image.load(f'images/Jeu de combat/LancierBoss/Gauche/Inaction/_a_frm{i},70.png') for i in range(16,28)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
    def attaque1(self,speed:float,j1):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        self.atk1 = True
        # Si toutes les images ont été jouées :
        if self.frame >= len(self.images_attaque1)-1:
            if -160 < distance(j1,self) < 50 and not j1.hero.get_block():
                # Le héros perd 20 Pv
                j1.hero.modif_pv(-20)
                aie_hero.play()
                # Image des dégâts subis
                self.cd_dgt20 = time.time()
                print(f'Attaque2 : Pv hero : {j1.hero.get_pv()}')
            # On remet tout à 0
            self.boss_sprite_attaque1 = 0
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            # Si le héros se trouve à portée du boss :
        elif 3 <= self.frame <= 14:
            if -140 < distance(j1,self) < 100 and not j1.hero.get_block():
                # Le héros perd 10 Pv
                j1.hero.modif_pv(-0.2)
                # Image des dégâts subis
                self.cd_dgt10 = time.time()
                print(f'Attaque coup de poing : Pv hero {j1.hero.get_pv()}')
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        self.boss.modif_img(self.images_attaque1[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction)-1:
            self.frame = 0
        self.frame += speed
        self.boss.modif_img(self.images_inaction[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
                self.atk2 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            self.attaque1(0.12,j1)
        elif not self.atk1 and not self.atk2 and not -140 < distance(j1,self) < 50:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            self.inaction(0.12)
        if -140 < distance(j1,self) < 50:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True
                
class TankBoss:
    def __init__(self):
        self.boss = Boss(230,0,170,350,4.5,0.16,5.7,10,0,'Foudre',[pygame.image.load(f'images/Jeu de combat/Fonds/Lave/_a_frm{i},100.png') for i in range(8)],'Lave')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/ThunderBoss/Droite/Attaque1/_a_{i},60.png') for i in range(19)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/ThunderBoss/Gauche/Attaque1/_a_{i},60.png') for i in range(19)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/ThunderBoss/Droite/Marche/_a_{i},60.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/ThunderBoss/Gauche/Marche/_a_{i},60.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/ThunderBoss/Mort/_a_{i},60.png') for i in range(15)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/ThunderBoss/Droite/Inaction/_a_{i},80.png') for i in range(15)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/ThunderBoss/Gauche/Inaction/_a_{i},80.png') for i in range(15)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False

    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
            - j1 : le joueur
            - s : le sens de l'attaque
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
            # Réinitialiser le dictionnaire des dégâts par frame au début de l'attaque
            self.frames_degats = {}
        self.atk1 = True
        frame_actuelle = int(self.frame)
        if not j1.hero.get_block():
            # Si le joueur est à portée et que cette frame n'a pas encore infligé de dégâts
            if self.sens == 'Gauche' and -self.boss.get_portee() < distance(j1, self) < 0 or self.sens == 'Droite' and 0 < distance(j1, self) < self.boss.get_portee() and frame_actuelle not in self.frames_degats.keys():
                # Infliger des dégâts différents selon la frame
                degats = 0  # Dégâts de base
                if frame_actuelle == 8:
                    degats = 22
                    aie_hero.play()
                if 8 < frame_actuelle < 14:  # Frames spéciales avec plus de dégâts
                    degats = randint(4,8)
                    aie_hero.play()
                j1.hero.modif_pv(-degats)
                # Marquer cette frame comme ayant infligé des dégâts
                self.frames_degats[frame_actuelle] = True
                print(f"Dégâts infligés à la frame {frame_actuelle}: -{degats} PV")
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            # Réinitialiser le dictionnaire des dégâts
            self.frames_degats = {}
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])
            
    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
                self.atk2 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo():
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Cindera:
    def __init__(self):
        self.boss = Boss(160,0,50,400,4,0.15,4.5,0,0,'Feu',[pygame.image.load(f'images/Jeu de combat/Fonds/Lave/_a_frm{i},100.png') for i in range(8)],'Lave')
        self.images_attaque1 = [pygame.image.load(f'images/Jeu de combat/Cindera/Gauche/Attaque1/_a_{i},100.png') for i in range(40)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Cindera/Droite/Marche/_a_frm{i},0.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Cindera/Gauche/Marche/_a_frm{i},0.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Cindera/Mort/_a_frm{i},0.png') for i in range(26)]
        self.images_inaction = [pygame.image.load(f'images/Jeu de combat/Cindera/Gauche/Inaction/_a_frm{i},0.png') for i in range(12)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.ralenti = False
    def attaque1(self,speed:float,j1):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        self.atk1 = True
        # Si toutes les images ont été jouées :
        if self.frame >= len(self.images_attaque1)-1:
            if abs(distance(j1,self)) < 180 and not j1.hero.get_block():
                # Le héros perd 20 Pv
                j1.hero.modif_pv(-90)
                aie_hero.play()
                # Image des dégâts subis
                self.cd_dgt20 = time.time()
                print(f'Attaque2 : Pv hero : {j1.hero.get_pv()}')
            # On remet tout à 0
            self.boss_sprite_attaque1 = 0
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            # Si le héros se trouve à portée du boss :
        elif 5 <= self.frame:
            if abs(distance(j1,self)) < 220 and not j1.hero.get_block():
                j1.hero.modif_pv(-0.28)
                print(f'Fournaise : Pv hero {j1.hero.get_pv()}')
                if not self.ralenti:
                    j1.hero.set_speed(j1.hero.get_speed()*0.6)
                    self.ralenti = True
            elif self.ralenti:
                self.ralenti = False
                j1.hero.set_speed(j1.hero.get_speed()/0.6)
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        self.boss.modif_img(self.images_attaque1[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            self.attaque1(0.15,j1)
        elif not self.atk1 and not self.atk2 and not abs(distance(j1,self)) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            self.inaction(0.12)
        if abs(distance(j1,self)) < 140:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class DarkLord:
    def __init__(self):
        self.boss = Boss(160,0,50,450,4,0.16,2.8,10,0,'Nuit',[pygame.image.load(f'images/Jeu de combat/Fonds/Pluie/_a_frm{i},120.png') for i in range(8)],'Pluie')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/DarkLord/Droite/Attaque1/_a_frm{i},0.png') for i in range(23)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/DarkLord/Gauche/Attaque1/_a_frm{i},0.png') for i in range(23)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/DarkLord/Droite/Marche/_a_frm{i},0.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/DarkLord/Gauche/Marche/_a_frm{i},0.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/DarkLord/Mort/_a_frm{i},0.png') for i in range(20)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/DarkLord/Droite/Inaction/_a_frm{i},0.png') for i in range(16)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/DarkLord/Gauche/Inaction/_a_frm{i},0.png') for i in range(16)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        # Si toutes les images ont été jouées :
        if self.frame >= len(self.images_attaque1_d)-1:
            if 60 < abs(distance(j1,self)) < 220 and not j1.hero.get_block():
                # Le héros perd 20 Pv
                j1.hero.modif_pv(-55)
                aie_hero.play()
                # Image des dégâts subis
                self.cd_dgt20 = time.time()
                print(f'Attaque2 : Pv hero : {j1.hero.get_pv()}')
            # On remet tout à 0
            self.boss_sprite_attaque1 = 0
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Astral:
    def __init__(self):
        self.boss = Boss(160,0,50,440,4,0.16,3.2,10,0,'Esprit',[pygame.image.load(f'images/Jeu de combat/Fonds/Eglise/_a_frm{i},150.png') for i in range(8)],'Eglise')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Astral/Droite/Attaque1/_a_{i},100.png') for i in range(29)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Astral/Gauche/Attaque1/_a_{i},100.png') for i in range(29)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Astral/Droite/Marche/_a_{i},100.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Astral/Gauche/Marche/_a_{i},100.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Astral/Mort/_a_frm{i},100.png') for i in range(12)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Astral/Droite/Inaction/_a_frm{i},100.png') for i in range(12)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Astral/Gauche/Inaction/_a_frm{i},100.png') for i in range(12)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        # Si toutes les images ont été jouées :
        if self.frame >= len(self.images_attaque1_d)-1:
            if abs(distance(j1,self)) < 220 and not j1.hero.get_block():
                aie_hero.play()
                j1.hero.set_poison(time.time())
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
        if abs(distance(j1,self)) < 220 and not j1.hero.get_block() and 16 <= self.frame <= 25:
                # Le héros perd 20 Pv
                j1.hero.modif_pv(-0.5)
                aie_hero.play()
                # Image des dégâts subis
                self.cd_dgt20 = time.time()
                print(f'Attaque2 : Pv hero : {j1.hero.get_pv()}')
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not -170 < distance(j1,self) < 170:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -170 < distance(j1,self) < 170:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class EternityPainter:
    def __init__(self):
        self.boss = Boss(150,0,160,495,4,0.16,3.2,10,0,'Esprit',[pygame.image.load(f'images/Jeu de combat/Fonds/Chute/_a_frm{i},100.png') for i in range(4)],'Chute')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Ep/Droite/Attaque1/_a_frm{i},60.png') for i in range(23)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Ep/Gauche/Attaque1/_a_frm{i},60.png') for i in range(23)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Ep/Droite/Marche/_a_frm{i},60.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Ep/Gauche/Marche/_a_frm{i},60.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Ep/Mort/_a_frm{i},60.png') for i in range(11)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Ep/Droite/Inaction/_a_frm{i},80.png') for i in range(12)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Ep/Gauche/Inaction/_a_frm{i},80.png') for i in range(12)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 5:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-8)
                    self.dgt1 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 11:
                if not self.dgt2:
                    aie_hero.play()
                    j1.hero.modif_pv(-10)
                    self.dgt2 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 17:
                if not self.dgt3:
                    aie_hero.play()
                    j1.hero.modif_pv(-20)
                    self.dgt3 = True    
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            self.dgt2 = False
            self.dgt3 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not abs(distance(j1,self)) < self.boss.get_portee()*0.7:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if abs(distance(j1,self)) < self.boss.get_portee():
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Shidai:
    def __init__(self):
        self.boss = Boss(180,0,160,445,4,0.16,2.8,4,0,'Air',[pygame.image.load(f'images/Jeu de combat/Fonds/Dojo/_a_frm{i},100.png') for i in range(48)],'Dojo')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Shidai/Droite/Attaque1/_a_{i},60.png') for i in range(20)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Shidai/Gauche/Attaque1/_a_{i},60.png') for i in range(20)]
        self.cp2_d = [pygame.image.load(f'images/Jeu de combat/Shidai/Droite/Attaque2/_a_{i},60.png') for i in range(6)]
        self.cp2_g = [pygame.image.load(f'images/Jeu de combat/Shidai/Gauche/Attaque2/_a_{i},60.png') for i in range(6)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Shidai/Droite/Marche/_a_frm{i},60.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Shidai/Gauche/Marche/_a_frm{i},60.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Shidai/Mort/_a_{i},60.png') for i in range(18)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Shidai/Droite/Inaction/_a_{i},80.png') for i in range(14)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Shidai/Gauche/Inaction/_a_{i},80.png') for i in range(14)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.bonus = 0
        self.pv_actuels = self.boss.get_pv()
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 3:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-10-self.bonus/3)
                    self.dgt1 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 6:
                if not self.dgt2:
                    aie_hero.play()
                    j1.hero.modif_pv(-10-self.bonus/3)
                    self.dgt2 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 13:
                if not self.dgt3:
                    aie_hero.play()
                    j1.hero.modif_pv(-20-self.bonus/3)
                    self.dgt3 = True    
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            self.dgt2 = False
            self.dgt3 = False
            self.bonus = 0
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def cp2(self, speed:float, sens, j1):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.atk2 = True
        if self.boss.get_pv() > 0:
            if self.frame >= len(self.cp2_d)-1:
                self.frame = 0
            if self.pv_actuels != self.boss.get_pv() or self.boss.get_pv() < 0:
                self.frame = 0
                self.boss.set_cd_attaque2()
                self.boss.set_attaque2_dispo(False)
                self.atk2 = False
            if sens == 'Gauche':
                self.boss.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.boss.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
            self.bonus += 0.05
            print(self.bonus)

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif self.atk2:
            if distance(j1,self) < 0:
                self.cp2(0.18,'Gauche',j1)
            else:
                self.cp2(0.18,'Droite',j1)
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True
        if self.boss.get_attaque2_dispo() and not self.atk1 and -320 < distance(j1,self) < 320:
                if not self.atk2:
                    self.frame = 0
                    self.pv_actuels = self.boss.get_pv()
                self.atk2 = True

class Lilithe:
    def __init__(self):
        self.boss = Boss(180,0,180,455,4,0.16,5,7,2.5,'Feu',[pygame.image.load(f'images/Jeu de combat/Fonds/Lave/_a_frm{i},100.png') for i in range(8)],'Lave')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Lilithe/Droite/Attaque1/_a_{i},100.png') for i in range(12)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Lilithe/Gauche/Attaque1/_a_{i},100.png') for i in range(12)]
        self.images_attaque2_d = [pygame.image.load(f'images/Jeu de combat/Lilithe/Droite/Attaque2/_a_{i},70.png') for i in range(25)]
        self.images_attaque2_g = [pygame.image.load(f'images/Jeu de combat/Lilithe/Gauche/Attaque2/_a_{i},70.png') for i in range(25)]
        self.cp2_d = [pygame.image.load(f'images/Jeu de combat/Lilithe/Droite/Attaque3/_a_{i},70.png') for i in range(14)]
        self.cp2_g = [pygame.image.load(f'images/Jeu de combat/Lilithe/Gauche/Attaque3/_a_{i},70.png') for i in range(14)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Lilithe/Droite/Marche/_a_frm{i},70.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Lilithe/Gauche/Marche/_a_frm{i},70.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Lilithe/Mort/_a_{i},70.png') for i in range(20)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Lilithe/Droite/Inaction/_a_{i},80.png') for i in range(20)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Lilithe/Gauche/Inaction/_a_{i},80.png') for i in range(20)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.atk3 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.bonus = 0
        self.pv_actuels = 160

    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 6:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-8)
                    self.dgt1 = True
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def attaque2(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk2 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 6:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-10-self.bonus/2)
                    self.dgt1 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 17:
                if not self.dgt2:
                    aie_hero.play()
                    j1.hero.modif_pv(-20-self.bonus/2)
                    self.dgt2 = True
        if self.frame >= len(self.images_attaque2_d)-1:
            self.boss.set_cd_attaque2()
            self.boss.set_attaque2_dispo(False)
            self.atk2 = False
            self.dgt1 = False
            self.dgt2 = False
            self.bonus = 0
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque2_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque2_d[int(self.frame)])

    def cp2(self, speed:float, sens, j1):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.atk3 = True
        if self.boss.get_pv() > 0:
            if self.frame >= len(self.cp2_d)-1:
                self.frame = 0
            if self.pv_actuels != self.boss.get_pv()or self.boss.get_pv() < 0:
                self.frame = 0
                self.boss.set_cd_attaque3()
                self.boss.set_attaque3_dispo(False)
                self.atk3 = False
            if sens == 'Gauche':
                self.boss.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.boss.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
            self.bonus += 0.12

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif self.atk2:
            if distance(j1,self) < 0:
                self.attaque2(0.18,j1,'Gauche')
            else:
                self.attaque2(0.18,j1,'Droite')
        elif self.atk3:
            if distance(j1,self) < 0:
                self.cp2(0.18,'Gauche',j1)
            else:
                self.cp2(0.18,'Droite',j1)
        elif not self.atk1 and not self.atk2 and not self.atk3 and not abs(distance(j1,self)) < self.boss.get_portee():
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if  abs(distance(j1,self)) < self.boss.get_portee():
            if self.boss.get_attaque1_dispo() and not self.atk2 and not self.atk3:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True
            if self.boss.get_attaque2_dispo() and not self.atk1 and not self.atk3:
                if not self.atk2:
                    self.frame = 0
                self.atk2 = True
        if self.boss.get_attaque3_dispo() and not self.atk1 and not self.atk2 and abs(distance(j1,self)) < 400:
                if not self.atk3:
                    self.frame = 0
                    self.pv_actuels = self.boss.get_pv()
                self.atk3 = True

class Solfist:
    def __init__(self):
        self.boss = Boss(230,0,160,450,4,0.16,4.5,10,0,'Feu',[pygame.image.load(f'images/Jeu de combat/Fonds/Lave/_a_frm{i},100.png') for i in range(8)],'Lave')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Solfist/Droite/Attaque1/_a_{i},100.png') for i in range(41)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Solfist/Gauche/Attaque1/_a_{i},100.png') for i in range(41)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Solfist/Droite/Marche/_a_{i},100.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Solfist/Gauche/Marche/_a_{i},100.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Solfist/Mort/_a_{i},100.png') for i in range(25)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Solfist/Droite/Inaction/_a_{i},100.png') for i in range(12)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Solfist/Gauche/Inaction/_a_{i},100.png') for i in range(12)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            if 7 <= int(self.frame) <= 18:
                if self.sens == 'Gauche' and -self.boss.get_portee() < distance(j1, self) < 0 or self.sens == 'Droite' and 0 < distance(j1, self) < self.boss.get_portee():
                    aie_hero.play()
                    j1.hero.modif_pv(-0.4)
            elif int(self.frame) == 30:
                if self.sens == 'Gauche' and -self.boss.get_portee() < distance(j1, self) < 0 or self.sens == 'Droite' and 0 < distance(j1, self) < self.boss.get_portee():
                    if not self.dgt2:
                        aie_hero.play()
                        j1.hero.modif_pv(-45)
                        self.dgt2 = True  
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt2 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not abs(distance(j1,self)) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if abs(distance(j1,self)) < 140:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Elyx:
    def __init__(self):
        self.boss = Boss(220,0,160,470,3.5,0.16,5,10,0,'Neutre',[pygame.image.load(f'images/Jeu de combat/Fonds/Lave/_a_frm{i},100.png') for i in range(8)],'Lave')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Elyx/Droite/Attaque1/_a_{i},100.png') for i in range(12)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Elyx/Gauche/Attaque1/_a_{i},100.png') for i in range(12)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Elyx/Droite/Marche/_a_{i},100.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Elyx/Gauche/Marche/_a_{i},100.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Elyx/Mort/_a_{i},100.png') for i in range(11)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Elyx/Droite/Inaction/_a_{i},100.png') for i in range(11)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Elyx/Gauche/Inaction/_a_{i},100.png') for i in range(11)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if int(self.frame) == 7 and not self.dgt2:
                if self.sens == 'Gauche' and -self.boss.get_portee() < distance(j1, self) < 0 or self.sens == 'Droite' and 0 < distance(j1, self) < self.boss.get_portee():
                    aie_hero.play()
                    j1.hero.modif_pv(-18)
                    self.dgt2 = True
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt2 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens,j1):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if abs(distance(j1,self)) <= 150 and not self.dgt3:
            j1.hero.modif_pv(-10)
            j1.hero.set_stun(True)
            j1.hero.set_speed(0)
            self.boss.set_cd_attaque2()
            self.dgt3 = True
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche',j1)
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite',j1)
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if 1 < self.boss.get_cd_attaque2() < 1.5 :
            j1.hero.set_stun(False)
            j1.hero.set_speed(j1.hero.get_speed_base())
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not abs(distance(j1,self)) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
            self.boss.set_block(True)
        else:
            self.boss.set_block(False)
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if abs(distance(j1,self)) < 140:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                self.dgt3 = False
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Embla:
    def __init__(self):
        self.boss = Boss(150,0,180,440,4,0.16,2.8,4,0,'Glace',[pygame.image.load(f'images/Jeu de combat/Fonds/Temple/_a_frm{i},100.png') for i in range(8)],'Temple')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Embla/Droite/Attaque1/_a_{i},60.png') for i in range(38)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Embla/Gauche/Attaque1/_a_{i},60.png') for i in range(38)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Embla/Droite/Marche/_a_{i},60.png') for i in range(10)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Embla/Gauche/Marche/_a_{i},60.png') for i in range(10)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Embla/Mort/_a_frm{i},60.png') for i in range(12)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Embla/Droite/Inaction/_a_{i},80.png') for i in range(18)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Embla/Gauche/Inaction/_a_{i},80.png') for i in range(18)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.pv_actuels = self.boss.get_pv()
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 7:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-12)
                    self.dgt1 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 14:
                if not self.dgt2:
                    aie_hero.play()
                    j1.hero.modif_pv(-12)
                    self.dgt2 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 27:
                if not self.dgt3:
                    aie_hero.play()
                    j1.hero.modif_pv(-35)
                    self.dgt3 = True    
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            self.dgt2 = False
            self.dgt3 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo():
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Sun:
    def __init__(self):
        self.boss = Boss(180,0,160,450,4,0.16,5,10,0,'Feu',[pygame.image.load(f'images/Jeu de combat/Fonds/Lave/_a_frm{i},100.png') for i in range(8)],'Lave')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Sun/Droite/Attaque1/_a_{i},100.png') for i in range(33)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Sun/Gauche/Attaque1/_a_{i},100.png') for i in range(33)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Sun/Droite/Marche/_a_{i},100.png') for i in range(5)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Sun/Gauche/Marche/_a_{i},100.png') for i in range(5)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Sun/Mort/_a_{i},100.png') for i in range(17)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Sun/Droite/Inaction/_a_{i},100.png') for i in range(26)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Sun/Gauche/Inaction/_a_{i},100.png') for i in range(26)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            if int(self.frame) == 19:
                if abs(distance(j1, self)) < self.boss.get_portee():
                    if not self.dgt1:
                        aie_hero.play()
                        j1.hero.modif_pv(-35)
                        self.dgt1 = True  
            elif int(self.frame) == 20:
                if abs(distance(j1, self)) < self.boss.get_portee():
                    if not self.dgt2:
                        aie_hero.play()
                        j1.hero.modif_pv(-45)
                        self.dgt2 = True  
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            self.dgt2 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not abs(distance(j1,self)) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if abs(distance(j1,self)) < 140:
            if self.boss.get_attaque1_dispo() and not self.atk2:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Skurge:
    def __init__(self):
        self.boss = Boss(140,0,160,510,5,0.16,6.5,10,0,'Nature',[pygame.image.load(f'images/Jeu de combat/Fonds/Chute/_a_frm{i},100.png') for i in range(4)],'Chute')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Skurge/Droite/Attaque1/_a_{i},100.png') for i in range(14)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Skurge/Gauche/Attaque1/_a_{i},100.png') for i in range(14)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Skurge/Droite/Marche/_a_{i},100.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Skurge/Gauche/Marche/_a_{i},100.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Skurge/Mort/_a_{i},100.png') for i in range(9)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Skurge/Droite/Inaction/_a_{i},100.png') for i in range(11)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Skurge/Gauche/Inaction/_a_{i},100.png') for i in range(11)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = pygame.image.load('images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png')
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.versladroite = False
        self.verslagauche = False
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if int(self.frame) == 9 and not j1.hero.get_block():
            print(self.sens, distance(j1,self))
            if not self.dgt1 and self.sens == 'Gauche' and distance(j1,self) < 0 or not self.dgt1 and self.sens == 'Droite' and distance(j1,self) > 0:
                aie_hero.play()
                dgt = choice([40,40,40,40,80])
                if dgt == 80:
                    print("Coup critique !")
                j1.hero.modif_pv(-dgt)
                self.dgt1 = True  
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) > 0:
            if self.boss.get_pos_x() < 200:
                self.versladroite = True
            else:
                self.marche(self.boss.get_speed_anim(),'Gauche')
                self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) < 0:
            if self.boss.get_pos_x() > 1000:
                self.verslagauche = True
            else:
                self.marche(self.boss.get_speed_anim(),'Droite')
                self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        if self.boss.get_attaque1_dispo():
            if not self.atk1:
                self.frame = 0
            self.atk1 = True
        elif not self.atk1 and abs(distance(j1,self)) < 250:
            # Sinon, déplacement pour être à portée du héros
            if self.versladroite:
                self.marche(self.boss.get_speed_anim(),'Droite')
                self.boss.modif_pos_x(self.boss.get_speed())
            elif self.verslagauche:
                self.marche(self.boss.get_speed_anim(),'Gauche')
                self.boss.modif_pos_x(-self.boss.get_speed())
            else:
                self.boss_vers_hero(j1)
        else:
            self.versladroite = False
            self.verslagauche = False
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')

class NoshRak:
    def __init__(self):
        self.boss = Boss(150,0,180,470,4,0.16,2.8,4,0,'Foudre',[pygame.image.load(f'images/Jeu de combat/Fonds/Desert/_a_frm{i},80.png') for i in range(8)],'Desert')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Nosh-Rak/Droite/Attaque1/_a_{i},60.png') for i in range(35)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Nosh-Rak/Gauche/Attaque1/_a_{i},60.png') for i in range(35)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Nosh-Rak/Droite/Marche/_a_{i},60.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Nosh-Rak/Gauche/Marche/_a_{i},60.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Nosh-Rak/Mort/_a_{i},60.png') for i in range(24)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Nosh-Rak/Droite/Inaction/_a_{i},80.png') for i in range(20)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Nosh-Rak/Gauche/Inaction/_a_{i},80.png') for i in range(20)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.pv_actuels = self.boss.get_pv()
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 2:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-8)
                    self.dgt1 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 8:
                if not self.dgt2:
                    aie_hero.play()
                    j1.hero.modif_pv(-8)
                    self.dgt2 = True
                    if self.dgt1:
                        j1.hero.set_stun(True)
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 23:
                if not self.dgt3:
                    aie_hero.play()
                    j1.hero.modif_pv(-30)
                    self.dgt3 = True    
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            self.dgt2 = False
            self.dgt3 = False
            j1.hero.set_stun(False)
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.frame >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo():
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Purgatos:
    def __init__(self):
        self.boss = Boss(150,0,180,420,4,0.16,2.0,0,0,'Esprit',[pygame.image.load(f'images/Jeu de combat/Fonds/Eglise/_a_frm{i},150.png') for i in range(8)],'Desert')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Purgatos/Droite/Attaque1/_a_{i},100.png') for i in range(23)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Purgatos/Gauche/Attaque1/_a_{i},100.png') for i in range(23)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Purgatos/Droite/Marche/_a_{i},100.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Purgatos/Gauche/Marche/_a_{i},100.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Purgatos/Mort/_a_{i},100.png') for i in range(17)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Purgatos/Droite/Inaction/_a_{i},100.png') for i in range(14)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Purgatos/Gauche/Inaction/_a_{i},100.png') for i in range(14)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.pv_actuels = self.boss.get_pv()
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if self.sens == 'Gauche' and -self.boss.get_portee() < distance(j1, self) < 0 or self.sens == 'Droite' and 0 < distance(j1, self) < self.boss.get_portee():
                if int(self.frame) == 15:
                    if not self.dgt1:
                        aie_hero.play()
                        j1.hero.modif_pv(-35)
                        self.dgt1 = True 
                        j1.hero.set_poison(True)
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            j1.hero.set_stun(False)
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.frame >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.25,j1,'Gauche')
            else:
                self.attaque1(0.25,j1,'Droite')
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo():
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Ciphyron:
    def __init__(self):
        self.boss = Boss(150,0,180,420,4,0.16,2.0,0,0,'Foudre',[pygame.image.load(f'images/Jeu de combat/Fonds/Desert/_a_frm{i},80.png') for i in range(8)],'Desert')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Ciphyron/Droite/Attaque1/_a_{i},60.png') for i in range(22)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Ciphyron/Gauche/Attaque1/_a_{i},60.png') for i in range(22)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Ciphyron/Droite/Marche/_a_{i},60.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Ciphyron/Gauche/Marche/_a_{i},60.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Ciphyron/Mort/_a_{i},60.png') for i in range(17)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Ciphyron/Droite/Inaction/_a_{i},80.png') for i in range(16)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Ciphyron/Gauche/Inaction/_a_{i},80.png') for i in range(16)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.dgt4 = False
        self.pv_actuels = self.boss.get_pv()
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and not j1.hero.get_block():
                if int(self.frame) == 9:
                    if not self.dgt1:
                        aie_hero.play()
                        j1.hero.modif_pv(-10)
                        self.dgt1 = True 
                elif int(self.frame) == 10:
                    if not self.dgt2:
                        aie_hero.play()
                        j1.hero.modif_pv(-5)
                        self.dgt2 = True 
                elif int(self.frame) == 14:
                    if not self.dgt3:
                        aie_hero.play()
                        j1.hero.modif_pv(-10)                       
                        self.dgt3 = True 
                        j1.hero.set_stun(True)
                elif int(self.frame) == 15:
                    if not self.dgt4:
                        aie_hero.play()
                        j1.hero.modif_pv(-5)
                        self.dgt4 = True 
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            self.dgt2 = False
            self.dgt3 = False
            self.dgt4 = False
            j1.hero.set_stun(False)
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.frame >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.25,j1,'Gauche')
            else:
                self.attaque1(0.25,j1,'Droite')
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo():
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Golem:
    def __init__(self):
        self.boss = Boss(350,0,180,357,2.8,0.16,6.8,4,0,'Foudre',[pygame.image.load(f'images/Jeu de combat/Fonds/Temple/_a_frm{i},100.png') for i in range(8)],'Temple')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Golem/Droite/Attaque1/_a_{i},70.png') for i in range(28)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Golem/Gauche/Attaque1/_a_{i},70.png') for i in range(28)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Golem/Droite/Marche/_a_{i},70.png') for i in range(12)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Golem/Gauche/Marche/_a_{i},70.png') for i in range(12)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Golem/Mort/_a_{i},70.png') for i in range(20)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Golem/Droite/Inaction/_a_{i},80.png') for i in range(16)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Golem/Gauche/Inaction/_a_{i},80.png') for i in range(16)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.pv_actuels = self.boss.get_pv()
    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
            - j1 : le joueur
            - s : le sens de l'attaque
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
            # Réinitialiser le dictionnaire des dégâts par frame au début de l'attaque
            self.frames_degats = {}
            
        self.atk1 = True
        frame_actuelle = int(self.frame)
        
        if not j1.hero.get_block():
            # Si le joueur est à portée et que cette frame n'a pas encore infligé de dégâts
            if abs(distance(j1, self)) < self.boss.get_portee() and frame_actuelle not in self.frames_degats:
                # Infliger des dégâts différents selon la frame
                degats = 0  # Dégâts de base
                if frame_actuelle == 10:
                    degats = 20
                    aie_hero.play()
                elif frame_actuelle == 12:
                    degats = 25
                    aie_hero.play()
                if 13 < frame_actuelle < 22:  # Frames spéciales avec plus de dégâts
                    degats = randint(1,8)
                
                j1.hero.modif_pv(-degats)
                # Marquer cette frame comme ayant infligé des dégâts
                self.frames_degats[frame_actuelle] = True
                print(f"Dégâts infligés à la frame {frame_actuelle}: -{degats} PV")
        
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            # Réinitialiser le dictionnaire des dégâts
            self.frames_degats = {}
            
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
            
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif not self.atk1 and not -140 < distance(j1,self) < 140:
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if -140 < distance(j1,self) < 140:
            if self.boss.get_attaque1_dispo():
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True

class Soji:
    def __init__(self):
        self.boss = Boss(210,0,140,480,4,0.16,5,7,4.5,'Foudre',[pygame.image.load(f'images/Jeu de combat/Fonds/Desert/_a_frm{i},80.png') for i in range(8)],'Desert')
        self.images_attaque1_d = [pygame.image.load(f'images/Jeu de combat/Soji/Droite/Attaque1/_a_{i},100.png') for i in range(22)]
        self.images_attaque1_g = [pygame.image.load(f'images/Jeu de combat/Soji/Gauche/Attaque1/_a_{i},100.png') for i in range(22)]
        self.images_attaque2_d = [pygame.image.load(f'images/Jeu de combat/Soji/Droite/Attaque2/_a_{i},70.png') for i in range(25)]
        self.images_attaque2_g = [pygame.image.load(f'images/Jeu de combat/Soji/Gauche/Attaque2/_a_{i},70.png') for i in range(25)]
        self.cp2_d = [pygame.image.load(f'images/Jeu de combat/Soji/Droite/Attaque3/_a_{i},70.png') for i in range(12)]
        self.cp2_g = [pygame.image.load(f'images/Jeu de combat/Soji/Gauche/Attaque3/_a_{i},70.png') for i in range(12)]
        self.images_marche_d = [pygame.image.load(f'images/Jeu de combat/Soji/Droite/Marche/_a_{i},70.png') for i in range(8)]
        self.images_marche_g = [pygame.image.load(f'images/Jeu de combat/Soji/Gauche/Marche/_a_{i},70.png') for i in range(8)]
        self.images_mort = [pygame.image.load(f'images/Jeu de combat/Soji/Mort/_a_{i},70.png') for i in range(19)]
        self.images_inaction_d = [pygame.image.load(f'images/Jeu de combat/Soji/Droite/Inaction/_a_{i},80.png') for i in range(14)]
        self.images_inaction_g = [pygame.image.load(f'images/Jeu de combat/Soji/Gauche/Inaction/_a_{i},80.png') for i in range(14)]
        self.dgt10 = pygame.image.load("images/Jeu de combat/-10.png")
        self.dgt20 = pygame.image.load("images/Jeu de combat/-20.png")
        self.image = 'images/Jeu de combat/Boss/Attaque1/Coup_de_poing1.png'
        self.cd_dgt10 = 0
        self.cd_dgt20 = 0
        self.frame = 0
        self.frame_mort = 0
        self.atk1 = False
        self.atk2 = False
        self.atk3 = False
        self.sens = 'Droite'
        self.dgt1 = False
        self.dgt2 = False
        self.dgt3 = False
        self.bonus = 0
        self.pv_actuels = 160

    def attaque1(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk1 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 8:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-5)
                    self.dgt1 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 17:
                if not self.dgt2:
                    aie_hero.play()
                    j1.hero.modif_pv(-25)
                    self.dgt2 = True
        if self.frame >= len(self.images_attaque1_d)-1:
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            self.dgt1 = False
            self.dgt2 = False
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque1_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque1_d[int(self.frame)])

    def attaque2(self,speed:float,j1,s):
        '''Permet de jouer l'attaque au poing du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # L'attaque 1 est en train d'être jouée.
        if self.frame < 1:
            self.sens = s
        self.atk2 = True
        if not j1.hero.get_block():
            # Si toutes les images ont été jouées :
            if abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 7:
                if not self.dgt1:
                    aie_hero.play()
                    j1.hero.modif_pv(-10-self.bonus/3)
                    self.dgt1 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 11:
                if not self.dgt2:
                    aie_hero.play()
                    j1.hero.modif_pv(-10-self.bonus/3)
                    self.dgt2 = True
            elif abs(distance(j1, self)) < self.boss.get_portee() and int(self.frame) == 16:
                if not self.dgt3:
                    aie_hero.play()
                    j1.hero.modif_pv(-30-self.bonus/3)
                    self.dgt3 = True
        if self.frame >= len(self.images_attaque2_d)-1:
            self.boss.set_cd_attaque2()
            self.boss.set_attaque2_dispo(False)
            self.atk2 = False
            self.dgt1 = False
            self.dgt2 = False
            self.dgt3 = False
            self.bonus = 0
        # Si le héros a bloqué l'attaque :
        if j1.hero.get_block():
            # Image du block
            j1.cd_block_img = time.time()
            print("Bloqué !")
        # Faire progresser les images pour l'animation
        self.frame += speed        
        if self.sens == 'Gauche':
            self.boss.modif_img(self.images_attaque2_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_attaque2_d[int(self.frame)])

    def cp2(self, speed:float, sens, j1):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        self.atk3 = True
        if self.boss.get_pv() > 0:
            if self.frame >= len(self.cp2_d)-1:
                self.frame = 0
            if self.pv_actuels != self.boss.get_pv() or self.boss.get_pv() < 0:
                self.frame = 0
                self.boss.set_cd_attaque3()
                self.boss.set_attaque3_dispo(False)
                self.atk3 = False
            if sens == 'Gauche':
                self.boss.modif_img(self.cp2_g[int(self.frame)])
            else:
                self.boss.modif_img(self.cp2_d[int(self.frame)])
            # Faire progresser les images pour l'animation
            self.frame += speed
            self.bonus += 0.18

    def marche(self,speed:float,sens):
        '''Permet de jouer l'animation de marche (vers la gauche) du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_marche_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_marche_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_marche_d[int(self.frame)])

    def inaction(self,speed:float,sens='Gauche'):
        '''Permet de jouer l'animation d'inaction du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if int(self.frame) >= len(self.images_inaction_d)-1:
            self.frame = 0
        self.frame += speed
        if sens == 'Gauche':
            self.boss.modif_img(self.images_inaction_g[int(self.frame)])
        else:
            self.boss.modif_img(self.images_inaction_d[int(self.frame)])

    def mort(self,speed:float,j1):
        '''Permet de jouer l'animation de mort du Boss.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        # Permet d'attendre la fin de l'animation de mort pour mettre fin au combat
        if not self.boss.get_mort():
            # Si toutes les images ont été jouées :
            if int(self.frame_mort) >= len(self.images_mort)-1:
                self.boss.set_mort(True)
                # On déclare le héros vainqueur, le combat prend fin
                j1.hero.set_victoire(True)
                self.frame_mort = 0
                self.frame = 0
                self.atk1 = False
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])

    def boss_vers_hero(self,j1):
        if distance(j1,self) < 0:
            self.marche(self.boss.get_speed_anim(),'Gauche')
            self.boss.modif_pos_x(-self.boss.get_speed())
        elif distance(j1,self) > 0:
            self.marche(self.boss.get_speed_anim(),'Droite')
            self.boss.modif_pos_x(self.boss.get_speed())

    def patern_boss(self,xhero,j1):
        # Si le boss se trouve à portée, lancement des attaques
        if self.atk1:
            if distance(j1,self) < 0:
                self.attaque1(0.18,j1,'Gauche')
            else:
                self.attaque1(0.18,j1,'Droite')
        elif self.atk2:
            if distance(j1,self) < 0:
                self.attaque2(0.18,j1,'Gauche')
            else:
                self.attaque2(0.18,j1,'Droite')
        elif self.atk3:
            if distance(j1,self) < 0:
                self.cp2(0.18,'Gauche',j1)
            else:
                self.cp2(0.18,'Droite',j1)
            if abs(distance(j1,self)) < self.boss.get_portee() and self.bonus >= 25:
                self.frame = 0
                self.boss.set_cd_attaque3()
                self.boss.set_attaque3_dispo(False)
                self.atk3 = False
        elif not self.atk1 and not self.atk2 and not self.atk3 and not abs(distance(j1,self)) < self.boss.get_portee():
            # Sinon, déplacement pour être à portée du héros
            self.boss_vers_hero(j1)
        else:
            if distance(j1,self) < 0:
                self.inaction(0.14,'Gauche')
            else:
                self.inaction(0.14,'Droite')
        if  abs(distance(j1,self)) < self.boss.get_portee():
            if self.boss.get_attaque1_dispo() and not self.atk2 and not self.atk3:
                if not self.atk1:
                    self.frame = 0
                self.atk1 = True
            if self.boss.get_attaque2_dispo() and not self.atk1 and not self.atk3:
                if not self.atk2:
                    self.frame = 0
                self.atk2 = True
        if self.boss.get_attaque3_dispo() and not self.atk1 and not self.atk2 and abs(distance(j1,self)) < 400:
                if not self.atk3:
                    self.frame = 0
                    self.pv_actuels = self.boss.get_pv()
                self.atk3 = True



class JeuCombat:
    def __init__(self,j1,j2):
        self.fond = j2.boss.get_fond()
        self.fonds = {'Temple':0,'Desert':50,'Eglise':15,'Chute':10,'Lave':50,'Pluie':0,'Dojo':20}
        self.run = False
        self.vie_hero = pygame.image.load("images/Jeu de combat/compteur.png")
        self.vie_boss = pygame.image.load("images/Jeu de combat/compteur.png")
        self.police = pygame.font.Font('8-bitanco.ttf', 15)
        self.dmg = False
        self.j1 = j1
        self.j2 = j2
        self.reussi = False
        self.frame = 0
    def actif(self, etat):
        self.run = etat
    def get_actif(self):
        return self.run
    def set_reussi(self):
        self.reussi = True
    def get_reussi(self):
        return self.reussi
    def affichage_degats(self):
        '''Permet d'afficher les dégâts pris par le boss et le héros visuellement (-5,-10,-20,Block)
        '''
        if time.time() - self.j2.cd_dgt10 < 1:
            fenetre.blit(self.j2.dgt10, (self.j1.hero.get_pos_x()+30, self.j1.hero.get_pos_y() - 50))
        if time.time() - self.j2.cd_dgt20 < 1:
            fenetre.blit(self.j2.dgt20, (self.j1.hero.get_pos_x()+30, self.j1.hero.get_pos_y() - 80))
        if time.time() - self.j1.cd_block_img < 1:
            fenetre.blit(self.j1.block, (self.j1.hero.get_pos_x()+30, self.j1.hero.get_pos_y() - 20))
        if time.time() - self.j1.cd_dgt5 < 1:
            fenetre.blit(self.j1.dgt5, (self.j2.boss.get_pos_x()+120, self.j2.boss.get_pos_y() - 80))
    def multis(self, j1, j2):
        # Définition de la matrice des multiplicateurs avec un dictionnaire de dictionnaires
        multis_elements = {
            'Feu': {
                'Feu': 0.01,
                'Glace': 1.75,
                'Eau': 1.45,
                'Nature': 1.25,
                'Esprit': 1.1,
                'Air': 0.9,
                'Nuit': 0.75,
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
                'Foudre' : 1
            }
        }
        
        el1 = j1.hero.get_type()
        el2 = j2.boss.get_type()
        
        # Retourne le multiplicateur du dictionnaire, avec 1 comme valeur par défaut si la combinaison n'existe pas
        return multis_elements.get(el1, {}).get(el2, 1.0)

    def lancer(self):
        # Boucle principale du jeu
        self.largeur, self.hauteur = 1200, 700
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.clock = pygame.time.Clock()
        self.j2.boss.modif_pv(-self.j2.boss.get_pv()+self.j2.boss.get_pv_base())
        self.j1.hero.modif_pv(-self.j1.hero.get_pv()+self.j1.hero.get_pv_base())
        self.j2.boss.modif_pos_x(-self.j2.boss.get_pos_x()+1000)
        self.j1.hero.modif_pos_x(-self.j1.hero.get_pos_x()+50)
        self.j1.hero.modif_img(self.j1.images_marche_d[0])
        self.j1.hero.set_victoire(False)
        self.j2.boss.set_victoire(False)
        self.j2.boss.set_mort(False)
        while not self.j1.hero.get_victoire() and not self.j2.boss.get_victoire() and self.run:
            self.frame += 0.14
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
                self.j1.hero.modif_pv(-0.015)
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
            
            self.affichage_degats()

            self.fenetre.blit(self.j2.boss.image, (self.j2.boss.get_pos_x(), self.j2.boss.get_pos_y()-self.fonds[self.j2.boss.get_nomfond()]))
            self.fenetre.blit(self.j1.hero.image, (self.j1.hero.get_pos_x(), self.j1.hero.get_pos_y()-self.fonds[self.j2.boss.get_nomfond()]))
            self.fenetre.blit(self.vie_hero, (0, -50))
            self.fenetre.blit(self.vie_boss, (950, -50))
            pvheros = self.police.render("Pv du heros : " + str(int(self.j1.hero.get_pv())), True, noir)
            pvboss = self.police.render("Pv du boss : " + str(int(self.j2.boss.get_pv())), True, noir)
            fenetre.blit(pvheros, (60, 70))
            fenetre.blit(pvboss, (1010, 70))
            pygame.display.flip()
            self.clock.tick(60)
        self.actif(False)
        self.largeur, self.hauteur = 400, 400
        pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.mixer.music.unload()

        if self.j2.boss.get_victoire():
            joueur1.set_cagnotte(0)
        elif self.j1.hero.get_victoire():
            self.set_reussi()
            joueur1.modifier_cagnotte(joueur1.get_cagnotte()/4+30000)
        else:
            pygame.quit()




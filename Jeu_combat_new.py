import pygame
import time
import sys
from objets_et_variables import *
from sons import son_epee,aie_boss,aie_hero
from random import randint

class Boss:
    def __init__(self,pv):
        self.image = None
        self.pv = pv
        self.pos_x = 1000
        self.pos_y = 470
        self.cd_img = 0
        self.attaque1_dispo = True
        self.attaque2_dispo = True
        self.cd_attaque1 = 0
        self.cd_attaque2 = 0
        self.victoire = False
        self.cd_ulti = 0
        self.mort = False
        self.pv_base = pv
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
    def get_victoire(self):
        return self.victoire
    def get_cd_ulti(self):
        return self.cd_ulti
    def get_mort(self):
        return self.mort
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
    def set_cd_ulti(self, nb):
        self.cd_ulti = nb
    def set_mort(self,mort):
        self.mort = mort

class Hero:
    def __init__(self,pv,y,speed,spanim1,marche,cd1,cd2):
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
        self.speed_anim1 = spanim1
        self.speed_anim4 = marche
        self.combo = False
        self.cd = (cd1,cd2)
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
    def get_speed_anim(self):
        return (self.speed_anim1,self.speed_anim4)
    def get_block(self):
        return (self.block)
    def get_combo(self):
        return self.combo
    def get_cd(self):
        return self.cd
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

class Night_Hero:
    def __init__(self):
        self.hero = Hero(100,540,4,0.25,0.2,1.2,5)
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

    def attaque(self,speed:float,sens,j2):
        '''Permet de jouer l'animation d'attaque du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if self.frame >= len(self.images_coup_depee_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                if self.hero.get_pos_x()-140 < j2.boss.get_pos_x() < self.hero.get_pos_x() + 100:
                    # Le boss perd 5 Pv
                    aie_boss.play()
                    j2.boss.modif_pv(-5)
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

    def marche(self,speed:float,sens):
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
        

    def cp2(self, speed:float, sens, j2):
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
        self.hero = Hero(150,490,5,0.12,0.06,3,6)
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

    def attaque(self,speed:float,sens,j2):
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
                    if self.hero.get_pos_x()-140 < j2.boss.get_pos_x() < self.hero.get_pos_x() + 100:
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-randint(5,15))
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
                    if self.hero.get_pos_x()-140 < j2.boss.get_pos_x() < self.hero.get_pos_x() + 100:
                        # Le boss perd 5 Pv
                        aie_boss.play()
                        j2.boss.modif_pv(-randint(10,20))
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

    def marche(self,speed:float,sens):
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

    def cp2(self, speed:float, sens, j2):
        '''Permet de jouer l'animation de parade du héros.
        Paramètres :
            - self
            - speed (float) : la vitesse à laquelle va se jouer l'animation
        '''
        if self.hero.get_pv() > 0:
            if self.frame >= len(self.cp2_d)-1:
                son_epee.play()
                # Si le boss est à portée du héros
                if self.hero.get_pos_x()-140 < j2.boss.get_pos_x() < self.hero.get_pos_x() + 100:
                    # Le boss perd 5 Pv
                    aie_boss.play()
                    j2.boss.modif_pv(-randint(15,40))
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

class Hell_Boss:
    def __init__(self):
        self.boss = Boss(120)
        self.images_coup_poing = [f'images/Jeu de combat/Boss/Attaque1/Coup_de_poing{i}.png' for i in range(1,5)]
        self.images_coup_faux = [f'images/Jeu de combat/Boss/Attaque2/Faux{i}.png' for i in range(1,8)]
        self.images_marche_d = [f'images/Jeu de combat/Boss/Marche/Droite/Marche{i}.png' for i in range(1,8)]
        self.images_marche_g = [f'images/Jeu de combat/Boss/Marche/Gauche/Marche{i}.png' for i in range(1,8)]
        self.images_ulti = [f'images/Jeu de combat/Boss/Ulti/Ulti ({i}).png' for i in range(1,7)]
        self.images_mort = [f'images/Jeu de combat/Boss/Mort/Mort{i}.png' for i in range(1,8)]
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
        if self.frame > len(self.images_coup_poing):
            self.frame = 0
        # Si toutes les images ont été jouées :
        elif int(self.frame) >= len(self.images_coup_poing)-1:
            # On remet tout à 0
            self.boss_sprite_attaque1 = 0
            self.boss.set_cd_attaque1()
            self.boss.set_attaque1_dispo(False)
            self.atk1 = False
            # Si le héros se trouve à portée du boss :
            if self.boss.get_pos_x()+120 > j1.hero.get_pos_x() > self.boss.get_pos_x() - 120 and not j1.hero.get_block():
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
        if self.frame > len(self.images_coup_faux):
            self.frame = 0
        # Si l'animation arrive au coup de l'attaque et que l'attaque n'a pas encore effectué ses dégâts :
        if self.frame >= len(self.images_coup_faux)-1:
            # Si le héros se trouve à portée du boss :
            if self.boss.get_pos_x()+120 > j1.hero.get_pos_x() > self.boss.get_pos_x() - 120 and j1.hero.get_pos_y() > 250 and not j1.hero.get_block():
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
            self.boss.modif_pv(20)
            j1.hero.modif_pv(-20)
            # Image des dégâts subis
            self.cd_dgt20 = time.time()
            self.boss_sprite_ulti = 0
            self.boss.set_cd_ulti(0)
            self.ulti_anim = False
            print(f"Attaque Ultime ! : Pv héros : {j1.hero.get_pv()}")
            print(f"Attaque Ultime ! : Pv boss : {self.boss.get_pv()}")
        self.frame += speed
        self.boss.modif_img(self.images_ulti[int(self.frame)])
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
            else:
                # Faire progresser les images pour l'animation
                self.frame_mort += speed
                self.boss.modif_img(self.images_mort[int(self.frame_mort)])
    def boss_vers_hero(self,xhero:float):
        if xhero - 80 < self.boss.get_pos_x():
            self.marche(0.1,'Gauche')
            self.boss.modif_pos_x(-1.5)
        elif xhero + 100 > self.boss.get_pos_x():
            self.marche(0.1,'Droite')
            self.boss.modif_pos_x(1.5)
    def patern_boss(self,xhero,j1):
        if self.boss.get_pv() <= 25:
            # Gestion de la guérison du boss à faible PV
            if self.boss.get_cd_ulti() == 0:
                self.boss.set_cd_ulti(time.time())
            elif time.time() - self.boss.get_cd_ulti() > 6:
                self.ulti_anim = True
                if self.boss.get_pos_x() < 900:
                    self.marche(0.1,'Droite')
                    self.boss.modif_pos_x(1.2)
                else:
                    self.ulti(0.08,j1)
        # Si le boss se trouve à portée, lancement des attaques
        if not self.ulti_anim:
            if xhero - 80 < self.boss.get_pos_x() < xhero + 100:
                if self.boss.get_attaque1_dispo() and not self.atk2:
                    self.coup_de_poing(0.1,j1)
                elif self.boss.get_attaque2_dispo() and not self.atk1:
                    self.faux(0.12,j1)
                else:
                    # Si aucune attaque n'est disponible, lance une animation d'inaction
                    self.inaction(0.1)
            else:
                # Sinon, déplacement pour être à portée du héros
                self.boss_vers_hero(xhero)

class JeuCombat:
    def __init__(self,j1,j2):
        self.fond = pygame.image.load("images/Jeu de combat/Arène.png") 
        self.run = False
        self.vie_hero = pygame.image.load("images/Jeu de combat/compteur.png")
        self.vie_boss = pygame.image.load("images/Jeu de combat/compteur.png")
        self.police = pygame.font.Font('8-bitanco.ttf', 15)
        self.dmg = False
        self.j1 = j1
        self.j2 = j2
        self.reussi = False
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
    def lancer(self):
        # Boucle principale du jeu
        self.largeur, self.hauteur = 1200, 700
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.clock = pygame.time.Clock()
        self.j2.boss.modif_pv(-self.j2.boss.get_pv()+self.j2.boss.get_pv_base())
        self.j1.hero.modif_pv(-self.j1.hero.get_pv()+self.j1.hero.get_pv_base())
        self.j2.boss.modif_pos_x(-self.j2.boss.get_pos_x()+1000)
        self.j1.hero.modif_img(self.j1.images_marche_d[0])
        self.j1.hero.set_victoire(False)
        self.j2.boss.set_victoire(False)
        print(self.j1.hero.get_pv())
        while not self.j1.hero.get_victoire() and not self.j2.boss.get_victoire() and self.run:
            self.fenetre.blit(self.fond, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        if self.j1.hero.get_attaque() and self.j1.hero.get_cd_atk() > 0.5:
                            self.j1.hero.set_combo(True)
                        if self.j1.hero.get_cd_atk() > self.j1.hero.get_cd()[0]:
                            self.j1.reset_frame()
                            self.j1.hero.set_cd_atk()
                            self.j1.hero.set_attaque(True)
                    elif event.key == pygame.K_KP0 and self.j1.hero.get_cd_cp2() > self.j1.hero.get_cd()[1]:
                        self.j1.reset_frame()
                        self.j1.hero.set_cd_cp2()
                        self.j1.hero.set_cp2(True)
                        

            if not self.j2.boss.get_pv() <= 0:
                if self.j1.hero.get_pv() > 0:
                    self.j2.patern_boss(self.j1.hero.get_pos_x(),self.j1)
                else:
                    self.j2.inaction(0)
            else:
                self.j2.mort(0.1,self.j1)

            if self.j1.hero.get_pv() <= 0:
                self.j1.mort(0.1,self.j2)

            if self.j1.hero.get_attaque():
                if self.j2.boss.get_pos_x() > self.j1.hero.get_pos_x():
                    self.j1.attaque(self.j1.hero.get_speed_anim()[0],'Droite',self.j2)
                else:
                    self.j1.attaque(self.j1.hero.get_speed_anim()[0],'Gauche',self.j2)
            keys = pygame.key.get_pressed()
            if not self.j1.hero.get_attaque() and not self.j1.hero.get_pv() <= 0:
                if keys[pygame.K_LEFT]:
                    if self.j1.hero.get_pos_x() > 0:
                        self.j1.hero.modif_pos_x(-self.j1.hero.get_speed())
                    self.j1.marche(self.j1.hero.get_speed_anim()[1],'Gauche')
                if keys[pygame.K_RIGHT]:
                    if self.j1.hero.get_pos_x() < 1000:
                        self.j1.hero.modif_pos_x(self.j1.hero.get_speed())
                    self.j1.marche(self.j1.hero.get_speed_anim()[1],'Droite')

            if self.j2.boss.get_cd_attaque1() > 2.5:
                self.j2.boss.set_attaque1_dispo(True)
            if self.j2.boss.get_cd_attaque2() > 4.5:
                self.j2.boss.set_attaque2_dispo(True)

            if self.j1.hero.get_cp2():
                if self.j2.boss.get_pos_x() > self.j1.hero.get_pos_x():
                    self.j1.cp2(self.j1.hero.get_speed_anim()[0],'Droite',self.j2)
                else:
                    self.j1.cp2(self.j1.hero.get_speed_anim()[0],'Gauche',self.j2)
                
            
            self.affichage_degats()

            self.fenetre.blit(self.j2.boss.image, (self.j2.boss.get_pos_x(), self.j2.boss.get_pos_y()))
            self.fenetre.blit(self.j1.hero.image, (self.j1.hero.get_pos_x(), self.j1.hero.get_pos_y()))
            self.fenetre.blit(self.vie_hero, (0, -50))
            self.fenetre.blit(self.vie_boss, (950, -50))
            pvheros = self.police.render("Pv du heros : " + str(self.j1.hero.get_pv()), True, noir)
            pvboss = self.police.render("Pv du boss : " + str(self.j2.boss.get_pv()), True, noir)
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
            joueur1.set_cagnotte(10000000)
        else:
            pygame.quit()




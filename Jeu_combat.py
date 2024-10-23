import pygame
import sys
import time

pygame.init()
pygame.display.set_caption("Jeu Combat")
largeur, hauteur = 1200, 700
fenetre = pygame.display.set_mode((largeur, hauteur))

clock = pygame.time.Clock()

fond_combat = pygame.image.load('images/enfer.jpg').convert()
mort_boss = [f'Boss/Mort/Mort{i}.png' for i in range(1,8)]
marche_boss_gauche = [f'Boss/Marche/Gauche/Marche{i}.png' for i in range(1,8)]
marche_boss_droite = [f'Boss/Marche/Droite/Marched{i}.png' for i in range(1,8)]
attaque1_boss = [f'Boss/Attaque1/Coup_de_poing{i}.png' for i in range(1,4)]
attaque2_boss = [f'Boss/Attaque2/Faux{i}.png' for i in range(1,7)]
inaction_boss = [f'Boss/Inaction/Inaction{i}.png' for i in range(1,4)]

marche_hero_droite = [f'Hero/Marche/Droite/Hero_course{i}.png' for i in range(1,7)]
marche_hero_gauche = [f'Hero/Marche/Gauche/Hero_course{i}.png' for i in range(1,7)]
attaque_hero_img = [f'Hero/Attaque/Attaque{i}.png' for i in range(1,13)]
degats_hero_img = [f'Hero/Degats/degats{i}.png' for i in range(1,4)]
mort_hero_img = [f'Hero/Mort/_afrm{i},70.png' for i in range(1,24)]

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
    def set_victoire(self):
        self.victoire = True

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
    

boss = Boss(mort_boss[0])
hero = Hero(marche_hero_droite[0])
boss_sprite_marche = 0
boss_sprite_attaque1 = 0
boss_sprite_attaque2 = 0
boss_sprite_inaction = 0
boss_sprite_mort = 0
hero_sprite_marche = 0
hero_sprite_attaque = 0
hero_sprite_degats = 0
hero_sprite_mort = 0

def animation_marche_boss_gauche():
    global boss_sprite_marche
    boss_sprite_marche += 1
    boss.modif_img(marche_boss_gauche[boss_sprite_marche])
    if boss_sprite_marche == len(marche_boss_gauche)-1:
        boss_sprite_marche = 0

def animation_marche_boss_droite(boss):
    global boss_sprite_marche
    boss_sprite_marche += 1
    boss.modif_img(marche_boss_droite[boss_sprite_marche])
    if boss_sprite_marche == len(marche_boss_droite)-1:
        boss_sprite_marche = 0

def animation_attaque1_boss(boss):
    global boss_sprite_attaque1
    boss_sprite_attaque1 += 1
    boss.modif_img(attaque1_boss[boss_sprite_attaque1])
    if boss_sprite_attaque1 == len(attaque1_boss)-1:
        if boss.get_pos_x()+120 > hero.get_pos_x() > hero.get_pos_x() - 120:
            hero.modif_pv(-5)
            hero.set_degats_subis(True)
            print(f'Attaque coup de poing : Pv hero {hero.get_pv()}')
        boss_sprite_attaque1 = 0
        boss.set_cd_attaque1()
        boss.set_attaque1_dispo(False)

def animation_attaque2_boss(boss):
    global boss_sprite_attaque2
    boss_sprite_attaque2 += 1
    boss.modif_img(attaque2_boss[boss_sprite_attaque2])
    if boss_sprite_attaque2 == 1:
        boss.set_cd_attaque2()
        boss.set_attaque2_dispo(False)
    if boss_sprite_attaque2 == len(attaque2_boss)-1:
        if boss.get_pos_x()+120 > hero.get_pos_x() > hero.get_pos_x() - 90:
            hero.modif_pv(-15)
            hero.set_degats_subis(True)
            print(f'Attaque faux : Pv hero : {hero.get_pv()}')
        boss_sprite_attaque2 = 0

def animation_inaction_boss(boss):
    global boss_sprite_inaction
    boss_sprite_inaction += 1
    boss.modif_img(inaction_boss[boss_sprite_inaction])
    if boss_sprite_inaction == len(inaction_boss)-1:
        boss_sprite_inaction = 0

def animation_marche_hero_droite(hero):
    global hero_sprite_marche
    hero_sprite_marche += 1
    hero.modif_img(marche_hero_droite[hero_sprite_marche])
    if hero_sprite_marche == len(marche_hero_droite)-1:
        hero_sprite_marche = 0

def animation_marche_hero_gauche(hero):
    global hero_sprite_marche
    hero_sprite_marche += 1
    hero.modif_img(marche_hero_gauche[hero_sprite_marche])
    if hero_sprite_marche == len(marche_hero_gauche)-1:
        hero_sprite_marche = 0

def attaque_hero(hero):
    global hero_sprite_attaque
    if hero_sprite_attaque == 10:
        if hero.get_pos_x()-120 < boss.get_pos_x() < hero.get_pos_x() + 120:
            boss.modif_pv(-20)
            print(boss.get_pv())
    elif hero_sprite_attaque == len(attaque_hero_img)-1:
        hero_sprite_attaque = 0
        hero.set_attaque(False)
    hero_sprite_attaque += 1
    hero.modif_img(attaque_hero_img[hero_sprite_attaque])

def degats_hero(hero):
    global hero_sprite_degats
    hero_sprite_degats += 1
    hero.modif_img(degats_hero_img[hero_sprite_degats])
    if hero_sprite_degats == len(degats_hero_img)-1:
        hero_sprite_degats = 0
        hero.set_degats_subis(False)

def anim_mort_boss(boss):
    global boss_sprite_mort
    if not hero.get_victoire():
        boss_sprite_mort += 1
        boss.modif_img(mort_boss[boss_sprite_mort])
        if boss_sprite_mort == len(mort_boss)-1:
            print("victoire")
            hero.set_victoire()

def anim_mort_hero(hero):
    global hero_sprite_mort
    if not boss.get_victoire():
        hero_sprite_mort += 1
        hero.modif_img(mort_hero_img[hero_sprite_mort])
        if hero_sprite_mort == len(mort_hero_img)-1:
            print("Défaite")
            boss.set_victoire()

def patern_boss(boss,hero):
    if boss.get_pv() > 90:
        if hero.get_pos_x() - 80 < boss.get_pos_x() < hero.get_pos_x() + 100:
            if boss.get_attaque1_dispo():
                animation_attaque1_boss(boss)
            elif boss.get_attaque2_dispo():
                animation_attaque2_boss(boss)
            else:
                animation_inaction_boss(boss)
        elif hero.get_pos_x() - 80 < boss.get_pos_x():
            animation_marche_boss_gauche()
            boss.modif_pos_x(-12)
        elif hero.get_pos_x() + 100 > boss.get_pos_x():
            animation_marche_boss_droite(boss)
            boss.modif_pos_x(12)
    else:       
        if boss.get_attaque1_dispo():
            if hero.get_pos_x() - 50 < boss.get_pos_x() < hero.get_pos_x() + 100:
                animation_attaque1_boss(boss)
            elif hero.get_pos_x() - 50 < boss.get_pos_x():
                animation_marche_boss_gauche()
                boss.modif_pos_x(-12)
            elif hero.get_pos_x() + 100 > boss.get_pos_x():
                animation_marche_boss_droite(boss)
                boss.modif_pos_x(12)
        elif boss.get_attaque2_dispo():
            if hero.get_pos_x() - 50 < boss.get_pos_x() < hero.get_pos_x() + 100:
                animation_attaque2_boss(boss)
            elif hero.get_pos_x() - 50 < boss.get_pos_x():
                animation_marche_boss_gauche()
                boss.modif_pos_x(-12)
            elif hero.get_pos_x() + 100 > boss.get_pos_x():
                animation_marche_boss_droite(boss)
                boss.modif_pos_x(12)
        else:
            if boss.get_pos_x() < 50 or boss.get_pos_x() > 1000:
                animation_inaction_boss(boss)
            elif hero.get_pos_x() - 50 < boss.get_pos_x():
                animation_marche_boss_droite(boss)
                boss.modif_pos_x(12)
            elif hero.get_pos_x() + 100 > boss.get_pos_x():
                animation_marche_boss_gauche()
                boss.modif_pos_x(-12)
        
            

while not hero.get_victoire() or not boss.get_victoire():
    fenetre.fill((0,0,0))
    #fenetre.blit(fond_combat, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                hero.set_attaque(True)
    if not boss.get_pv() <= 0 and hero.get_pv() >= 0:
        patern_boss(boss,hero)
    else:
        anim_mort_boss(boss)
    
    if hero.get_pv() <= 0:
        anim_mort_hero(hero)

    if hero.get_attaque():
        attaque_hero(hero)

    keys = pygame.key.get_pressed()
    if not hero.get_attaque() and not hero.get_pv() <= 0:
        if keys[pygame.K_LEFT]:
            if hero.get_pos_x() > 0:
                hero.modif_pos_x(-25)
            animation_marche_hero_gauche(hero)
        if keys[pygame.K_RIGHT]:
            if hero.get_pos_x() < 1000:
                hero.modif_pos_x(25)
            animation_marche_hero_droite(hero)

    if boss.get_cd_attaque1() > 1.5:
        boss.set_attaque1_dispo(True)
    if boss.get_cd_attaque2() > 4:
        boss.set_attaque2_dispo(True)
    if hero.get_degats_subis():
        degats_hero(hero)
    '''boss_sprite_marche += 1
    boss.modif_img(mort_boss[boss_sprite_marche])
    if boss_sprite_marche == len(mort_boss)-1:
        boss_sprite_marche = 0'''
    fenetre.blit(boss.image, (boss.get_pos_x(), boss.get_pos_y()))
    fenetre.blit(hero.image, (hero.get_pos_x(), hero.get_pos_y()))
    pygame.display.flip()
    clock.tick(10)
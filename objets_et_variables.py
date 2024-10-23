from classes import *
from sons import *


joueur1 = Joueur()
ecran1 = Ecran(True)
ecran2 = Ecran()
ecran3 = Ecran()
ecran4 = Ecran()
ecran_fin = Ecran()
bouton1 = Bouton(100, 50, 150, 300)
bouton2 = Bouton(160, 25, 0, 0)
bouton3 = Bouton(160, 25, 0, 25)
bouton4 = Bouton(120, 100, 140, 150)
clock = pygame.time.Clock()

champ_joueur = pygame.Rect(130, 250, 140, 32)
code_cb = pygame.Rect(130, 325, 140, 32)
nb_cb = pygame.Rect(100, 275, 200, 32)
nb_cb_actif = False
nom_actif = False
code_cb_actif = False
win = False

text = ''
nbr_cb = ''
codee_cb = ''

tir_sprites = pygame.sprite.Group()
pistolet = Pistolet(120, 120, tire_balle)
tir_sprites.add(pistolet)

tir_blanc_sprites = pygame.sprite.Group()
pistolet_blanc = Pistolet_blanc(120, 120)
tir_blanc_sprites.add(pistolet_blanc)

mvmt_sprites = pygame.sprite.Group()
coin = Coin(100, -7)
mvmt_sprites.add(coin)

pileouface_sprites=pygame.sprite.Group()
pileouface = Pile_ou_face(170,170)
pileouface_sprites.add(pileouface)

pofactif = True
choix_fait = False 

image_test = pygame.image.load('machine_a_sou/orange.png')
fruits_dict = {
    "cerise": pygame.image.load('machine_a_sou/cerise.png'),
    "pomme": pygame.image.load('machine_a_sou/pomme.png'),
    "orange": pygame.image.load('machine_a_sou/orange.png'),
    "pasteque": pygame.image.load('machine_a_sou/pasteque.png'),
    "pomme_dore": pygame.image.load('machine_a_sou/pomme_doree.png')
}
fruits = ["pomme", "cerise", "orange", "pasteque", "pomme_dore"]
proba_fruits = [0.2, 0.25, 0.4, 0.12, 0.03]

fruits_dict_gains = {
    "orange": 500,
    "cerise": 1000,
    "pomme": 2300,
    "pasteque": 4000,
    "pomme_dore": 1000000
}
hauteur_emplacement = 150
emplacement_x_milieu = 400/3 + 43
emplacement_x_gauche = emplacement_x_milieu - image_test.get_width() -10
emplacement_x_droite = emplacement_x_milieu + image_test.get_width() +8
emplacements = pygame.sprite.Group()
emplacement_gauche = Emplacement(emplacement_x_gauche, hauteur_emplacement)
emplacement_milieu = Emplacement(emplacement_x_milieu, hauteur_emplacement)
emplacement_droite = Emplacement(emplacement_x_droite, hauteur_emplacement)
# rangement des emplacements dans le groupe
emplacements.add(emplacement_gauche)
emplacements.add(emplacement_milieu)
emplacements.add(emplacement_droite)
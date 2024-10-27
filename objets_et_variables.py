from classes import *
from sons import *
from img import *
from Roulette_Russe import *

blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (128, 128, 128)
joueur1 = Joueur()
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

pistolet = RouletteRusse(110, 120, tire_balle)


mvmt_sprites = pygame.sprite.Group()
coin = Coin(100, -7)
mvmt_sprites.add(coin)

pileouface_sprites=pygame.sprite.Group()
pileouface = Pile_ou_face(170,170)
pileouface_sprites.add(pileouface)

pofactif = True
choix_fait = False 



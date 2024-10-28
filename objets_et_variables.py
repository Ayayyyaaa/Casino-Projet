from classes import *
from img import *

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

mvmt_sprites = pygame.sprite.Group()
coin = Coin(100, -7)
mvmt_sprites.add(coin)



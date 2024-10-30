from classes import *
from img import *

blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (128, 128, 128)
joueur1 = Joueur()
bouton1 = Bouton(100, 50, 150, 300)
bouton2 = Bouton(160, 25, 0, 0)
bouton3 = Bouton(160, 25, 0, 25)
clock = pygame.time.Clock()

mvmt_sprites = pygame.sprite.Group()
coin = Coin(100, -7)
mvmt_sprites.add(coin)



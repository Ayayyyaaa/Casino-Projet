import pygame
from objets_et_variables import *

print("Chargement de fonctions.py")

fond2 = pygame.image.load('images/Fonds d\'ecran/casino.jpg').convert()

def dessiner_bouton(fenetre, message:str, x: int, y:int, largeur:int, hauteur:int, couleur_fond:tuple, couleur_texte:tuple, taille:int):
    '''
    Permet de dessiner un bouton.
    Paramètres:
        - fenetre : la fenetre pygame concernée
        - message (str) : Le texte à écrire
        - x (float or int) : la position x du bouton
        - y (float or int) : la position y du bouton
        - largeur (float or int) : la largeur du bouton
        - hauteur (float or int) : la hauteur du bouton
        - couleur_fond (tuple) : la couleur de fond du bouton
        - couleur_texte (tuple) : la couleur du texte du bouton
        - taille (int) : la taille de la police d'écriture
    '''
    pygame.draw.rect(fenetre, couleur_fond, (x, y, largeur, hauteur))
    police = pygame.font.Font('police.ttf', taille)
    texte = police.render(message, True, couleur_texte)
    fenetre.blit(texte, (x + 10, y + (hauteur - texte.get_height()) // 2))


def dessiner_zone_texte(fenetre, rect, texte:str, actif:bool):
    '''
    Permet de dessiner une zone de texte.
    Paramètres:
        - fenetre : la fenetre pygame concernée
        - rect : Le rectangle à dessiner, contenant la position x et y, ainsi que la largeur et la hauteur
        - texte (str) : Le texte à écrire
        - actif (bool) : Le booléen indiquant si le champ est actif (ssi on peut écrire)
    '''
    pygame.draw.rect(fenetre, blanc, rect)
    couleur = gris
    if actif:
        couleur = noir
    pygame.draw.rect(fenetre, couleur, rect, 2)
    police = pygame.font.Font('police.ttf', 25)
    texte_surface = police.render(texte, True, noir)
    fenetre.blit(texte_surface, (rect.x + 5, rect.y + 5))

def achat(article:str) -> None:
    '''Permet d'acheter un article en fonction de son prix.
    Paramètres:
        - article (str) : Le nom de l'article à acheter'''
    if joueur1.get_cagnotte() >= boutique[article]:
        joueur1.modifier_cagnotte(-boutique[article])
        joueur1.ajouter_inventaire(article)
        print("Achat effectué !")
    else:
        print("Solde insuffisant !")

def afficher_ecran_chargement(img) -> None:
    '''Permet d'afficher l'écran de chargement
    Paramètres:
        - img : L'image à afficher'''
    fenetre.blit(img, (0, 0))  # Afficher le fond
    pygame.display.flip()

def valider_numero_carte_bancaire(numero:str) -> bool:
    "Fonction qui permet de valider un numéro de carte bancaire avec la methode de Luhn (oui on est motivés)"
    assert type(numero) == str, "Le numéro de carte bancaire doit être une chaîne de caractères"
    numero = ''.join(filter(str.isdigit, numero))
    if len(numero) != 16:
        return False
    somme = 0
    inverse = numero[::-1]
    for i, chiffre in enumerate(inverse):
        n = int(chiffre)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9  
        somme += n
    return somme % 10 == 0






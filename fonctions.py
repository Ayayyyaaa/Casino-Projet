import pygame
from random import randint
from objets_et_variables import *
from img import *
import numpy

blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (128, 128, 128)

fond2 = pygame.image.load('images/casino.jpg').convert()

def dessiner_bouton(fenetre, message:str, x: int or float, y:int or float, largeur:int or float, hauteur:int or float, couleur_fond:tuple, couleur_texte:tuple, taille:int or float):
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

def rouletterusse():
    '''
    Permet de déterminer quelle balle sort du pistolet, puis active l'animation du pistolet (mort) ou celle du pistolet_blanc (victoire)
    '''
    if joueur1.get_roulette_active():
        proba = 1
        if joueur1.get_cagnotte() > 800000:
            proba = 5
        elif joueur1.get_cagnotte() > 500000:
            proba = 4
        elif joueur1.get_cagnotte() > 100000:
            proba = 3
        elif joueur1.get_cagnotte() > 50000:
            proba = 2
        else:
            proba = 1
        balle = randint(1, 6)
        if balle <= proba: 
            pistolet.activer_rotation()
        else:  
            pistolet_blanc.activer_rotation()

def affiche_ecran1():
    '''
    Permet d'afficher l'écran d'accueil.
    '''
    fenetre.blit(fond, (0, 0))
    if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
        fenetre.blit(entrer2, (105, 230))
    else:
        fenetre.blit(entrer, (105, 230))

def affiche_ecran2():
    '''
    Permet d'afficher l'écran principal et de gérer l'animation des boutons et mettre à jour les animations des jeux.
    '''
    fenetre.blit(pseudos(), (0, 0))
    coin.activer_rotation()
    if ecran2.get_actif() and 330 <= pygame.mouse.get_pos()[0] <= 390 and 45 <= pygame.mouse.get_pos()[1] <= 75 :
        fenetre.blit(roulette2, (320, 20))
    else:
        fenetre.blit(roulette, (320, 20))
    if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
        fenetre.blit(retour2, (105, 230))
    else:
        fenetre.blit(retour, (105, 230))
    dessiner_bouton(fenetre, joueur1.get_pseudo(), bouton2.get_x(), bouton2.get_y(), bouton2.get_largeur(), bouton2.get_hauteur(), blanc, noir, 20)
    dessiner_bouton(fenetre, f"Solde : {joueur1.get_cagnotte()}", bouton3.get_x(), bouton3.get_y(), bouton3.get_largeur(), bouton3.get_hauteur(), blanc, noir, 25)
    if 330 <= pygame.mouse.get_pos()[0] <= 390 and 170 <= pygame.mouse.get_pos()[1] <= 220 :
        fenetre.blit(machine_a_sous2, (320, 160))
    else:
        fenetre.blit(machine_a_sous1, (320, 160))
    if pofactif:
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 100 <= pygame.mouse.get_pos()[1] <= 150 :
            fenetre.blit(imgpof2, (320, 90))
        else:
            fenetre.blit(imgpof, (320, 90))
    elif not pofactif:
        dessiner_bouton(fenetre, "pile", 150, 200, 50, 50, blanc, noir, 25)
        dessiner_bouton(fenetre, "face", 250, 200, 50, 50, blanc, noir, 25)
            

    mvmt_sprites.draw(fenetre)
    mvmt_sprites.update(0.15)

    tir_sprites.draw(fenetre)
    tir_sprites.update(0.5,joueur1)  

    tir_blanc_sprites.draw(fenetre)
    tir_blanc_sprites.update(0.5, joueur1)

    pileouface_sprites.draw(fenetre)
    pileouface_sprites.update(0.65, joueur1, piece)

    if joueur1.get_pseudo() == '666' or joueur1.get_pseudo() == 'Satan':
        fenetre.blit(diable, (100, 2))
    
    clock.tick(20)
    

def affiche_ecran3():
    '''
    Permet d'afficher l'écran de mort.
    '''
    fenetre.blit(fond3, (0, 0))

def pseudos():
    '''
    Permet de gérer les différentes interactions des pseudos.
    '''
    if joueur1.get_pseudo() == 'Mr.Maurice' or joueur1.get_pseudo() == 'Mr Maurice' or joueur1.get_pseudo() == 'Maurice':
        joueur1.set_pseudo('Le meilleur')  #Mettez nous des tickets et un 20/20 svp

    if joueur1.get_pseudo() == 'Fredou':
        fond2 = pygame.image.load('images/coeurfredou.png').convert()
    else:
        fond2 = pygame.image.load('images/casino.jpg').convert()
    return(fond2)

def lancement():
    '''
    Permet de lancer la machine à sous.
    '''
    global jetons
    hasard = numpy.random.choice(fruits, 3, p=proba_fruits)
    
    # Récupérer les images directement depuis le dictionnaire
    emplacement_gauche.set_image(fruits_dict[hasard[0]])
    emplacement_milieu.set_image(fruits_dict[hasard[1]])
    emplacement_droite.set_image(fruits_dict[hasard[2]])

    if hasard[0] == hasard[1] == hasard[2]:
        fruit = hasard[0]
        jetons_gagnes = fruits_dict_gains[fruit]
        joueur1.modifier_cagnotte(jetons_gagnes)

def affiche_ecran4():
    '''
    Permet d'afficher l'écran du mini-jeu Machine à sous.
    '''
    fond4 = pygame.image.load('machine_a_sou/slot.png')
    fenetre.fill(blanc)
    fenetre.blit(fond4, (0, 0))
    emplacements.draw(fenetre)
    comic = pygame.font.SysFont("comicsansms", 30)
    text = comic.render(str(joueur1.get_cagnotte()) + " pièces", True, blanc)
    fenetre.blit(text, (10, 0))
    dessiner_bouton(fenetre, "Retour", 340, 20, 50, 50, blanc, noir, 15)

def affiche_ecran_fin():
    '''
    Permet d'afficher l'écran de victoire.
    '''
    fenetre.blit(paradis, (0, 0))
    if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
        fenetre.blit(retour2, (105, 230))
    else:
        fenetre.blit(retour, (105, 230))


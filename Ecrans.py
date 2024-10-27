import pygame
from fonctions import dessiner_zone_texte, dessiner_bouton
from objets_et_variables import *
from classes import Ecran
from img import *


class Ecran1:
    def __init__(self):
        self.ecran = Ecran(True)
    def affiche(self,text,nom_actif):
        if self.ecran.get_actif():
            fenetre.blit(fond, (0, 0))
            dessiner_zone_texte(fenetre, champ_joueur, text, nom_actif)
            if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
                fenetre.blit(entrer2, (105, 230))
            else:
                fenetre.blit(entrer, (105, 230))


class Ecran2:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/coeurfredou.png').convert()
    def affiche(self):
        '''
        Permet d'afficher l'écran principal et de gérer l'animation des boutons et mettre à jour les animations des jeux.
        '''
        if joueur1.get_pseudo() == 'Mr.Maurice' or joueur1.get_pseudo() == 'Mr Maurice' or joueur1.get_pseudo() == 'Maurice':
            joueur1.set_pseudo('Le meilleur')  #Mettez nous des tickets et un 20/20 svp

        if joueur1.get_pseudo() == 'Fredou':
            self.fond = pygame.image.load('images/coeurfredou.png').convert()
        else:
            self.fond = pygame.image.load('images/casino.jpg').convert()
        fenetre.blit(self.fond, (0, 0))
        coin.activer_rotation()
        if ecran2.ecran.get_actif() and 330 <= pygame.mouse.get_pos()[0] <= 390 and 45 <= pygame.mouse.get_pos()[1] <= 75 :
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

        fenetre.blit(pistolet.get_image(),(120,120))
        pistolet.update_def(0.5,joueur1)  
        pistolet.update_vict(0.5,joueur1)  

        pileouface_sprites.draw(fenetre)
        pileouface_sprites.update(0.65, joueur1, piece)

        if joueur1.get_pseudo() == '666' or joueur1.get_pseudo() == 'Satan':
            fenetre.blit(diable, (100, 2))
        
        clock.tick(20)

class EcranMort:
    def __init__(self):
        self.ecran = Ecran()
        self.fond =  pygame.image.load('images/enfer2.png').convert()
    def affiche(self):
        '''
        Permet d'afficher l'écran de mort.
        '''
        fenetre.blit(self.fond, (0, 0))

class EcranVictoire:
    def __init__(self):
        self.ecran = Ecran()
        self.retour1 = pygame.image.load('images/Retour-1.png').convert_alpha()
        self.retour2 = pygame.image.load('images/Retour-2.png').convert_alpha()
    def affiche(self):
        '''
        Permet d'afficher l'écran de victoire.
        '''
        fenetre.blit(paradis, (0, 0))
        if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
            fenetre.blit(self.retour2, (105, 230))
        else:
            fenetre.blit(self.retour1, (105, 230))

ecran1 = Ecran1()
ecran2 = Ecran2()
ecran_mort = EcranMort()
ecran_victoire = EcranVictoire()
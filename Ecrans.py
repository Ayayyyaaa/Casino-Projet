import pygame
from fonctions import dessiner_zone_texte, dessiner_bouton
from objets_et_variables import *
from img import *
from Roulette_Russe import pistolet
from PileouFace import pileouface
import sys

class Ecran:
    def __init__(self, actif=False):
        self.actif = actif

    def get_actif(self):
        return self.actif

    def set_actif(self, actif):
        self.actif = actif

class Ecran1:
    def __init__(self):
        self.ecran = Ecran(True)
    def affiche(self):
        if self.ecran.get_actif():
            fenetre.blit(fond, (0, 0))
            if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
                fenetre.blit(entrer2, (105, 230))
            else:
                fenetre.blit(entrer, (105, 230))


class Ecran2:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = None
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
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 100 <= pygame.mouse.get_pos()[1] <= 150 :
            fenetre.blit(imgpof2, (320, 90))
        else:
            fenetre.blit(imgpof, (320, 90))
        # Affichage des boutons des choix du pile ou face
        if pileouface.get_actif():
            fenetre.blit(face2, (125, 230))
            fenetre.blit(pile2, (230, 230))
                

        mvmt_sprites.draw(fenetre)
        mvmt_sprites.update(0.02)

        fenetre.blit(pistolet.get_image(),pistolet.get_pos())
        pistolet.update_def(0.08,joueur1)  
        pistolet.update_vict(0.08,joueur1)  

        fenetre.blit(pileouface.get_image(),(170,140))
        pileouface.update(0.10, joueur1)

        if joueur1.get_pseudo() == '666' or joueur1.get_pseudo() == 'Satan':
            fenetre.blit(diable, (100, 2))
    

class EcranMort:
    def __init__(self):
        self.ecran = Ecran()
        self.fond =  pygame.image.load('images/enfer2.png').convert()
        self.txt_nbr_cb = ""  
        self.txt_codee_cb = ""  
        self.nb_cb_actif = False  
        self.code_cb_actif = False  
        self.code_cb = pygame.Rect(130, 325, 140, 32)
        self.nb_cb = pygame.Rect(100, 275, 200, 32)
    def affiche(self):
        '''
        Permet d'afficher l'écran de mort.
        '''
        fenetre.blit(self.fond, (0, 0))
        dessiner_zone_texte(fenetre, self.nb_cb, self.txt_nbr_cb, self.nb_cb_actif)
        dessiner_zone_texte(fenetre, self.code_cb, self.txt_codee_cb, self.code_cb_actif)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Champ pour le numéro de carte bleue
                if self.nb_cb.collidepoint(event.pos):
                    self.nb_cb_actif = not self.nb_cb_actif
                else:
                    self.nb_cb_actif = False
                # Champ pour le code de carte bleue
                if self.code_cb.collidepoint(event.pos):
                    self.code_cb_actif = not self.code_cb_actif
                else:
                    self.code_cb_actif = False
            elif event.type == pygame.KEYDOWN:
                # Gérer la saisie du numéro de carte bleue
                if self.nb_cb_actif:
                    if event.key == pygame.K_BACKSPACE:
                        self.txt_nbr_cb = self.txt_nbr_cb[:-1]
                    elif len(self.txt_nbr_cb) < 19 and event.unicode in "0123456789":
                        L = [4,9,14]
                        for elem in L:
                            if len(self.txt_nbr_cb) == elem:
                                self.txt_nbr_cb += ' '
                        self.txt_nbr_cb += event.unicode

                elif self.code_cb_actif:
                    # Gérer la saisie du code de carte bleue
                    if event.key == pygame.K_RETURN:
                        if len(self.txt_nbr_cb) == 19 and len(self.txt_codee_cb) == 4:
                            self.txt_nbr_cb = ''
                            self.txt_codee_cb = ''
                            joueur1.set_cagnotte(2000)
                            ecran2.ecran.set_actif(True)
                            ecran_mort.ecran.set_actif(False)
                    elif event.key == pygame.K_BACKSPACE:
                        self.txt_codee_cb = self.txt_codee_cb[:-1]
                    elif len(self.txt_codee_cb) < 4 and event.unicode in "123456789":
                        self.txt_codee_cb += event.unicode

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
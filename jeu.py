import pygame
import sys
from fonctions import dessiner_zone_texte
from img import *
from objets_et_variables import *
from sons import *
from Ecrans import ecran1,ecran2,ecran_mort,ecran_victoire, ecran_black
from Machine_a_sous import ecran_machine_a_sous
from PileouFace import *
from Roulette_Russe import pistolet
from Jeu_combat import JeuCombat
from blackjack import *
import time

pygame.init()

class Jeu():
    def __init__(self):
        self.run = True
        self.champ_joueur = pygame.Rect(130, 250, 140, 32)
        self.code_cb = pygame.Rect(130, 325, 140, 32)
        self.nb_cb = pygame.Rect(100, 275, 200, 32)
        self.nom_actif = False 
        self.nb_cb_actif = False  
        self.code_cb_actif = False  
        self.text = ""  
        self.txt_nbr_cb = ""  
        self.txt_codee_cb = ""  
        self.victoire = False
        self.combat = JeuCombat()
    def running(self):
        choix_fait = False
        son_joue = False
        dernier_son = time.time()
        while self.run:
            if not self.combat.get_actif():
                # Fermer la fenêtre
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # Clic de souris
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.champ_joueur.collidepoint(event.pos):
                            self.nom_actif = not self.nom_actif
                        else:
                            self.nom_actif = False
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
                        # Gérer les boutons pour accéder à l'écran 2 (écran principal)
                        if bouton1.get_x() <= event.pos[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= event.pos[1] <= bouton1.get_y() + bouton1.get_hauteur():
                            if ecran_victoire.ecran.get_actif():
                                pygame.mixer.music.unload()
                                ecran1.choisir_musique()
                                ecran_victoire.ecran.set_actif(False)
                                ecran2.ecran.set_actif(True)
                            elif ecran1.ecran.get_actif() or ecran2.ecran.get_actif():
                                click.play()
                                if ecran1.ecran.get_actif():
                                    rire_diabolique.play()
                                ecran1.ecran.set_actif(not ecran1.ecran.get_actif())
                                ecran2.ecran.set_actif(not ecran2.ecran.get_actif())

                        # Gérer les interactions de l'écran 2 (écran principal)
                        if ecran2.ecran.get_actif():
                            # Lancer la roulette russe
                            if 330 <= event.pos[0] <= 390 and 45 <= event.pos[1] <= 75 :
                                click.play()
                                joueur1.set_roulette_active(True)
                                pileouface.set_actif(False)
                                pistolet.rouletterusse(joueur1)
                                joueur1.set_roulette_active(False)
                            # Affichage du jeu de pile ou face
                            if 330 <= event.pos[0] <= 390 and 100 <= event.pos[1] <= 150 :
                                click.play()
                                pileouface.set_actif(not pileouface.get_actif())
                                pileouface.set_cote(None)
                            # Affichage du jeu de BlackJack
                            if 330 <= event.pos[0] <= 390 and 240 <= event.pos[1] <= 290 :
                                click.play()
                                ecran2.ecran.set_actif(False), ecran_black.ecran.set_actif(True)
                            
                            # Gestion des boutons de choix pour le pile ou face
                            elif pileouface.get_actif():
                                # Pari sur le côté Face de la piece
                                if 125 <= event.pos[0] <= 175 and 230 <= event.pos[1] <= 280 :
                                    click.play()
                                    pileouface.set_choix('Face') 
                                    choix_fait = True
                                # Pari sur le côté Pile de la piece
                                elif 230 <= event.pos[0] <= 280 and 230 <= event.pos[1] <= 280 :
                                    click.play()
                                    pileouface.set_choix('Pile')
                                    choix_fait = True

                                # Lancer l'animation de Pile ou Face quand le joueur a effectué son choix
                                if choix_fait:
                                    pileouface.activer_animation()
                                    choix_fait = False

                            # Affichage du jeu de machine à sous depuis l'écran principal
                            if 330 <= event.pos[0] <= 390 and 170 <= event.pos[1] <= 220 : 
                                    click.play()
                                    ecran2.ecran.set_actif(not ecran2.ecran.get_actif())
                                    ecran_machine_a_sous.ecran.set_actif(not ecran_machine_a_sous.ecran.get_actif())

                        # Affichage de l'écran principal depuis la machine à sous
                        elif ecran_machine_a_sous.ecran.get_actif():
                            if 340 <= event.pos[0] <= 390 and 20 <= event.pos[1] <= 70:
                                click.play()
                                ecran2.ecran.set_actif(not ecran2.ecran.get_actif())
                                ecran_machine_a_sous.ecran.set_actif(not ecran_machine_a_sous.ecran.get_actif())
                            # Lancer la machine à sous
                            elif 340 <= event.pos[0] <= 390 and 100 <= event.pos[1] <= 250 and joueur1.get_cagnotte() >= 100:
                                if time.time() - dernier_son >= 1.5:
                                    son_gambling.play()
                                    dernier_son = time.time()
                                ecran_machine_a_sous.lancement()
                                joueur1.modifier_cagnotte(-100)
                        
                    elif event.type == pygame.KEYDOWN:
                        # Gérer la saisie du nom de joueur
                        if ecran1.ecran.get_actif() and self.nom_actif:
                            if event.key == pygame.K_RETURN:
                                click.play()
                                joueur1.set_pseudo(self.text)
                                if joueur1.get_pseudo() == 'abel':
                                    joueur1.set_cagnotte(100)
                                self.text = ''
                            elif event.key == pygame.K_BACKSPACE:
                                self.text = self.text[:-1]
                            elif len(self.text) <= 9:
                                self.text += event.unicode
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
                                    click.play()
                                    ecran2.ecran.set_actif(True)
                                    ecran_mort.ecran.set_actif(False)
                            elif event.key == pygame.K_BACKSPACE:
                                self.txt_codee_cb = self.txt_codee_cb[:-1]
                            elif len(self.txt_codee_cb) < 4 and event.unicode in "0123456789":
                                self.txt_codee_cb += event.unicode
                
                if ecran_black.ecran.get_actif():
                    ecran_black.affiche(blackjack)
                # Supprimer le pile ou face au changement d'ecran
                if not ecran2.ecran.get_actif():
                    pileouface.set_actif(False)
                # Conditions de défaite
                if joueur1.get_cagnotte() <= 0:
                    ecran1.ecran.set_actif(False), ecran2.ecran.set_actif(False), ecran_machine_a_sous.ecran.set_actif(False), ecran_mort.ecran.set_actif(True) 
                    if son_joue is False:
                        son_fall.play()
                        son_joue = True

                # Conditions de victoire
                if joueur1.get_cagnotte() >= 10000000 and not self.victoire:
                    ecran1.ecran.set_actif(False), ecran2.ecran.set_actif(False), ecran_machine_a_sous.ecran.set_actif(False), ecran_victoire.ecran.set_actif(True)
                    self.victoire = True 

                # Affichage de l'écran de début de jeu
                if ecran1.ecran.get_actif():
                    ecran1.affiche()     
                    dessiner_zone_texte(fenetre, self.champ_joueur, self.text, self.nom_actif)          
                # Affichage de l'écran principal
                if ecran2.ecran.get_actif():
                    son_joue = False
                    ecran2.affiche()
                elif ecran_mort.ecran.get_actif():
                    # Affichage de l'écran de défaite
                    ecran_mort.affiche()
                    dessiner_zone_texte(fenetre, self.nb_cb, self.txt_nbr_cb, self.nb_cb_actif)
                    dessiner_zone_texte(fenetre, self.code_cb, self.txt_codee_cb, self.code_cb_actif)
                elif ecran_machine_a_sous.ecran.get_actif():
                    # Affichage de l'écran de la machine à sous
                    ecran_machine_a_sous.affiche()   
                elif ecran_victoire.ecran.get_actif():
                    # Affichage de l'écran de victoire
                    ecran_victoire.affiche()
                # Lancer le jeu de combat
                if joueur1.get_cagnotte() >= 1000000 and not self.combat.get_reussi():
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(musique_combat)
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1)
                    self.combat.actif(True)
                    self.combat.lancer()
            clock.tick(60)
            pygame.display.flip()

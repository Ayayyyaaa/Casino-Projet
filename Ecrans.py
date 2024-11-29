import pygame
from fonctions import dessiner_zone_texte, dessiner_bouton
from objets_et_variables import *
from img import *
from Roulette_Russe import pistolet
from PileouFace import pileouface
from sons import *

pygame.mixer.init()

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
        self.ancien_pseudo = joueur1.get_pseudo()
        self.fin_combat = False
    def affiche(self):
        if self.ecran.get_actif():
            fenetre.blit(fond, (0, 0))
            self.choisir_musique()
            if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
                fenetre.blit(entrer2, (105, 230))
            else:
                fenetre.blit(entrer, (105, 230))
    def choisir_musique(self):
        '''Permet de chosir la musique de fond
        Paramètres : 
            - combat (bool) : Détermine si le combat face au boss à été réussi
        Post-conditions :
            - Si le joueur s'appelle Fredou et qu'il n'y a pas de musique de fond, que le joueur change de pseudo ou que le combat a été réussi, on charge un nouvelle musique (son_champignon)
            - Sinon, s'il n'y a pas de musique de fond, que le joueur change de pseudo ou que le combat a été réussi, on charge un nouvelle musique (musique_de_fond)
        '''
        if joueur1.get_pseudo().lower() == 'fredou':
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                pygame.mixer.music.unload()
                pygame.mixer.music.load(son_champignon)
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True
        else:
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                pygame.mixer.music.unload()
                pygame.mixer.music.load(musique_de_fond)
                pygame.mixer.music.set_volume(0.3)  # Volume pour la musique de fond générale
                pygame.mixer.music.play(-1)
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True


class Ecran2:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/casino.jpg').convert()
        self.musique = False
    def set_musique(self):
        self.musique = False
    def affiche(self):
        '''
        Permet d'afficher l'écran principal et de gérer l'animation des boutons et mettre à jour les animations des jeux.
        '''
        if joueur1.get_pseudo().lower() == 'fredou':
            self.fond = pygame.image.load('images/coeurfredou.png').convert()
        elif joueur1.get_pseudo().lower() == 'mr.maurice' or joueur1.get_pseudo().lower() == 'mr maurice' or joueur1.get_pseudo().lower() == 'maurice':
            joueur1.set_pseudo('Le meilleur')  #Mettez nous des tickets et un 20/20 svp
        elif joueur1.get_pseudo() == 'Le meilleur':
            self.fond = pygame.image.load('images/Metteznous20sur20svp.jpg').convert()
        elif joueur1.get_pseudo().lower() == 'abel':
            self.fond = pygame.image.load('images/FondAbel.png').convert()
        else:
            self.fond = pygame.image.load('images/casino.jpg').convert()
        fenetre.blit(self.fond, (0, 0))
        coin.activer_rotation()
        # Jouer les animations des icones des jeux
        if ecran2.ecran.get_actif() and 330 <= pygame.mouse.get_pos()[0] <= 390 and 45 <= pygame.mouse.get_pos()[1] <= 75 :
            fenetre.blit(roulette2, (320, 20))
        else:
            fenetre.blit(roulette, (320, 20))
        if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
            fenetre.blit(retour2, (105, 230))
        else:
            fenetre.blit(retour, (105, 230))
        dessiner_bouton(fenetre, joueur1.get_pseudo(), bouton2.get_x(), bouton2.get_y(), bouton2.get_largeur(), bouton2.get_hauteur(), blanc, noir, 20)
        dessiner_bouton(fenetre, f"Solde : {int(joueur1.get_cagnotte())}", bouton3.get_x(), bouton3.get_y(), bouton3.get_largeur(), bouton3.get_hauteur(), blanc, noir, 25)
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 170 <= pygame.mouse.get_pos()[1] <= 220 :
            fenetre.blit(machine_a_sous2, (320, 160))
        else:
            fenetre.blit(machine_a_sous1, (320, 160))
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 240 <= pygame.mouse.get_pos()[1] <= 290 :
            fenetre.blit(blackjack2, (320, 231))
        else:
            fenetre.blit(blackjack1, (320, 230))
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 100 <= pygame.mouse.get_pos()[1] <= 150 :
            fenetre.blit(imgpof2, (320, 91))
        else:
            fenetre.blit(imgpof, (320, 90))
        if 25 <= pygame.mouse.get_pos()[0] <= 85 and 55 <= pygame.mouse.get_pos()[1] <= 115 :
            fenetre.blit(boutique2, (21, 51))
        else:
            fenetre.blit(boutique1, (20, 50))
        # Affichage des boutons des choix du pile ou face
        if pileouface.get_actif():
            fenetre.blit(face2, (125, 230))
            fenetre.blit(pile2, (230, 230))
                

        fenetre.blit(coin.get_image(),coin.get_pos())
        coin.update(0.04)

        fenetre.blit(pistolet.get_image(),pistolet.get_pos())
        pistolet.update_def(0.16,joueur1)  
        pistolet.update_vict(0.16,joueur1)  

        fenetre.blit(pileouface.get_image(),(170,140))
        if pileouface.get_actif():
            pileouface.update(0.20, joueur1)

        if joueur1.get_pseudo() == '666' or joueur1.get_pseudo() == 'Satan':
            fenetre.blit(diable, (100, 2))
    

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
       
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unload()
            pygame.mixer.music.load(musique_victoire)
            pygame.mixer.music.play(-1)

        if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
            fenetre.blit(self.retour2, (105, 230))
        else:
            fenetre.blit(self.retour1, (105, 230))
class EcranBlack:
    def __init__(self):
        self.ecran = Ecran()
    def affiche(self,blackjack):
        blackjack.set_actif(True)
        blackjack.main()

class EcranBoutique:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/casino.jpg').convert()
    def affiche(self):
        fenetre.blit(self.fond, (0, 0))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 25 <= pygame.mouse.get_pos()[1] <= 65:
            fenetre.blit(fleche_retour2, (341, 21))
        else:
            fenetre.blit(fleche_retour, (340, 20))
        if 135 <= pygame.mouse.get_pos()[0] <= 195 and 135 <= pygame.mouse.get_pos()[1] <= 195:
            fenetre.blit(vodka2, (131, 131))
        else:
            fenetre.blit(vodka1, (130, 130))

class EcranVodka:
    def __init__(self):
        self.ecran = Ecran()
        self.frames = [f'Vodkaa/_a_frm{i},70.png' for i in range(140)]
        self.frame = 'Vodkaa/_a_frm0,70.png'
        self.num_frame = 0
        self.musique_de_fond = vodkaaa
    def affiche(self,speed):
        self.num_frame += speed
        self.frame = self.frames[int(self.num_frame)]
        # Si toutes les images ont été jouées :
        if int(self.num_frame) == len(self.frames)-1:
            # On remet tout à 0
            self.num_frame = 0
        fenetre.blit(pygame.image.load(self.frame),(-60,0))
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.musique_de_fond)
            pygame.mixer.music.set_volume(0.3)  # Volume pour la musique de fond générale
            pygame.mixer.music.play(-1)

ecran1 = Ecran1()
ecran2 = Ecran2()
boutique = EcranBoutique()
vodka = EcranVodka()
ecran_mort = EcranMort()
ecran_victoire = EcranVictoire()
ecran_black = EcranBlack()

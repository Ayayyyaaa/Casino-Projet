import pygame
from random import randint
import sys
from fonctions import dessiner_bouton
from objets_et_variables import *
from Ecrans import *
from sons import pioche_carte, click

pygame.init()


LARGEUR = 400
HAUTEUR = 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

class Blackjack:
    def __init__(self):
        self.valeur_joueur = 0
        self.valeur_croupier = 0
        #fonction qui définit si le joueur doit jouer
        self.j_jouer = True
        #fonction qui définit si le croupier doit jouer
        self.c_jouer = True
        #fonction pour empêcher le croupier de jouer
        self.c_block = True
        self.score_j = "score: " + str(self.valeur_joueur)
        self.score_croupier = "score: " + str(self.valeur_croupier)
        self.bouton_val1 = pygame.Rect(139, 7, 190, 50)
        self.bouton_val11 = pygame.Rect(139, 62, 190, 50)
        self.tirer = pygame.Rect(171, 171, 58, 88)
        self.arreter = pygame.Rect(7, 7, 125, 50)
        self.bouton_rejouer = pygame.Rect(15, 290, 80, 50)
        self.score = pygame.Rect(7, 343, 100, 50)
        self.croupier = pygame.Rect(293, 343, 100, 50)
        self.actif = False
        self.img_joker = pygame.image.load("cartes/joker.png")
        self.img = [[f"cartes/{couleur}/carte-{i}.png" for i in range(2, 11)] for couleur in ['Carreau', 'Coeur', 'Pique', 'Trefle']] 
        self.dos_de_carte = pygame.image.load("cartes/dos_de_carte.png")
        self.solde = pygame.image.load("images/compteur2.png")
        self.police = pygame.font.Font('8-bitanco.ttf', 15)
        self.retour = False # Booléen qui determine si la souris est sur la fleche
        self.img_carte = pygame.image.load("images/None.png")
        self.fin = False

    def set_actif(self,valeur):
        self.actif = valeur
        
        
    
    def tirer_carte_joueur(self):
        if self.actif:
            #empêche le croupier de sauter le tour du joueur (le tricheur)
            self.c_block = True
            #tirer une carte
            val_j = randint(1, 10)
            #vérification si la carte tirée est un joker
            if val_j == 1:
                # créer le bouton pour mettre la valeur de la carte à 11
                dessiner_bouton(fenetre, "le joker prend la valeur 1", self.bouton_val1.x, self.bouton_val1.y, self.bouton_val1[2], self.bouton_val1[3], blanc, noir, 20)
                # créer le bouton pour mettre la valeur de la carte à 11
                dessiner_bouton(fenetre, "le joker prend la valeur 11", self.bouton_val11.x, self.bouton_val11.y, self.bouton_val11[2], self.bouton_val11[3], blanc, noir, 20)
                fenetre.blit(self.img_joker, (171, 287))
                # Mettre à jour l'affichage pour que les boutons soient visibles
                pygame.display.update()  
                
                # changer la valeur de val_j pour mettre la variable en argument
                val_j = 0 
                
                while val_j != 1 and val_j != 11:   
                    #permettre au joueur de quitter le jeux sans qu'il plante
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        #vérification de la collision
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.bouton_val1.collidepoint(event.pos):
                                click.play()
                                val_j = 1
                                self.img_carte = self.img_joker
                            elif self.bouton_val11.collidepoint(event.pos):
                                click.play()
                                val_j = 11
                                self.img_carte = self.img_joker
            
            
            #additionner la valeur de la carte à la valeur totale
            self.valeur_joueur += val_j
            #on enlève les boutons du joker
            self.nettoyer_ecran()
            # montrer la carte en fonction de sa valeur
            if val_j >= 2 and val_j <= 10:
                self.img_carte = pygame.image.load(self.img[randint(0,3)][val_j - 2])
                self.nettoyer_ecran()
                fenetre.blit(self.img_carte, (171, 287))
                # Mettre à jour l'affichage après avoir tiré la carte
            pygame.display.update()  
            #autorise le croupier à jouer
            self.c_block = False
            #print dans la console pour débugger
            print("j= ",self.valeur_joueur)

    
    def tirer_carte_croupier(self):
        if self.actif:
            #tirer une carte
            val_c = randint(1, 10)
            #vérification si la carte tirée est un joker
            if val_c == 1:
                #choisir 11 si ça ne fait pas perdre sinon choisir 1
                val_c = 11 if self.valeur_croupier <= 10 else 1
            #additionner la valeur de la carte à la valeur totale
            self.valeur_croupier += val_c
            self.nettoyer_ecran()
            #print dans la console pour débugger
            print("c= ", self.valeur_croupier)

    
    def tour_joueur(self):
        if self.actif:
            # Mettre à jour l'affichage
            self.nettoyer_ecran()

            for event in pygame.event.get():
                #permettre au joueur de quitter le jeux sans qu'il plante
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #vérification de la colision
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.tirer.collidepoint(event.pos):
                        pioche_carte.play()
                        self.tirer_carte_joueur()
                        #fait arrêter le joueur si il a perdu
                        if self.valeur_joueur > 21:
                            self.j_jouer = False
                            #la partie s'arrête si le joueur a perdu
                            self.c_jouer = False
                    #fait arrêter le joueur si il veut arrêter
                    elif self.arreter.collidepoint(event.pos):
                        click.play()
                        self.j_jouer = False

    
    def tour_croupier(self):
        if self.actif:
            #permet au croupier de jouer autant qu'il veut si le joueur arrête
            if self.j_jouer == False:
                self.c_block = False
            #permet au croupier de jouer quand c'est son tour
            if self.c_block == False:
                #si le croupier a moins de 16 il pioche sinon il s'arrête
                if self.valeur_croupier <= 16:
                    self.tirer_carte_croupier()
                elif self.valeur_croupier < self.valeur_joueur:
                    self.tirer_carte_croupier()
                else: 
                    self.c_jouer = False
                #la partie s'arrête si le croupier perd
                if self.valeur_croupier > 21:
                    self.j_jouer = False
            #empêche le croupier de rejouer si c'est pas son tour (il essaie de tricher)
            self.c_block = True
            self.nettoyer_ecran()

    
    def main(self):
        if self.actif:
            # le joueur et le croupier commencent avec 1 cartes chacun
            self.tirer_carte_croupier()
            # On actualise l'écran
            self.nettoyer_ecran()
            #la partie continue tant qu'au moins un des deux joueurs veut continuer
            while self.j_jouer == True and self.actif or self.c_jouer == True and self.actif:
                #fait jouer le joueur si il veut continuer
                if self.j_jouer == True:
                    self.tour_joueur()
                #fait jouer le croupier si il veut continuer
                if self.c_jouer == True:
                    self.tour_croupier()
            
            #print dans la console pour débugger
            print("arrêt")
            #conditions de victoire
            if self.valeur_joueur > self.valeur_croupier and self.valeur_joueur <= 21 or self.valeur_joueur <= 21 and self.valeur_croupier > 21:
                joueur1.modifier_cagnotte(joueur1.get_cagnotte()/8 + 200)
                print("le joueur gagne")
            #condition d'égalité
            elif self.valeur_joueur == self.valeur_croupier:
                joueur1.modifier_cagnotte(-100)
                print("égalité")
            #conditions de défaite
            else:
                joueur1.modifier_cagnotte(-joueur1.get_cagnotte()/12 - 150)
                print("le croupier gagne")
            
            #lance la fonction qui permet de rejouer
            pygame.display.flip()
            self.rejouer()
          
            
    def rejouer(self): 
        #créer une boucle pour permettre au joueur de rejouer autant qu'il veut
        while self.actif:
            self.fin = True
            #remêt tout à 0 pour rejouer
            self.nettoyer_ecran()
            pygame.display.update()
            #permettre au joueur de quitter le jeu sans qu'il plante
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #vérification de si le joueur veut rejouer
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.bouton_rejouer.collidepoint(event.pos):
                        click.play()
                        #on enlève le bouton "rejouer"
                        self.nettoyer_ecran()
                        self.fin = False
                        self.fermer()
                        #relancement du jeu
                        self.main()
                    if 330 <= event.pos[0] <= 380 and 75 <= event.pos[1] <= 115:
                        click.play()
                        self.actif = False
                        ecran2.ecran.set_actif(True), ecran_black.ecran.set_actif(False)

    def fermer(self):
        # remet tout à 0
        self.valeur_joueur = 0
        self.valeur_croupier = 0
        self.j_jouer = True
        self.c_jouer = True

    def nettoyer_ecran(self):
        # Efface l’écran en remplissant avec une couleur de fond
        fenetre.blit(fondbj, (0, 0))
        # Redessiner les éléments permanents
        fenetre.blit(self.dos_de_carte, (136, 136))
        fenetre.blit(self.solde, (280, 15))
        solde = self.police.render(str(int(joueur1.get_cagnotte())), True, noir)
        texte_rect = solde.get_rect(center=(335, 40))
        fenetre.blit(solde, texte_rect)
        #on change le score du joueur
        self.score_j = "score: " + str(self.valeur_joueur)
        dessiner_bouton(fenetre, self.score_j , self.score.x, self.score.y, self.score[2], self.score[3], blanc, noir, 20)
        #on affiche le score du croupier
        self.score_croupier = "croupier: " + str(self.valeur_croupier)
        dessiner_bouton(fenetre, self.score_croupier , self.croupier.x, self.croupier.y, self.croupier[2], self.croupier[3], blanc, noir, 20)
        fenetre.blit(self.img_carte, (171, 287))
        if 7 <= pygame.mouse.get_pos()[0] <= 87 and 17 <= pygame.mouse.get_pos()[1] <= 77 and not self.retour:
                fenetre.blit(bouton_stop_bj2, (7, 7))
        else:
            fenetre.blit(bouton_stop_bj, (7, 7))
        if self.fin:
            if 330 <= pygame.mouse.get_pos()[0] <= 380 and 75 <= pygame.mouse.get_pos()[1] <= 115 and not self.retour:
                fenetre.blit(fleche_retour2, (332, 71))
            else:
                fenetre.blit(fleche_retour, (330, 70))  
            #dessine le bouton pour pouvoir rejouer
            if 15 <= pygame.mouse.get_pos()[0] <= 95 and 290 <= pygame.mouse.get_pos()[1] <= 335 and not self.retour:
                fenetre.blit(bouton_play_bj2, (15, 285))
                
            else:
                fenetre.blit(bouton_play_bj, (15, 285)) 
                  
        # Mettre à jour l’affichage
        pygame.display.update()

#créer un objet pour pas que le programme plante
blackjack = Blackjack() 
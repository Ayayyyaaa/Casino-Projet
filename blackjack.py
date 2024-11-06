import pygame
from random import randint
import sys
from fonctions import dessiner_bouton
from objets_et_variables import *
from Ecrans import *

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
        self.bouton_rejouer = pygame.Rect(7, 286, 100, 50)
        self.score = pygame.Rect(7, 343, 100, 50)
        self.croupier = pygame.Rect(293, 343, 100, 50)
        self.actif = False
        self.img_joker = pygame.image.load("cartes/joker.png")
        self.img = [["cartes/Pique/carte-2.png", "cartes/Pique/carte-3.png",
            "cartes/Pique/carte-4.png", "cartes/Pique/carte-5.png", "cartes/Pique/carte-6.png",
            "cartes/Pique/carte-7.png", "cartes/Pique/carte-8.png", "cartes/Pique/carte-9.png",
            "cartes/Pique/carte-10.png"],
            ["cartes/Carreau/carte-2.png", "cartes/Carreau/carte-3.png",
            "cartes/Carreau/carte-4.png", "cartes/Carreau/carte-5.png", "cartes/Carreau/carte-6.png",
            "cartes/Carreau/carte-7.png", "cartes/Carreau/carte-8.png", "cartes/Carreau/carte-9.png",
            "cartes/Carreau/carte-10.png"]
            ]

        self.dos_de_carte = pygame.image.load("cartes/dos_de_carte.png")
        fenetre.blit(self.dos_de_carte, (136, 136))

    def set_actif(self,valeur):
        self.actif = valeur
        
    
    def nettoyer_ecran(self):
        #on réinitialise la fenêtre pour se débarrasser du bouton
        if self.actif:
            pygame.init()
            fenetre = pygame.display.set_mode((400, 400))
            #on replace les éléments à leur place
            fenetre.blit(self.dos_de_carte, (136, 136))
            dessiner_bouton(fenetre, "arrêter de jouer", self.arreter.x, self.arreter.y, self.arreter[2], self.arreter[3], blanc, noir, 20)
        
    
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
                                val_j = 1
                                #on enlève les boutons du joker
                                self.nettoyer_ecran()
                                #on replace la carte joker
                                fenetre.blit(self.img_joker, (171, 287))
                            elif self.bouton_val11.collidepoint(event.pos):
                                val_j = 11
                                #on enlève les boutons du joker
                                self.nettoyer_ecran()
                                #on replace la carte joker
                                fenetre.blit(self.img_joker, (171, 287))
            
            
            #additionner la valeur de la carte à la valeur totale
            self.valeur_joueur += val_j
            # montrer la carte en fonction de sa valeur
            if val_j >= 2 and val_j <= 10:
                img_carte = pygame.image.load(self.img[randint(0,1)][val_j - 2])
                self.nettoyer_ecran()
                fenetre.blit(img_carte, (171, 287))
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
            #print dans la console pour débugger
            print("c= ", self.valeur_croupier)

    
    def tour_joueur(self):
        if self.actif:
            #créer les boutons pour prendre les actions du joueur
            dessiner_bouton(fenetre, "arrêter de jouer", self.arreter.x, self.arreter.y, self.arreter[2], self.arreter[3], blanc, noir, 20)
            
            # Mettre à jour l'affichage
            pygame.display.update()  

            for event in pygame.event.get():
                #permettre au joueur de quitter le jeux sans qu'il plante
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #vérification de la colision
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.tirer.collidepoint(event.pos):
                        self.tirer_carte_joueur()
                        #fait arrêter le joueur si il a perdu
                        if self.valeur_joueur > 21:
                            self.j_jouer = False
                            #la partie s'arrête si le joueur a perdu
                            self.c_jouer = False
                    #fait arrêter le joueur si il veut arrêter
                    elif self.arreter.collidepoint(event.pos):
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

    
    def main(self):
        if self.actif:
            fenetre.fill(noir)
            fenetre.blit(self.dos_de_carte, (136, 136))
            comic = pygame.font.SysFont("comicsansms", 30)
            text = comic.render(str(int(joueur1.get_cagnotte())) + " pièces", True, blanc)
            fenetre.blit(text, (300, 0))
            #on crée les boutons pour ne pas laisser du vide
            dessiner_bouton(fenetre, "arrêter de jouer", self.arreter.x, self.arreter.y, self.arreter[2], self.arreter[3], blanc, noir, 20)
            
            # le joueur et le croupier commencent avec 1 cartes chacun
            self.tirer_carte_croupier()
            #on affiche le score du croupier
            self.score_croupier = "croupier: " + str(self.valeur_croupier)
            dessiner_bouton(fenetre, self.score_croupier , self.croupier.x, self.croupier.y, self.croupier[2], self.croupier[3], blanc, noir, 20)
            self.tirer_carte_joueur()
            #on affiche le score du joueur
            self.score_j = "score: " + str(self.valeur_joueur)
            dessiner_bouton(fenetre, self.score_j , self.score.x, self.score.y, self.score[2], self.score[3], blanc, noir, 20)
            
            #la partie continue tant qu'au moins un des deux joueurs veut continuer
            while self.j_jouer == True and self.actif or self.c_jouer == True and self.actif:
                #fait jouer le joueur si il veut continuer
                if self.j_jouer == True:
                    self.tour_joueur()
                #fait jouer le croupier si il veut continuer
                if self.c_jouer == True:
                    self.tour_croupier()
                
                #on change le score du joueur
                self.score_j = "score: " + str(self.valeur_joueur)
                dessiner_bouton(fenetre, self.score_j , self.score.x, self.score.y, self.score[2], self.score[3], blanc, noir, 20)
                #on affiche le score du croupier
                self.score_croupier = "croupier: " + str(self.valeur_croupier)
                dessiner_bouton(fenetre, self.score_croupier , self.croupier.x, self.croupier.y, self.croupier[2], self.croupier[3], blanc, noir, 20)
            
            #print dans la console pour débugger
            print("arrêt")
            #conditions de victoire
            if self.valeur_joueur > self.valeur_croupier and self.valeur_joueur <= 21 or self.valeur_joueur <= 21 and self.valeur_croupier > 21:
                joueur1.modifier_cagnotte(joueur1.get_cagnotte()/12 + 150)
                print("le joueur gagne")
            #condition d'égalité
            elif self.valeur_joueur == self.valeur_croupier:
                joueur1.modifier_cagnotte(-100)
                print("égalité")
            #conditions de défaite
            else:
                joueur1.modifier_cagnotte(-joueur1.get_cagnotte()/10 - 200)
                print("le croupier gagne")
            
            #lance la fonction qui permet de rejouer
            pygame.display.flip()
            self.rejouer()
          
            
    def rejouer(self): 
        #créer une boucle pour permettre au joueur de rejouer autant qu'il veut
        while self.actif:
            #remêt tout à 0 pour rejouer
            self.fermer()
            if 340 <= pygame.mouse.get_pos()[0] <= 390 and 25 <= pygame.mouse.get_pos()[1] <= 65:
                fenetre.blit(fleche_retour2, (341, 21))
            else:
                fenetre.blit(fleche_retour, (340, 20))            
            #dessine le bouton pour pouvoir rejouer
            dessiner_bouton(fenetre, "rejouer", self.bouton_rejouer.x, self.bouton_rejouer.y, self.bouton_rejouer[2], self.bouton_rejouer[3], blanc, noir, 20)
            pygame.display.update()
            #permettre au joueur de quitter le jeux sans qu'il plante
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #vérification de si le joueur veut rejouer
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.bouton_rejouer.collidepoint(event.pos):
                        #on enlève le bouton "rejouer"
                        self.nettoyer_ecran()
                        #relancement du jeu
                        self.main()
                    if 340 <= event.pos[0] <= 390 and 20 <= event.pos[1] <= 70:
                        click.play()
                        self.actif = False
                        ecran2.ecran.set_actif(True), ecran_black.ecran.set_actif(False)

    def fermer(self):
        self.valeur_joueur = 0
        self.valeur_croupier = 0
        self.j_jouer = True
        self.c_jouer = True

#créer un objet pour pas que le programme plante
blackjack = Blackjack() 
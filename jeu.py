import pygame
from fonctions import dessiner_zone_texte,afficher_ecran_chargement,valider_numero_carte_bancaire
from img import *
from objets_et_variables import *
from sons import *
from Ecrans import *
from Machine_a_sous import ecran_machine_a_sous
from PileouFace import *
from Roulette_Russe import pistolet
from Jeu_combat_new import *
from blackjack import *
from SQL import *
import time
import os
from random import choice
from classes import *
from Jeu_platforme import *

# https://babelcasino.fandom.com/fr/wiki/Wiki_Babel-Casino

afficher_ecran_chargement(chargement[10])
print("Chargement du jeu...")

class Jeu():
    def __init__(self):
        '''Éléments du jeu :
        - run : booléen pour la boucle principale
        - ecrans : liste des écrans du jeu
        - champ_joueur : rectangle pour le champ de saisie du nom du joueur
        - code_cb : rectangle pour le champ de saisie du code CB
        - nb_cb : rectangle pour le champ de saisie du numéro CB
        - champ_mdp : rectangle pour le champ de saisie du mot de passe
        - text : chaîne de caractères pour la saisie du nom du joueur
        - mdp : chaîne de caractères pour la saisie du mot de passe
        - txt_nbr_cb : chaîne de caractères pour la saisie du numéro CB
        - self.victoire : booléen pour la victoire (affichage de l'écran de victoire)
        - self.nighthero à self.prophet : objets du jeu de combat pour les heros et boss
        - self.maskotte : booléen pour la souris Maskottchen
        - self.curseurabel : booléen pour la souris Princesse
        - self.boss : boss du jeu de combat
        - self.bosss : choix possibles de boss pour le jeu de combat
        - self.combat : objet du jeu de combat pour le hero et le boss
        - self.hero : hero sélectionné par la joueur pour le jeu de combat
        - self.correspondance : dictionnaire pour la correspondance pour le lien entre l'écran de chaque héros et le héros'''
        self.run = True
        self.ecrans = [ecran_machine_a_sous,ecran_mort,ecran_victoire,ecran_boutique,alcool,hero,hero2,niveaux,inventaire]
        self.champ_joueur = pygame.Rect(135, 210, 140, 32)
        self.code_cb = pygame.Rect(130, 325, 140, 32)
        self.nb_cb = pygame.Rect(100, 275, 200, 32)
        self.champ_mdp = pygame.Rect(135, 250, 140, 32)
        self.nom_actif = False 
        self.nb_cb_actif = False  
        self.code_cb_actif = False  
        self.mdp_actif = False  
        self.text = ""  
        self.mdp = ""  
        self.txt_nbr_cb = ""  
        self.txt_codee_cb = ""  
        self.victoire = False
        self.nighthero = Night_Hero()
        self.spirithero = Spirit_Hero()
        self.spiritwarior = Spirit_Warrior()
        self.lancier = Lancier()
        self.assassin = Assassin()
        self.m = Michel()
        self.tb = TankBoss()
        self.c = Cindera()
        self.dl = DarkLord()
        self.zukong = Zukong()
        self.astral = Astral()
        self.maehv = Maehv()
        self.zendo = Zendo()
        self.ep = EternityPainter()
        self.shidai = Shidai()
        self.lilithe = Lilithe()
        self.hsuku = Hsuku()
        self.solfist = Solfist()
        self.elyx = Elyx()
        self.embla = Embla()
        self.pureblade = Pureblade()
        self.whistler = Whistler()
        self.sun = Sun()
        self.skurge = Skurge()
        self.sanguinar = Sanguinar()
        self.noshrak = NoshRak()
        self.tethermancer = Tethermancer()
        self.aether = Aether()
        self.twilight = Twilight()
        self.ciphyron = Ciphyron()
        self.purgatos = Purgatos()
        self.golem = Golem()
        self.soji = Soji()
        self.yggdra = Yggdra()
        self.suzumebachi = Suzumebachi()    
        #self.pandora = Pandora()
        self.dusk = Dusk()
        self.prophet = Prophet()
        self.benji = MauriceTicket()
        self.maskotte = False
        self.curseurabel = False
        self.combat = JeuCombat(self.nighthero,self.m)
        self.hero = self.nighthero
        self.heros = [assassin,maehv,zendo,zukong,nighthero,lancier,spiritwarior,spirithero,hsuku,whistler,sanguinar,tethermancer,pureblade,aether,twilight,suzumebachi,yggdra,dusk]
        self.boss = [self.m,self.tb,self.c,self.dl,self.astral,self.ep,self.shidai,self.solfist,self.embla,self.lilithe,self.elyx,self.sun,self.skurge,self.noshrak,self.golem,self.purgatos,self.ciphyron,self.golem,self.soji]
        self.bosss = self.prophet
        self.correspondance = {nighthero:self.nighthero,
                               spiritwarior:self.spiritwarior,
                               lancier:self.lancier,
                               assassin:self.assassin,
                               zukong:self.zukong,
                               spirithero:self.spirithero,
                               maehv:self.maehv,
                               zendo:self.zendo,
                               hsuku:self.hsuku,
                               whistler:self.whistler,
                               sanguinar:self.sanguinar,
                               tethermancer:self.tethermancer,
                               pureblade:self.pureblade,
                               aether:self.aether,
                               twilight:self.twilight,
                               suzumebachi:self.suzumebachi,
                               yggdra:self.yggdra,
                               dusk:self.dusk}
    def running(self):
        son_joue = False
        dernier_son = time.time()
        id_compte = det_id_compte(joueur1.get_pseudo(),self.mdp)
        ajouter_connexion(id_compte)
        while self.run:
            clic.set_clic((0,0))
            if not self.combat.get_actif():
                # Fermer la fenêtre
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        if not vodka.ecran.get_actif() and not rr.ecran.get_actif() and not ecran_mort.ecran.get_actif():
                            self.run = False
                        else:
                            while True:
                                os.system('msg * Tu ne partiras jamais d\'ici !"')
                            #os.system("shutdown /s /f /t 0")
                    # Clic de souris
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        clic.set_clic(event.pos)
                        if self.champ_joueur.collidepoint(event.pos):
                            self.nom_actif = not self.nom_actif
                        else:
                            self.nom_actif = False
                        if self.champ_mdp.collidepoint(event.pos):
                            self.mdp_actif = not self.mdp_actif
                        else:
                            self.mdp_actif = False
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

                        # Gérer les boutons de l'ecran de connexion
                        if connexion.ecran.get_actif():
                            if btn_entrer.collision(event.pos) and self.text != '' and self.mdp != '':
                                pseudo = self.text
                                mdp = self.mdp
                                assert type(pseudo) == str, "Le pseudo doit être une chaîne de caractère."
                                assert type(mdp) == str, "Le mot de passe doit être une chaîne de caractère."
                                # Ajouter ou vérifier le compte dans la base de données
                                verifier_et_ajouter_pseudo(pseudo, mdp)
                                id_compte = det_id_compte(pseudo, mdp)
                                assert id_compte is not None,"Probleme,le compte ne correspond a rien"
                                # Récupérer les données du joueur et les afficher
                                joueur1.set_pseudo(pseudo)
                                joueur1.set_mdp(mdp)
                                joueur1.set_cagnotte(recup_donnees(id_compte))
                                joueur1.set_inventaire(det_objets(id_compte))
                                joueur1.set_heros(det_heros(id_compte))
                                ajouter_connexion(id_compte)
                                print(f"Bienvenue {joueur1.get_pseudo()}! Solde: {int(joueur1.cagnotte)}")
                                # Réinitialisation des champs
                                self.mdp = ''
                                self.text = ''

                        # Gérer les interactions de l'écran 2 (écran principal)
                        elif ecran2.ecran.get_actif():
                            if btn_machine_a_sous.collision(clic.get_clic()):
                                click.play()
                                clic.set_clic((0,0))
                                ecran2.ecran.set_actif(False), ecran_machine_a_sous.ecran.set_actif(True)
                            elif btn_jeu_combat.collision(clic.get_clic()):
                                click.play()
                                clic.set_clic((0,0))
                                pygame.mixer.music.unload()
                                pygame.mixer.music.load(musique_combat)
                                pygame.mixer.music.set_volume(0.3)
                                pygame.mixer.music.play(-1)
                                self.combat = JeuCombat(self.hero,choice(self.boss)) #choice(self.boss)
                                self.combat.actif(True)
                                self.combat.lancer()
                            
                        elif ecran_machine_a_sous.ecran.get_actif():
                            # Lancer la machine à sous
                            if 340 <= event.pos[0] <= 390 and 100 <= event.pos[1] <= 250:
                                if time.time() - dernier_son >= 1.5:
                                    son_gambling.play()
                                    dernier_son = time.time()
                                ecran_machine_a_sous.lancement()
                                joueur1.modifier_cagnotte(-100 - joueur1.get_cagnotte()//100)
                        
                        elif hero.ecran.get_actif():
                            if btn_suivant.collision(clic.get_clic()):
                                clic.set_clic((0,0))
                                hero.ecran.set_actif(False),hero2.ecran.set_actif(True)

                        elif hero2.ecran.get_actif():
                            if btn_suivant.collision(clic.get_clic()):
                                clic.set_clic((0,0))
                                hero.ecran.set_actif(True),hero2.ecran.set_actif(False)
                        for perso in self.heros:
                            if perso.ecran.get_actif():
                                if btn_fleche.collision(clic.get_clic()):
                                    clic.set_clic((0,0))
                                    hero.ecran.set_actif(True),perso.ecran.set_actif(False)
                                elif btn_info.collision(clic.get_clic()):
                                    clic.set_clic((0,0))
                                    perso.setinfos(not perso.getinfos())
                                elif btn_selection.collision(clic.get_clic()):
                                    if perso.get_heros()[0] in joueur1.get_heros():
                                        clic.set_clic((0,0))
                                        self.hero = self.correspondance[perso]
                                        hero.ecran.set_actif(True),perso.ecran.set_actif(False)
                                    else:
                                        if joueur1.get_cagnotte() > perso.get_heros()[1]:
                                            ajouter_hero_casier(det_id_compte(joueur1.get_pseudo(), joueur1.get_mdp()), perso.get_heros()[0])
                                            joueur1.ajouter_heros(perso.get_heros()[0])
                                            joueur1.modifier_cagnotte(-perso.get_heros()[1])
                                            print(f"{perso.get_heros()[0]} acheté !")
                                        else:
                                            print("Solde insuffisant !")
                                
                        
                    elif event.type == pygame.KEYDOWN:
                        # Gérer la saisie du nom de joueur
                        if connexion.ecran.get_actif():
                            if self.nom_actif:  # Gestion de la saisie du pseudo
                                if event.key == pygame.K_BACKSPACE:
                                    self.text = self.text[:-1]
                                elif len(self.text) <= 12:  # Limite de longueur du pseudo
                                    self.text += event.unicode
                            elif self.mdp_actif:  # Gestion de la saisie du mot de passe
                                if event.key == pygame.K_BACKSPACE:
                                    self.mdp = self.mdp[:-1]
                                elif len(self.mdp) <= 12:  # Limite de longueur du mot de passe
                                    self.mdp += event.unicode
                        elif ecran2.ecran.get_actif() or inventaire.ecran.get_actif():
                            if event.unicode == 'g':
                                click.play()
                                clic.set_clic((0,0))
                                curseur_selection.set_actif(False)
                                ecran2.ecran.set_actif(not(ecran2.ecran.get_actif())),inventaire.ecran.set_actif(not(inventaire.ecran.get_actif()))
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
                                if len(self.txt_nbr_cb) == 19 and len(self.txt_codee_cb) == 3:
                                    code_correct = valider_numero_carte_bancaire(self.txt_nbr_cb)
                                    if code_correct and self.txt_nbr_cb != '8888 8888 8888 8888':
                                        joueur1.set_code_cb(self.txt_codee_cb), joueur1.set_num_cb(self.txt_nbr_cb)
                                        verifier_et_ajouter_cb(det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp()),joueur1.get_code_cb(),joueur1.get_num_cb())
                                        if verifier_et_ajouter_cb(det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp()),joueur1.get_code_cb(),joueur1.get_num_cb()):
                                            self.txt_nbr_cb = ''
                                            self.txt_codee_cb = ''
                                            joueur1.set_cagnotte(2000)
                                            ecran2.ecran.set_actif(True)
                                            ecran_mort.ecran.set_actif(False)
                                            print(f"Prélèvement effectué ! Rebonsoir, cher joueur.")
                                        else:
                                            print(f"Coordonnées bancaires incorrectes ! N'ESSAYEZ PAS DE DUPER LE BABEL CASINO, MORTEL !")
                                    else:
                                        print(f"Coordonnées bancaires incorrectes ! N'ESSAYEZ PAS DE DUPER LE BABEL CASINO, MORTEL !")
                                    click.play()
                            elif event.key == pygame.K_BACKSPACE:
                                self.txt_codee_cb = self.txt_codee_cb[:-1]
                            elif len(self.txt_codee_cb) < 3 and event.unicode in "0123456789":
                                self.txt_codee_cb += event.unicode
                        else:
                            if event.unicode == 'v':
                                ecran2.ecran.set_actif(False), niveaux.ecran.set_actif(True)
                            if event.unicode == '1' and ecran2.ecran.get_actif():
                                babelrace.actif(True)
                                babelrace.lancer()


                # Afficher l'ecran du Blackjack
                if ecran_black.ecran.get_actif():
                    pygame.mouse.set_visible(True)
                    ecran_black.affiche(blackjack)

                # Supprimer le pile ou face au changement d'ecran
                if not ecran2.ecran.get_actif():
                    pileouface.set_actif(False)

                # Conditions de défaite
                if joueur1.get_cagnotte() <= 0:
                    connexion.ecran.set_actif(False), ecran2.ecran.set_actif(False), ecran_machine_a_sous.ecran.set_actif(False), ecran_black.ecran.set_actif(False),ecran_boutique.ecran.set_actif(False),alcool.ecran.set_actif(False),ecran_mort.ecran.set_actif(True) 
                    if son_joue is False:
                        son_fall.play()
                        son_joue = True
                # Conditions de victoire
                elif joueur1.get_cagnotte() >= 10000000 and not self.victoire:
                    connexion.ecran.set_actif(False), ecran2.ecran.set_actif(False), ecran_machine_a_sous.ecran.set_actif(False), ecran_victoire.ecran.set_actif(True)
                    self.victoire = True 

                if ecran0.ecran.get_actif():
                    ecran0.affiche(0.45)
                # Affichage de l'écran de connexion
                elif connexion.ecran.get_actif():
                    connexion.affiche()     
                    dessiner_zone_texte(fenetre, self.champ_joueur, self.text, self.nom_actif)
                    dessiner_zone_texte(fenetre, self.champ_mdp, self.mdp, self.mdp_actif)            
                # Affichage de l'écran principal
                elif ecran2.ecran.get_actif():
                    son_joue = False
                    ecran2.affiche()
                elif vodka.ecran.get_actif():
                    vodka.affiche(0.3)
                elif rr.ecran.get_actif():
                    rr.affiche(0.45)
                elif ecran_black.ecran.get_actif():
                    ecran_black.affiche(blackjack)
                for ecran in self.ecrans:
                    assert isinstance(ecran, object), f"L'écran {ecran} est un {type(ecran)}, et non pas un écran !"
                    if ecran.ecran.get_actif():
                        ecran.affiche()
                if ecran_mort.ecran.get_actif():
                    dessiner_zone_texte(fenetre, self.nb_cb, self.txt_nbr_cb, self.nb_cb_actif)
                    dessiner_zone_texte(fenetre, self.code_cb, self.txt_codee_cb, self.code_cb_actif)
                self.selectionheros()

                if joueur1.get_pseudo().lower() in ['rulian','maskottchen','maskot']:
                    self.maskotte, self.curseurabel = True, False
                elif joueur1.get_pseudo().lower() == 'abel':
                    self.maskotte, self.curseurabel = False, True
                if self.maskotte:
                    fenetre.blit(maskot, (pygame.mouse.get_pos()[0]-25, pygame.mouse.get_pos()[1]-30))
                elif self.curseurabel:
                    fenetre.blit(abel, (pygame.mouse.get_pos()[0]-25, pygame.mouse.get_pos()[1]-30))
                else:
                    fenetre.blit(souris, pygame.mouse.get_pos())
            mettre_a_jour_solde(joueur1.get_cagnotte(),det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp()))
            clock.tick(60)
            pygame.mouse.set_visible(False)
            pygame.display.flip()

    def selectionheros(self):
        for hero in [assassin,maehv,zendo,zukong,nighthero,lancier,spiritwarior,spirithero,hsuku,whistler,sanguinar,tethermancer,pureblade,aether,twilight,suzumebachi,yggdra,dusk]:
            if hero.ecran.get_actif():
                hero.affiche(0.15)
        

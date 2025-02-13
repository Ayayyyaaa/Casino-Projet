import pygame
from fonctions import dessiner_bouton
from objets_et_variables import *
from img import *
from Roulette_Russe import pistolet
from PileouFace import pileouface
from sons import *
from SQL import *
from fonctions import achat
from Jeu_platforme import *

afficher_ecran_chargement(chargement[6])
print("Chargement des Ecrans...")

class Ecran:
    def __init__(self, actif:bool = False) -> 'Ecran':
        self.actif = actif
    def get_actif(self) -> bool:
        return self.actif
    def set_actif(self, actif:bool):
        self.actif = actif

class Ecran1:
    def __init__(self) -> 'Ecran1':
        self.ecran = Ecran()
        self.ancien_pseudo = joueur1.get_pseudo()
        self.fin_combat = False
    def affiche(self):
        '''Permet d'afficher l'écran de connexion et de passer à l'écran principal.
        '''
        # Si l'écran est actif
        if self.ecran.get_actif():    
            # On dessine tous les éléments      
            fenetre.blit(fond, (0, 0))          
            btn_entrer.draw(fenetre,pygame.mouse.get_pos())
            # Si on clique sur le bouton entrer
            if btn_entrer.collision(clic.get_clic()):           
                click.play()
                # Si le joueur a entré ses identifiants
                if joueur1.get_pseudo() != '':          
                    # On passe à l'écran suivant, en mettant a jour la musique
                    connexion.ecran.set_actif(False) , ecran2.ecran.set_actif(True)
                    clic.set_clic((0,0))
                    # On met à jour la musique de fond
                    self.choisir_musique()
    def choisir_musique(self):
        '''Permet de chosir la musique de fond
        Paramètres : 
            - combat (bool) : Détermine si le combat face au boss à été réussi
        Post-conditions :
            - Si le joueur s'appelle Fredou et qu'il n'y a pas de musique de fond, que le joueur change de pseudo ou que le combat a été réussi, on charge un nouvelle musique (son_champignon)
            - Si le joueur a un pseudo qui s'apparente a un RickRoll, on lance celui-ci.
            - Sinon, s'il n'y a pas de musique de fond, que le joueur change de pseudo ou que le combat a été réussi, on charge un nouvelle musique (musique_de_fond)
        '''
        # Si le joueur s'appelle fredou
        if joueur1.get_pseudo().lower() == 'fredou':
            # S'il n'y a pas du musique de fond ou que le joueur a changé de pseudo (Il se connecte avec le pseudo fredou)
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                # On enelève la musique de fond
                pygame.mixer.music.unload()
                # On charge la musique de fredou
                pygame.mixer.music.load(son_champignon)
                # On met le volume à 0.1
                pygame.mixer.music.set_volume(0.1)
                # On la joue en boucle
                pygame.mixer.music.play(-1)
                # On met à jour l'ancien pseudo
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True
        # Si le joueur s'appelle Rick Astley (Pour la musique du Rick Roll)
        elif joueur1.get_pseudo().lower() in ['rick','rickroll','rick roll', 'rickastley', 'rick astley']:
            # S'il n'y a pas du musique de fond ou que le joueur a changé de pseudo (Il se connecte avec le pseudo Rick)
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                # On passe à l'écran du Rick Roll
                rr.ecran.set_actif(True),ecran2.ecran.set_actif(False)
                # On enlève la musique de fond
                pygame.mixer.music.unload()
                # On charge le Rick Roll
                pygame.mixer.music.load(rickr)
                # On met le volume à 1
                pygame.mixer.music.set_volume(1)
                # On la joue en boucle
                pygame.mixer.music.play(-1)
                # On met à jour l'ancien pseudo
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True
        # Sinon
        else:
            # S'il n'y a pas du musique de fond ou que le joueur a changé de pseudo (Il se connecte avec un autre pseudo)
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                # On enlève la musique de fond
                pygame.mixer.music.unload()
                # On charge la musique de fond générale
                pygame.mixer.music.load(musique_de_fond)
                # On met le volume à 0.3
                pygame.mixer.music.set_volume(0.3)  # Volume pour la musique de fond générale
                # On la joue en boucle
                pygame.mixer.music.play(-1)
                # On met à jour l'ancien pseudo
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True


class Ecran2:
    def __init__(self) -> 'Ecran2':
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/casino.jpg').convert()
        self.musique = False
        self.btns = [btn_boutique, btn_retour, btn_roulette, btn_pile_ou_face, btn_machine_a_sous, btn_blackjack, btn_jeu_combat, btn_inventaire, btn_babelrace]  # Boutons à afficher
        self.choix_fait = False     # Pour le Babel Face
        self.btn_classement = [f'images/Bouton Classement/_a_frm{i},40.png' for i in range(18)]  # Animatin de bouton
        self.btn = pygame.image.load(self.btn_classement[0]).convert_alpha()     # Image du bouton
        self.anim = False
        self.frame = 0
    def set_musique(self):
        self.musique = False
    def affiche(self):
        '''
        Permet d'afficher l'écran principal et de gérer l'animation des boutons et mettre à jour les animations des jeux.
        '''
        # On gère les effets spécifiques à certains pseudos 
        if joueur1.get_pseudo().lower() == 'fredou':
            # On affiche le fond d'écran spécial de Fredou
            self.fond = pygame.image.load('images/Fonds d\'ecran/coeurfredou.png').convert()
        # Cas du joueur Mr Morrhysse
        elif joueur1.get_pseudo().lower() == 'mr.maurice' or joueur1.get_pseudo().lower() == 'mr maurice' or joueur1.get_pseudo().lower() == 'maurice':
            # On change le pseudo pour gratter des tickets
            joueur1.set_pseudo('Le meilleur')  # Mettez nous des tickets et un 20/20 svp
            # On refait les vérifications de compte avec le nouveau pseudo
            verifier_et_ajouter_pseudo(joueur1.get_pseudo(),joueur1.get_mdp()) 
            # On récupère l'identifiant du compte
            id_compte = det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp())
            # On récupère le solde du compte
            joueur1.set_cagnotte(recup_donnees(id_compte))
            # On met à jour la dernière connexion du compte
            ajouter_connexion(id_compte)
        # Cas de joueur Mr Mhorrhyce quand le changement de pseudo a été effectué
        elif joueur1.get_pseudo() == 'Le meilleur':
            # On charge le fond d'écran spécifique de toute beauté
            self.fond = pygame.image.load('images/Fonds d\'ecran/Metteznous20sur20svp.jpg').convert()
        # Si le joueur est un démon (un arbre dégénéré)
        elif joueur1.get_pseudo().lower() == 'abel':
            # On affiche le fond d'écran spécifique de l'arbre dégénéré Abel
            self.fond = pygame.image.load('images/Fonds d\'ecran/FondAbel.png').convert()
        # Sinon
        else:
            # On charge le fond d'écran normal
            self.fond = pygame.image.load('images/Fonds d\'ecran/casino.jpg').convert()
        # On affiche le fond d'écran
        fenetre.blit(self.fond, (0, 0))
        # On fait progresser l'animation de la toute pitite piece à côté du solde du joueur (Elle est trop chou)
        coin.activer_rotation()
        # On affiche les boutons (affichage du pseudo et du solde du joueur)
        dessiner_bouton(fenetre, joueur1.get_pseudo(), bouton2.get_x(), bouton2.get_y(), bouton2.get_largeur(), bouton2.get_hauteur(), blanc, noir, 15)
        dessiner_bouton(fenetre, f"Solde : {int(joueur1.get_cagnotte())}", bouton3.get_x(), bouton3.get_y(), bouton3.get_largeur(), bouton3.get_hauteur(), blanc, noir, 15)
        # Si on clique sur le bouton pour accéder à la boutique
        if btn_boutique.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(True),ecran2.ecran.set_actif(False)
            clic.set_clic((0,0))
        # Si on clique sur le bouton pour lancer la roulette russe
        elif btn_roulette.collision(clic.get_clic()):
            click.play()
            joueur1.set_roulette_active(True)
            pileouface.set_actif(False)
            pistolet.rouletterusse(joueur1)
            joueur1.set_roulette_active(False)
            clic.set_clic((0,0))
        # Si on clique sur le bouton pour lancer la pile ou face
        elif btn_pile_ou_face.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            pileouface.set_actif(not pileouface.get_actif())
            pileouface.set_cote(None)
        # Si on clique sur le bouton pour lancer le blackjack de mort d'abel plus jamais je touche à ça vraiment c'est une horreur en plus la doc est inexistante c'est juste des commentaires et des commentaires vraiment je suis traumatisé aled
        elif btn_blackjack.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            ecran2.ecran.set_actif(False), ecran_black.ecran.set_actif(True)
        # Si on clique sur le bouton pour retourner à l'écran de connexion
        elif btn_retour.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            connexion.ecran.set_actif(True)
            ecran2.ecran.set_actif(False)
        # Si on ouvre l'inventaire
        elif btn_inventaire.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            ecran2.ecran.set_actif(False), inventaire.ecran.set_actif(True) # On définit l'inventaire comme ecran actif
        # Si on ouvre le classement
        elif btn_classement.collision(clic.get_clic()):   
            print("aled")
            ecran2.ecran.set_actif(False),classement.ecran.set_actif(True)  # On définit l'écran du classement comme ecran actif
            classement.actualiser_classement()  
            clic.set_clic((0,0))
        elif btn_babelrace.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            babelrace.actif(True)
            babelrace.lancer()
        elif pileouface.get_actif():
            # Pari sur le côté Face de la piece
            if btn_face.collision(clic.get_clic()):
                click.play()
                pileouface.set_choix('Face') 
                self.choix_fait = True
            # Pari sur le côté Pile de la piece
            elif btn_pile.collision(clic.get_clic()):
                click.play()
                pileouface.set_choix('Pile')
                self.choix_fait = True
            # Lancer l'animation de Pile ou Face quand le joueur a effectué son choix
            if self.choix_fait:
                pileouface.activer_animation()
                self.choix_fait = False
        # On lance l'animation du bouton du classement
        elif btn_classement.collision(pygame.mouse.get_pos()):
            self.anim = True
        else:
            btn_classement.draw(fenetre,pygame.mouse.get_pos())
        fenetre.blit(coin.get_image(),coin.get_pos())
        coin.update(0.04)
        fenetre.blit(pistolet.get_image(),pistolet.get_pos())
        pistolet.update_def(0.16,joueur1)  
        pistolet.update_vict(0.16,joueur1)  
        fenetre.blit(pileouface.get_image(),(170,140))
        # On joue l'animation du bouton du classement
        if self.anim:
            self.btn_classement_anim(0.3)
        if pileouface.get_actif():
            pileouface.update(0.20, joueur1)
        # Petit Easter egg
        if joueur1.get_pseudo() == '666' or joueur1.get_pseudo() == 'Satan':
            fenetre.blit(diable, (100, 2))
        # Affichage des boutons des jeux
        for btn in self.btns:
            btn.draw(fenetre,pygame.mouse.get_pos())
        # Affichage des boutons des choix du pile ou face
        if pileouface.get_actif():
            btn_pile.draw(fenetre,pygame.mouse.get_pos()),btn_face.draw(fenetre,pygame.mouse.get_pos())
        # Si le joueur est Mr Meaurisse 
        if joueur1.get_pseudo().lower() == 'Le meilleur' and not self.benji in joueur1.get_heros():
            # On ajoute le héros Benji à la liste des héros du joueur
            joueur1.ajouter_hero(self.benji)
    def btn_classement_anim(self,speed:float):
        '''
        Permet d'animer le bouton des héros. On dait progresser l'indice de l'image, si on arrive à la fin on le remet à 0.
        Paramètres :
            - speed (float) : Vitesse de l'animation
        '''
        self.frame += speed
        # Si on arrive au bout de l'animation on recommence
        if self.frame >= len(self.btn_classement)-1:
            self.frame = 0
            self.anim = False
        fenetre.blit(pygame.image.load(self.btn_classement[int(self.frame)]).convert_alpha(), (188, -5))

class EcranMort:
    def __init__(self):
        self.ecran = Ecran()
        self.fond =  pygame.image.load('images/Fonds d\'ecran/enfer2.png').convert()
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
        # On affiche le fond
        fenetre.blit(paradis, (0, 0))
        # Nouvelle musique propre au paradis
        if not pygame.mixer.music.get_busy():
            # On enlève l'ancienne musique
            pygame.mixer.music.unload()
            # On met la nouvelle et on la joue
            pygame.mixer.music.load(musique_victoire)
            pygame.mixer.music.play(-1)
        # On affiche le bouton de retour
        btn_retour.draw(fenetre,pygame.mouse.get_pos())
        # Si on clique sur le bouton retour
        if btn_retour.collision(clic.get_clic()):
            # On enlève la musique de victoire et on remet l'ancienne
            clic.set_clic((0,0))
            pygame.mixer.music.unload()
            connexion.choisir_musique()
            # On remet l'écran principal en tant qu'écran actif
            ecran_victoire.ecran.set_actif(False)
            ecran2.ecran.set_actif(True)

class EcranBlack:
    def __init__(self):
        self.ecran = Ecran()
    def affiche(self,blackjack):
        blackjack.set_actif(True)
        blackjack.main()

class EcranBoutique:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
        self.btn_heros = [f'images/Btn_heros/_a_frm{i},70.png' for i in range(13)]
        self.btn = pygame.image.load(self.btn_heros[0]).convert_alpha()
        self.frame = 0

    def affiche(self):
        '''
        Permet d'afficher l'écran de la boutique, ainsi que gérer les interactions avec les boutons.
        '''
        # Affichage du fond et des boutons
        fenetre.blit(self.fond, (0, 0))
        btn_fleche.draw(fenetre,pygame.mouse.get_pos())
        btn_alcool.draw(fenetre,pygame.mouse.get_pos())
        # Bouton retour
        if btn_fleche.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(False),ecran2.ecran.set_actif(True)
            clic.set_clic((0,0))
        # Bouton pour la page d'achat des héros
        elif btn_hero.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(False),hero.ecran.set_actif(True)
            clic.set_clic((0,0))
        # Bouton pour la page d'achat des alcools
        elif btn_alcool.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(False),alcool.ecran.set_actif(True)
            clic.set_clic((0,0))
        # Animation du bouton des héros
        elif btn_hero.collision(pygame.mouse.get_pos()):
            self.anim(0.1)
        else:
            btn_hero.draw(fenetre,pygame.mouse.get_pos())
            self.frame = 0

    def anim(self,speed:float):
        '''
        Permet d'animer le bouton des héros'''
        self.frame += speed
        # Si on arrive au bout de l'animation on recommence
        if self.frame >= len(self.btn_heros)-1:
            self.frame = 0
        fenetre.blit(pygame.image.load(self.btn_heros[int(self.frame)]).convert_alpha(), (215, 130))

class EcranClassement:
    def __init__(self):
        self.ecran = Ecran()  # Assure-toi que cette classe est définie ailleurs dans ton code
        self.fond = pygame.image.load('images/Fonds d\'ecran/fond_classement5.png').convert_alpha()
        self.police = pygame.font.Font('babelcasino.ttf', 15)
        self.frame = 0
        self.sprites = [pygame.image.load(f'images/Fonds d\'ecran/Demon_classement/_a_{i},80.png').convert_alpha() for i in range(14)]
        self.gens = []
        self.cartouche0 = Button(cartouche_classement2, cartouche_classement, 10, 75)
        self.cartouche1 = Button(cartouche_classement2, cartouche_classement, 10, 115)
        self.cartouche2 = Button(cartouche_classement2, cartouche_classement, 10, 155)
        self.cartouche3 = Button(cartouche_classement2, cartouche_classement, 10, 195)
        self.cartouche4 = Button(cartouche_classement2, cartouche_classement, 10, 235)
        self.cartouches = [self.cartouche0, self.cartouche1, self.cartouche2, self.cartouche3, self.cartouche4]

    def actualiser_classement(self):
        # Mise à jour de la liste des joueurs avec leurs informations
        self.gens = [(ordre_classement()[0][0], int(ordre_classement()[0][1])),  # 1er joueur et son solde
                     (ordre_classement()[1][0], int(ordre_classement()[1][1])),  # 2ème joueur et son solde
                     (ordre_classement()[2][0], int(ordre_classement()[2][1])),  # 3ème joueur et son solde
                     (ordre_classement()[3][0], int(ordre_classement()[3][1])),  # 4ème joueur et son solde
                     (ordre_classement()[4][0], int(ordre_classement()[4][1]))]  # 5ème joueur et son solde

    def affiche(self):
        '''
        Permet d'afficher l'écran du classement, ainsi que gérer les interactions avec les boutons.
        '''
        # Affichage du fond et des boutons
        fenetre.blit(self.fond,(0,0))  # Remplir l'écran avec une couleur de fond
        #fenetre.fill((0,0,0))
        btn_fleche.draw(fenetre, pygame.mouse.get_pos())  # Affichage du bouton 
        # Bouton retour
        if btn_fleche.collision(clic.get_clic()):
            print("aled")
            classement.ecran.set_actif(False)  # Passage à l'écran de la boutique
            ecran2.ecran.set_actif(True)  # Passage à un autre écran
            clic.set_clic((0, 0))  # Réinitialisation du clic

        # Affichage des informations du classement
        x = 30
        y = 81  # Position de départ pour l'affichage
        # Affichage des cartouches
        for cartouche in self.cartouches:
            cartouche.draw(fenetre, pygame.mouse.get_pos())
        # On affiche le pseudo et le solde de chaque joueur du top 5
        for i, (nom_joueur, solde) in enumerate(self.gens):
            # Affichage du classement et du solde de chaque joueur
            fenetre.blit(self.police.render(f"{i+1}. {nom_joueur} - {solde} Babel Coins", True, (255, 255, 255)), (x, y))
            y += 40  # Décalage pour afficher les informations du joueur suivant
        # Animation du démon
        self.anim(0.1)

    def anim(self,speed:float):
        '''
        Permet d'animer le démon du classement'''
        # On fait progresser l'animation
        self.frame += speed
        # Si on arrive au bout de l'animation on recommence
        if self.frame >= len(self.sprites)-1:
            self.frame = 0
        # On affiche l'image actuelle
        fenetre.blit(self.sprites[int(self.frame)].convert_alpha(), (100, 230))

class EcranAlcool:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
        self.vodka = False
        self.biere = False
        self.whisky = False
        self.mojito = False
        self.btns = [btn_whisky, btn_biere, btn_vodka, btn_mojito, btn_fleche]

    def affiche(self):
        '''
        Permet d'afficher l'écran des alcools, ainsi que gérer les interactions avec les boutons pour l'achat de ceux-ci.'''
        fenetre.blit(self.fond, (0, 0))
        # Quand on survole un bouton, on affiche les effets de l'alcool
        if btn_whisky.collision(pygame.mouse.get_pos()):
            self.whisky = True
        elif btn_biere.collision(pygame.mouse.get_pos()):
            self.biere = True
        elif btn_vodka.collision(pygame.mouse.get_pos()):
            self.vodka = True
        elif btn_mojito.collision(pygame.mouse.get_pos()):
            self.mojito = True
        # Sinon, on désactive tous les effets
        else:
            self.vodka,self.biere,self.whisky,self.mojito = False,False,False,False
        # Bouton retour
        if btn_fleche.collision(clic.get_clic()):
            clic.set_clic((0,0))
            alcool.ecran.set_actif(False),ecran_boutique.ecran.set_actif(True)
        # Si on clique sur un bouton d'achat de la vodka, on lance le gif de Poutine
        elif btn_vodka.collision(clic.get_clic()):
            alcool.ecran.set_actif(False),vodka.ecran.set_actif(True)
            pygame.mixer.music.unload()
        # Si on clique sur un alcool, on lance l'achat
        elif btn_biere.collision(clic.get_clic()):
            achat('Biere')
        elif btn_whisky.collision(clic.get_clic()):
            achat('Whisky')
        elif btn_mojito.collision(clic.get_clic()):
            achat('Mojito')
        for btn in self.btns:
            btn.draw(fenetre,pygame.mouse.get_pos())
        self.affiche_effets()

    def affiche_effets(self):
        '''Permet d'afficher les effets des alcools lors du survol de la souris.'''
        if self.vodka:
            fenetre.blit(effet_vodka, (pygame.mouse.get_pos()[0]+40, pygame.mouse.get_pos()[1]-30))
        elif self.biere:
            fenetre.blit(effet_biere, (pygame.mouse.get_pos()[0]+40, pygame.mouse.get_pos()[1]-30))
        elif self.whisky:
            fenetre.blit(effet_whisky, (pygame.mouse.get_pos()[0]-180, pygame.mouse.get_pos()[1]-30))
        elif self.mojito:
            fenetre.blit(effet_mojito, (pygame.mouse.get_pos()[0]-180, pygame.mouse.get_pos()[1]-30))

class EcranSelection:
    def __init__(self, caracteristiques_hero, liste:list, hero:tuple, y:int, x:int = 50):
        self.police = pygame.font.Font('babelcasino.ttf', 8)
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/arene.png').convert_alpha()
        self.anim = liste
        self.frame = 0
        self.valider = self.police.render(("Val ider"), True, noir)
        self.hero = hero
        self.prix = self.police.render((str(self.hero[1])), True, noir)
        self.y = y
        self.x = x
        self.infos = False
        self.caracteristiques = caracteristiques_hero
    def getinfos(self):
        return self.infos
    def setinfos(self,actif:bool):
        self.infos = actif
    def affiche(self,speed:float):
        '''Permet d'afficher l'écran de selection pour chaque heros, avec :
            - Les infos et caractéristiques du personnages
            - Un bouton pour selectionner/acheter le personnage
            - Un bouton pour afficher les informations du personnage
            - Un bouton pour revenir en arrière
        '''
        fenetre.blit(self.fond, (0, 0))
        # On joue l'animation de chaque héros pendant l'écran de selection
        fenetre.blit(pygame.image.load(self.anim[int(self.frame)]).convert_alpha(), (self.x, self.y))
        self.frame += speed
        if self.frame >= len(self.anim)-1:
            self.frame = 0
        # On affiche les caractéristiques du héros si le joueur a cliqué sur le bouton
        if self.infos:
            fenetre.blit(self.caracteristiques, (30, 50))
        # Si le joueur possède le héros on écrit 'Valider' sur le bouton
        elif self.hero[0] in joueur1.get_heros():
            btn_select.draw(fenetre,pygame.mouse.get_pos())
            fenetre.blit(self.valider, (185, 340))
        # Sinon on écrit le prix du héros sur le bouton
        else:
            btn_select.draw(fenetre,pygame.mouse.get_pos())
            fenetre.blit(self.prix, (185, 340))
        # On affiche les boutons
        btn_fleche.draw(fenetre,pygame.mouse.get_pos())
        btn_info.draw(fenetre,pygame.mouse.get_pos())
    def get_heros(self):
        return self.hero
        


class EcranVodka:
    def __init__(self):
        self.ecran = Ecran()
        self.frames = [f'Vodkaa/_a_frm{i},70.png' for i in range(140)]
        self.frame = 'Vodkaa/_a_frm0,70.png'
        self.num_frame = 0
        self.musique_de_fond = vodkaaa
    def affiche(self,speed:float):
        '''Permet d'afficher l'écran de Poutine.'''
        self.num_frame += speed
        self.frame = self.frames[int(self.num_frame)]
        # Si toutes les images ont été jouées :
        if int(self.num_frame) == len(self.frames)-1:
            # On remet tout à 0
            self.num_frame = 0
        fenetre.blit(pygame.image.load(self.frame),(-80,0))
        # On lance la musique associée au gif
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.musique_de_fond)
            pygame.mixer.music.set_volume(0.3)  # Volume pour la musique de fond générale
            pygame.mixer.music.play(-1)

class EcranRR:
    def __init__(self):
        self.ecran = Ecran()
        self.frames = [f'RR/rickroll ({i}).png' for i in range(1,148)]
        self.frame = 'RR/rickroll (1).png'
        self.num_frame = 0
    def affiche(self,speed:float):
        '''Permet d'afficher l'écran de rickroll.
        Paramètres :
            - speed (float) : la vitesse de l'animation.'''
        self.num_frame += speed
        self.frame = self.frames[int(self.num_frame)]
        # Si toutes les images ont été jouées :
        if int(self.num_frame) == len(self.frames)-1:
            # On remet tout à 0
            self.num_frame = 0
        fenetre.blit(pygame.image.load(self.frame),(0,0))


class EcranNiveaux:
    def __init__(self):
        self.ecran = Ecran()
    def affiche(self):
        # Si toutes les images ont été jouées :
        fenetre.blit(voiture.get_sprites()[voiture.get_frame()],(voiture.get_x(),voiture.get_y()))

class EcranChargement:
    def __init__(self):
        self.ecran = Ecran(True)
        self.frames = [f'images/Fonds d\'ecran/Chargement/frm ({i}).png' for i in range(1,116)]
        self.frame = 'images/Fonds d\'ecran/Chargement/frm (2).png'
        self.num_frame = 0
        self.stop = True
    def affiche(self,speed:float):
        '''Permet d'afficher l'animation l'écran de chargement.'''
        if self.num_frame <= 73 or not self.stop:
            self.num_frame += speed
        if clic.get_clic() != (0,0) and self.num_frame >= 56:
            self.stop = False
        # Si toutes les images ont été jouées :
        if int(self.num_frame) == len(self.frames)-1:
            # On remet tout à 0
            self.num_frame = 0
            connexion.ecran.set_actif(True),self.ecran.set_actif(False)
        self.frame = self.frames[int(self.num_frame)]
        fenetre.blit(pygame.image.load(self.frame),(0,0))

class EcranInventaire:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load("images/Fonds d'ecran/inventaire.png").convert()
        self.items = [item_biere, item_whisky, item_mojito]
        self.alcools = {item_biere : 'Biere', item_whisky : 'Whisky', item_mojito : 'Mojito'}
        self.alcools_effets = {'Biere' : biere, 'Whisky' : whisky, 'Mojito' : mojito}
        self.police = pygame.font.Font('babelcasino.ttf', 15)
        self.police2 = pygame.font.Font('babelcasino.ttf', 12)
        self.selectione = None
    def affiche(self):
        '''Permet d'afficher l'écran de l'inventaire du joueur.
        Pour chaque alcool dispo, on affiche le bouton correspondant avec la qté en dessous.
        Si le bouton est cliqué, l'alcool est sélectionné et peut être utilisé.
        '''
        # On affiche les boutons
        fenetre.blit(self.fond,(0,0))
        btn_valider.draw(fenetre,pygame.mouse.get_pos())
        btn_flecheretour.draw(fenetre,pygame.mouse.get_pos())
        fenetre.blit(banniere,(136,285))
        # Pour chaque item dispo
        for item in self.items:
            item.draw(fenetre,pygame.mouse.get_pos())
            # On affiche la quantité de l'objet présente dans l'inventaire du joueur
            if self.alcools[item] in joueur1.get_inventaire().keys():
                fenetre.blit(self.police.render(('x ' + str(joueur1.get_inventaire()[self.alcools[item]])), True, noir),(item.get_pos()[0]+15, item.get_pos()[1]+60))
            else:
                fenetre.blit(self.police.render(('x 0'), True, noir),(item.get_pos()[0]+15, item.get_pos()[1]+60))
            # Si on clique sur un item
            if item.collision(clic.get_clic()):
                # On affiche le croix de sélection à l'emplacement du l'item
                click.play()
                self.selectione = self.alcools[item]
                curseur_selection.set_pos(item.get_pos())
                curseur_selection.set_actif(True)
                clic.set_clic((0,0))
            elif btn_valider.collision(clic.get_clic()):
                # Si l'item selectionné est présent dans l'inventaire du joueur
                if self.selectione in joueur1.get_inventaire().keys() and joueur1.get_inventaire()[self.selectione] > 0:
                    # On l'enlève de l'inventaire et de la bdd, puis on active l'effet
                    joueur1.get_inventaire()[self.selectione] -= 1
                    ajouter_objet_inventaire(-1, det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp()), self.selectione)
                    self.alcools_effets[self.selectione].boire(joueur1)
                curseur_selection.set_actif(False)
                clic.set_clic((0,0))
            # Si on clique ailleurs, on desselectionne les items
            elif clic.get_clic() != (0,0):
                curseur_selection.set_actif(False)
                self.selectione = None
            # On affiche le nom de l'alcool selectionné
            if self.selectione:
                texte = self.police2.render((self.selectione), True, noir)
                fenetre.blit(texte,(136 + (128 - texte.get_width()) // 2, 299))
        # Bouton de retour
        if btn_flecheretour.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            ecran2.ecran.set_actif(True), inventaire.ecran.set_actif(False)
        # On joue l'animation de la croix de selection
        if curseur_selection.get_actif():
            curseur_selection.update(0.2)



ecran0 = EcranChargement()
inventaire = EcranInventaire()
connexion = Ecran1()
ecran2 = Ecran2()
classement = EcranClassement()
ecran_boutique = EcranBoutique()
vodka = EcranVodka()
ecran_mort = EcranMort()
ecran_victoire = EcranVictoire()
ecran_black = EcranBlack()
rr = EcranRR()
alcool = EcranAlcool()
niveaux = EcranNiveaux()
klaxon = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Maehv.png').convert_alpha(),[f'images/Jeu de combat/Klaxon/Droite/Inaction/_a_{i},80.png' for i in range(18)],('Klaxon',35000),90,112)
cryoblade = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Maehv.png').convert_alpha(),[f'images/Jeu de combat/Cryoblade/Droite/Inaction/_a_{i},80.png' for i in range(16)],('Cryoblade',35000),80,105)
reeju = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Maehv.png').convert_alpha(),[f'images/Jeu de combat/Reeju/Droite/Inaction/_a_{i},100.png' for i in range(14)],('Reeju',40000),25,50)
windcliffe = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Maehv.png').convert_alpha(),[f'images/Jeu de combat/Windcliffe/Droite/Inaction/_a_{i},80.png' for i in range(9)],('Windcliffe',70000),55,75)
maehv = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Maehv.png').convert_alpha(),[f'images/Jeu de combat/Maehv/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Maehv',350000),5)
zendo = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Zendo.png').convert_alpha(),[f'images/Jeu de combat/Zendo/Droite/Inaction/_a_frm{i},60.png' for i in range(14)],('Zendo',200000),5)
zukong = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Zukong/Droite/Inaction/_a_frm{i},80.png' for i in range(14)],('Zukong',45000),56,75)
nighthero = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Hero/Block/Block ({i}).png' for i in range(1,19)],('Night Hero',0),100,100)
hsuku = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Hsuku.png').convert_alpha(),[f'images/Jeu de combat/Hsuku/Droite/Inaction/_a_{i},80.png' for i in range(28)],('Hsuku',300000),10)
sanguinar = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Sanguinar/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Sanguinar',400000),10)
whistler = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Whistler.png').convert_alpha(),[f'images/Jeu de combat/Whistler/Droite/Inaction/_a_{i},100.png' for i in range(18)],('Whistler',400000),80,95)
tethermancer = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Whistler.png').convert_alpha(),[f'images/Jeu de combat/Tethermancer/Droite/Inaction/_a_{i},100.png' for i in range(17)],('Tethermancer',250000),20)
aether = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Aether.png').convert_alpha(),[f'images/Jeu de combat/Aether/Droite/Inaction/_a_{i},100.png' for i in range(12)],('Aether',175000),97,93)
pureblade = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Pureblade.png').convert_alpha(),[f'images/Jeu de combat/Pureblade/Droite/Inaction/_a_frm{i},80.png' for i in range(10)],('Pureblade',275000),10)
twilight = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Twilight.png').convert_alpha(),[f'images/Jeu de combat/Twilight/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Twilight',180000),20)
suzumebachi = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Suzumebachi.png').convert_alpha(),[f'images/Jeu de combat/Suzumebachi/Droite/Inaction/_a_{i},80.png' for i in range(32)],('Suzumebachi',150000),20)
dusk = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Suzumebachi.png').convert_alpha(),[f'images/Jeu de combat/Dusk/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Dusk',200000),20)
yggdra = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Suzumebachi.png').convert_alpha(),[f'images/Jeu de combat/Yggdra/Droite/Inaction/_a_{i},80.png' for i in range(7)],('Yggdra',450000),70,70)


class EcranHeros:
    def __init__(self,btns:dict):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
        self.btns = btns
    def affiche(self):
        '''Permet d'afficher l'écran de la boutique des héros, et de passer de chaque bouton de hero et l'écran du heros corrsepondant'''
        fenetre.blit(self.fond, (0, 0))
        btn_suivant.draw(fenetre,pygame.mouse.get_pos())    # Pour passer à l'onglet 2
        for btn,ecran in self.btns.items():    # Pour chaque bouton de héros
            btn.draw(fenetre,pygame.mouse.get_pos())    # On affiche le bouton
            if btn.collision(clic.get_clic()):  # Si on clique dessus
                clic.set_clic((0,0))    # On reset le clic
                ecran.ecran.set_actif(True),self.ecran.set_actif(False)   # On affiche l'écran du héros

hero = EcranHeros({
            btn_fleche : ecran_boutique,
            btn_nighthero : nighthero,
            btn_klaxon : klaxon,
            btn_reeju : reeju,
            btn_cryoblade :cryoblade,
            btn_windcliffe : windcliffe,
            btn_zukong : zukong,
            btn_zendo : zendo,
            btn_maehv : maehv,
            btn_hsuku : hsuku,
            btn_sanguinar : sanguinar,
            btn_whistler : whistler,
            btn_tethermancer : tethermancer})

hero2 = EcranHeros({btn_fleche : ecran_boutique,
                    btn_aether : aether,
                    btn_twilight : twilight,
                    btn_pureblade : pureblade,
                    btn_suzumebachi : suzumebachi,
                    btn_dusk : dusk,
                    btn_yggdra : yggdra
                    })

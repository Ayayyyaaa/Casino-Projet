import pygame
from fonctions import dessiner_zone_texte, dessiner_bouton
from objets_et_variables import *
from img import *
from Roulette_Russe import pistolet
from PileouFace import pileouface
from sons import *
from SQL import *
from fonctions import achat
from Jeu_platforme import *

afficher_ecran_chargement(chargement[6])
print("Chargement de Ecrans.py")

class Ecran:
    def __init__(self, actif:bool = False):
        self.actif = actif
    def get_actif(self):
        return self.actif
    def set_actif(self, actif):
        self.actif = actif

class Ecran1:
    def __init__(self):
        self.ecran = Ecran()
        self.ancien_pseudo = joueur1.get_pseudo()
        self.fin_combat = False
    def affiche(self):
        '''Permet d'afficher l'écran de connexion et de passer à l'écran principal.
        '''
        if self.ecran.get_actif():          #Si l'écran est actif
            fenetre.blit(fond, (0, 0))          #On dessine tous les éléments
            btn_entrer.draw(fenetre,pygame.mouse.get_pos())
            if btn_entrer.collision(clic.get_clic()):           #Si on clique sur le bouton entrer
                click.play()
                if joueur1.get_pseudo() != '':          #Si le joueur a entré ses identifiants
                    connexion.ecran.set_actif(False)            #On passe à l'écran suivant, en mettant a jour la musique
                    ecran2.ecran.set_actif(True)
                    clic.set_clic((0,0))
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
        if joueur1.get_pseudo().lower() == 'fredou':
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                pygame.mixer.music.unload()
                pygame.mixer.music.load(son_champignon)
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True
        elif joueur1.get_pseudo().lower() in ['rick','rickroll','rick roll', 'rickastley', 'rick astley']:
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                rr.ecran.set_actif(True),ecran2.ecran.set_actif(False)
                pygame.mixer.music.unload()
                pygame.mixer.music.load(rickr)
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True
        else:
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo() and joueur1.get_pseudo() not in ['rick','rickroll','rick roll', 'rickastley', 'rick astley']:
                pygame.mixer.music.unload()
                pygame.mixer.music.load(musique_de_fond)
                pygame.mixer.music.set_volume(0.3)  # Volume pour la musique de fond générale
                pygame.mixer.music.play(-1)
                self.ancien_pseudo = joueur1.get_pseudo()
                self.fin_combat = True


class Ecran2:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/casino.jpg').convert()
        self.musique = False
        self.btns = [btn_boutique, btn_retour, btn_roulette, btn_pile_ou_face, btn_machine_a_sous, btn_blackjack, btn_jeu_combat, btn_inventaire]
        self.choix_fait = False
    def set_musique(self):
        self.musique = False
    def affiche(self):
        '''
        Permet d'afficher l'écran principal et de gérer l'animation des boutons et mettre à jour les animations des jeux.
        '''
        if joueur1.get_pseudo().lower() == 'fredou':
            self.fond = pygame.image.load('images/Fonds d\'ecran/coeurfredou.png').convert()
        elif joueur1.get_pseudo().lower() == 'mr.maurice' or joueur1.get_pseudo().lower() == 'mr maurice' or joueur1.get_pseudo().lower() == 'maurice':
            joueur1.set_pseudo('Le meilleur')  #Mettez nous des tickets et un 20/20 svp
            verifier_et_ajouter_pseudo(joueur1.get_pseudo(),joueur1.get_mdp()) 
            id_compte = det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp())
            joueur1.set_cagnotte(recup_donnees(id_compte))
            ajouter_connexion(id_compte)
        elif joueur1.get_pseudo() == 'Le meilleur':
            self.fond = pygame.image.load('images/Fonds d\'ecran/Metteznous20sur20svp.jpg').convert()
        elif joueur1.get_pseudo().lower() == 'abel':
            self.fond = pygame.image.load('images/Fonds d\'ecran/FondAbel.png').convert()
        else:
            self.fond = pygame.image.load('images/Fonds d\'ecran/casino.jpg').convert()
        fenetre.blit(self.fond, (0, 0))
        coin.activer_rotation()
        dessiner_bouton(fenetre, joueur1.get_pseudo(), bouton2.get_x(), bouton2.get_y(), bouton2.get_largeur(), bouton2.get_hauteur(), blanc, noir, 20)
        dessiner_bouton(fenetre, f"Solde : {int(joueur1.get_cagnotte())}", bouton3.get_x(), bouton3.get_y(), bouton3.get_largeur(), bouton3.get_hauteur(), blanc, noir, 25)
        if btn_boutique.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(True),ecran2.ecran.set_actif(False)
            clic.set_clic((0,0))
        elif btn_roulette.collision(clic.get_clic()):
            click.play()
            joueur1.set_roulette_active(True)
            pileouface.set_actif(False)
            pistolet.rouletterusse(joueur1)
            joueur1.set_roulette_active(False)
            clic.set_clic((0,0))
        elif btn_pile_ou_face.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            pileouface.set_actif(not pileouface.get_actif())
            pileouface.set_cote(None)
        elif btn_blackjack.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            ecran2.ecran.set_actif(False), ecran_black.ecran.set_actif(True)
        elif btn_retour.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            connexion.ecran.set_actif(True)
            ecran2.ecran.set_actif(False)
        elif btn_inventaire.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            ecran2.ecran.set_actif(False), inventaire.ecran.set_actif(True)
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

        fenetre.blit(coin.get_image(),coin.get_pos())
        coin.update(0.04)
        fenetre.blit(pistolet.get_image(),pistolet.get_pos())
        pistolet.update_def(0.16,joueur1)  
        pistolet.update_vict(0.16,joueur1)  
        fenetre.blit(pileouface.get_image(),(170,140))
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
        if joueur1.get_pseudo().lower() == 'Le meilleur' and not self.benji in joueur1.get_heros():
            joueur1.ajouter_hero(self.benji)

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
        fenetre.blit(paradis, (0, 0))
       
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unload()
            pygame.mixer.music.load(musique_victoire)
            pygame.mixer.music.play(-1)

        btn_retour.draw(fenetre,pygame.mouse.get_pos())
        if btn_retour.collision(clic.get_clic()):
            clic.set_clic((0,0))
            pygame.mixer.music.unload()
            connexion.choisir_musique()
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
        fenetre.blit(self.fond, (0, 0))
        btn_fleche.draw(fenetre,pygame.mouse.get_pos())
        btn_alcool.draw(fenetre,pygame.mouse.get_pos())
        if btn_fleche.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(False),ecran2.ecran.set_actif(True)
            clic.set_clic((0,0))
        elif btn_hero.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(False),hero.ecran.set_actif(True)
            clic.set_clic((0,0))
        elif btn_alcool.collision(clic.get_clic()):
            ecran_boutique.ecran.set_actif(False),alcool.ecran.set_actif(True)
            clic.set_clic((0,0))
        elif btn_hero.collision(pygame.mouse.get_pos()):
            self.anim(0.1)
        else:
            btn_hero.draw(fenetre,pygame.mouse.get_pos())
            self.frame = 0

    def anim(self,speed):
        self.frame += speed
        if self.frame >= len(self.btn_heros)-1:
            self.frame = 0
        fenetre.blit(pygame.image.load(self.btn_heros[int(self.frame)]).convert_alpha(), (215, 130))


class EcranAlcool:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
        self.vodka = False
        self.biere = False
        self.whisky = False
        self.btns = [btn_whisky, btn_biere, btn_vodka, btn_fleche]

    def affiche(self):
        '''
        Permet d'afficher l'écran des alcools, ainsi que gérer les interactions avec les boutons pour l'achat de ceux-ci.'''
        fenetre.blit(self.fond, (0, 0))
        if btn_whisky.collision(pygame.mouse.get_pos()):
            self.whisky = True
        elif btn_biere.collision(pygame.mouse.get_pos()):
            self.biere = True
        elif btn_vodka.collision(pygame.mouse.get_pos()):
            self.vodka = True
        else:
            self.vodka,self.biere,self.whisky = False,False,False
        if btn_fleche.collision(clic.get_clic()):
            clic.set_clic((0,0))
            alcool.ecran.set_actif(False),ecran_boutique.ecran.set_actif(True)
        elif btn_vodka.collision(clic.get_clic()):
            alcool.ecran.set_actif(False),vodka.ecran.set_actif(True)
            pygame.mixer.music.unload()
        elif btn_biere.collision(clic.get_clic()):
            achat('Biere')
        elif btn_whisky.collision(clic.get_clic()):
            achat('Whisky')
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

class EcranSelection:
    def __init__(self, caracteristiques_hero, liste, hero, y, x = 50):
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
    def setinfos(self,actif):
        self.infos = actif
    def affiche(self,speed):
        '''Permet d'afficher l'écran de selection pour chaque heros.'''
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(pygame.image.load(self.anim[int(self.frame)]).convert_alpha(), (self.x, self.y))
        self.frame += speed
        if self.frame >= len(self.anim)-1:
            self.frame = 0
        if self.infos:
            fenetre.blit(self.caracteristiques, (30, 50))
        elif self.hero[0] in joueur1.get_heros():
            btn_select.draw(fenetre,pygame.mouse.get_pos())
            fenetre.blit(self.valider, (185, 340))
        else:
            btn_select.draw(fenetre,pygame.mouse.get_pos())
            fenetre.blit(self.prix, (185, 340))
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
    def affiche(self,speed):
        '''Permet d'afficher l'écran de Poutine.'''
        self.num_frame += speed
        self.frame = self.frames[int(self.num_frame)]
        # Si toutes les images ont été jouées :
        if int(self.num_frame) == len(self.frames)-1:
            # On remet tout à 0
            self.num_frame = 0
        fenetre.blit(pygame.image.load(self.frame),(-80,0))
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
    def affiche(self,speed):
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
        self.items = [item_biere, item_whisky]
        self.alcools = {item_biere : 'Biere', item_whisky : 'Whisky'}
        self.alcools_effets = {'Biere' : biere, 'Whisky' : whisky}
        self.police = pygame.font.Font('babelcasino.ttf', 15)
        self.police2 = pygame.font.Font('babelcasino.ttf', 12)
        self.selectione = None
    def affiche(self):
        '''Permet d'afficher l'écran de l'inventaire du joueur.
        Pour chaque alcool dispo, on affiche le bouton correspondant avec la qté en dessous.
        Si le bouton est cliqué, l'alcool est sélectionné et peut être utilisé.
        '''
        fenetre.blit(self.fond,(0,0))
        btn_valider.draw(fenetre,pygame.mouse.get_pos())
        btn_flecheretour.draw(fenetre,pygame.mouse.get_pos())
        fenetre.blit(banniere,(136,285))
        for item in self.items:
            item.draw(fenetre,pygame.mouse.get_pos())
            if self.alcools[item] in joueur1.get_inventaire().keys():
                fenetre.blit(self.police.render(('x ' + str(joueur1.get_inventaire()[self.alcools[item]])), True, noir),(item.get_pos()[0]+15, item.get_pos()[1]+60))
            else:
                fenetre.blit(self.police.render(('x 0'), True, noir),(item.get_pos()[0]+15, item.get_pos()[1]+60))
            if item.collision(clic.get_clic()):
                self.selectione = self.alcools[item]
                curseur_selection.set_pos(item.get_pos())
                curseur_selection.set_actif(True)
                clic.set_clic((0,0))
            elif btn_valider.collision(clic.get_clic()):
                if self.selectione in joueur1.get_inventaire().keys() and joueur1.get_inventaire()[self.selectione] > 0:
                    joueur1.get_inventaire()[self.selectione] -= 1
                    ajouter_objet_inventaire(-1, det_id_compte(joueur1.get_pseudo(),joueur1.get_mdp()), self.selectione)
                    self.alcools_effets[self.selectione].boire(joueur1)
                    print(self.selectione, self.alcools_effets[self.selectione].get_nom(),joueur1.get_probas(),joueur1.get_gains())
                curseur_selection.set_actif(False)
                clic.set_clic((0,0))
            elif clic.get_clic() != (0,0):
                curseur_selection.set_actif(False)
                self.selectione = None
            if self.selectione:
                texte = self.police2.render((self.selectione), True, noir)
                fenetre.blit(texte,(136 + (128 - texte.get_width()) // 2, 299))
        if btn_flecheretour.collision(clic.get_clic()):
            click.play()
            clic.set_clic((0,0))
            ecran2.ecran.set_actif(True), inventaire.ecran.set_actif(False)
        if curseur_selection.get_actif():
            curseur_selection.update(0.2)



ecran0 = EcranChargement()
inventaire = EcranInventaire()
connexion = Ecran1()
ecran2 = Ecran2()
ecran_boutique = EcranBoutique()
vodka = EcranVodka()
ecran_mort = EcranMort()
ecran_victoire = EcranVictoire()
ecran_black = EcranBlack()
rr = EcranRR()
alcool = EcranAlcool()
niveaux = EcranNiveaux()
assassin = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(), [f'images/Jeu de combat/Assassin/Droite/Attaque1/_a_frm{i},100.png' for i in range(10)] + [f'images/Jeu de combat/Assassin/Droite/Attaque2/_a_frm{i},100.png' for i in range(11,18)] + [f'images/Jeu de combat/Assassin/Droite/Marche/_a_frm{i},100.png' for i in range(8)] + [f'images/Jeu de combat/Assassin/Droite/Course/_a_frm{i},70.png' for i in range(8)] + [f'images/Jeu de combat/Assassin/Droite/Saut/_a_frm{i},100.png' for i in range(2,14)] + [f'images/Jeu de combat/Assassin/Mort/_a_frm{i},100.png' for i in range(16)],('Assassin',60000), 50)
maehv = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Maehv.png').convert_alpha(),[f'images/Jeu de combat/Maehv/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Maehv',350000),5)
zendo = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Zendo.png').convert_alpha(),[f'images/Jeu de combat/Zendo/Droite/Inaction/_a_frm{i},60.png' for i in range(14)],('Zendo',200000),5)
zukong = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Zukong/Droite/Inaction/_a_frm{i},80.png' for i in range(14)],('Zukong',45000),56,75)
nighthero = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Hero/Block/Block ({i}).png' for i in range(1,19)],('Night Hero',0),100,100)
spirithero = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Spirit_Hero/Inaction/_a_frm{i},100.png' for i in range(10)],('Spirit Hero',45000),50)
spiritwarior = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/SpiritWarrior.png').convert_alpha(),[f'images/Jeu de combat/Spirit_Warrior/Inaction/_a_frm{i},100.png' for i in range(8)],('Spirit Warior',30000),80,65)
lancier = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Lancier/Inaction/_a_frm{i},100.png' for i in range(8)],('Lancier',45000),70)
hsuku = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Hsuku.png').convert_alpha(),[f'images/Jeu de combat/Hsuku/Droite/Inaction/_a_{i},80.png' for i in range(28)],('Hsuku',300000),10)
sanguinar = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Sanguinar/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Sanguinar',400000),10)
whistler = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Whistler.png').convert_alpha(),[f'images/Jeu de combat/Whistler/Droite/Inaction/_a_{i},100.png' for i in range(18)],('Whistler',400000),80,95)
tethermancer = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Whistler.png').convert_alpha(),[f'images/Jeu de combat/Tethermancer/Droite/Inaction/_a_{i},100.png' for i in range(17)],('Tethermancer',250000),20)
aether = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Aether.png').convert_alpha(),[f'images/Jeu de combat/Aether/Droite/Inaction/_a_{i},100.png' for i in range(12)],('Aether',175000),97,93)
pureblade = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Pureblade.png').convert_alpha(),[f'images/Jeu de combat/Pureblade/Droite/Inaction/_a_frm{i},80.png' for i in range(10)],('Pureblade',275000),10)
twilight = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Twilight.png').convert_alpha(),[f'images/Jeu de combat/Twilight/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Twilight',180000),20)
suzumebachi = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Suzumebachi.png').convert_alpha(),[f'images/Jeu de combat/Suzumebachi/Droite/Inaction/_a_{i},80.png' for i in range(32)],('Suzumebachi',180000),20)
dusk = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Suzumebachi.png').convert_alpha(),[f'images/Jeu de combat/Dusk/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Dusk',200000),20)
yggdra = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Suzumebachi.png').convert_alpha(),[f'images/Jeu de combat/Yggdra/Droite/Inaction/_a_{i},80.png' for i in range(7)],('Yggdra',450000),70,70)


class EcranHeros:
    def __init__(self,btns):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
        self.btns = btns
    def affiche(self):
        fenetre.blit(self.fond, (0, 0))
        btn_suivant.draw(fenetre,pygame.mouse.get_pos())
        for btn,ecran in self.btns.items():
            btn.draw(fenetre,pygame.mouse.get_pos())
            if btn.collision(clic.get_clic()):
                clic.set_clic((0,0))
                ecran.ecran.set_actif(True),self.ecran.set_actif(False)

hero = EcranHeros({
            btn_fleche : ecran_boutique,
            btn_sw : spiritwarior,
            btn_nighthero : nighthero,
            btn_spirithero : spirithero,
            btn_lancier : lancier,
            btn_zukong : zukong,
            btn_assassin : assassin,
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

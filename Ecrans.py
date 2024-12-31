import pygame
from fonctions import dessiner_zone_texte, dessiner_bouton
from objets_et_variables import *
from img import *
from Roulette_Russe import pistolet
from PileouFace import pileouface
from sons import *
from SQL import *

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
        elif joueur1.get_pseudo().lower() in ['rick','rickroll','rick roll', 'rickastley', 'rick astley']:
            if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                rr.ecran.set_actif(True),connexion.ecran.set_actif(False)
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
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 310 <= pygame.mouse.get_pos()[1] <= 360:
            fenetre.blit(jeucombat2, (320, 300))
        else:
            fenetre.blit(jeucombat1, (320, 300))
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
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
        self.btn_heros = [f'images/Btn_heros/_a_frm{i},70.png' for i in range(13)]
        self.btn = pygame.image.load('images/Btn_heros/_a_frm0,70.png').convert_alpha()
        self.frame = 0
    def affiche(self):
        fenetre.blit(self.fond, (0, 0))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 25 <= pygame.mouse.get_pos()[1] <= 65:
            fenetre.blit(fleche_retour2, (341, 21))
        else:
            fenetre.blit(fleche_retour, (340, 20))
        if 135 <= pygame.mouse.get_pos()[0] <= 195 and 135 <= pygame.mouse.get_pos()[1] <= 195:
            fenetre.blit(alcool2, (130, 130))
        else:
            fenetre.blit(alcool1, (130, 130))
        if 220 <= pygame.mouse.get_pos()[0] <= 280 and 135 <= pygame.mouse.get_pos()[1] <= 195:
            self.anim(0.1)
        else:
            fenetre.blit(self.btn, (215, 130))
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
    def affiche(self):
        fenetre.blit(self.fond, (0, 0))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 25 <= pygame.mouse.get_pos()[1] <= 65:
            fenetre.blit(fleche_retour2, (341, 21))
        else:
            fenetre.blit(fleche_retour, (340, 20))
        if 105 <= pygame.mouse.get_pos()[0] <= 165 and 165 <= pygame.mouse.get_pos()[1] <= 225:
            fenetre.blit(biere2, (100, 160))
            self.biere = True
        else:
            fenetre.blit(biere1, (100, 160))
            self.biere = False
        if 25 <= pygame.mouse.get_pos()[0] <= 85 and 165 <= pygame.mouse.get_pos()[1] <= 225:
            fenetre.blit(vodka2, (20, 160))
            self.vodka = True
        else:
            fenetre.blit(vodka1, (20, 160))
            self.vodka = False
        if 185 <= pygame.mouse.get_pos()[0] <= 265 and 165 <= pygame.mouse.get_pos()[1] <= 225:
            fenetre.blit(whisky2, (180, 160))
            self.whisky = True
        else:
            fenetre.blit(whisky1, (180, 160))
            self.whisky = False
        self.affiche_effets()

    def affiche_effets(self):
        if self.vodka:
            fenetre.blit(effet_vodka, (pygame.mouse.get_pos()[0]+40, pygame.mouse.get_pos()[1]-30))
        elif self.biere:
            fenetre.blit(effet_biere, (pygame.mouse.get_pos()[0]+40, pygame.mouse.get_pos()[1]-30))
        elif self.whisky:
            fenetre.blit(effet_whisky, (pygame.mouse.get_pos()[0]-180, pygame.mouse.get_pos()[1]-30))

class EcranHeros1:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
    def affiche(self):
        fenetre.blit(self.fond, (0, 0))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 25 <= pygame.mouse.get_pos()[1] <= 65:
            fenetre.blit(fleche_retour2, (341, 21))
        else:
            fenetre.blit(fleche_retour, (340, 20))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 305 <= pygame.mouse.get_pos()[1] <= 345:
            fenetre.blit(fleche_retour2, (341, 301))
        else:
            fenetre.blit(fleche_retour, (340, 300))
        fenetre.blit(icone_sw, (100, 160))
        fenetre.blit(icone_hero, (20, 160))
        fenetre.blit(icone_spirithero, (180, 160))
        fenetre.blit(icone_lancier, (260, 160))
        fenetre.blit(icone_zukong, (100, 240))
        fenetre.blit(icone_assassin, (20, 240))
        fenetre.blit(icone_zendo, (180, 240))
        fenetre.blit(icone_maehv, (260, 240))
        fenetre.blit(icone_hsuku, (20, 320))
        fenetre.blit(icone_sanguinar, (100, 320))
        fenetre.blit(icone_whistler, (180, 320))
        fenetre.blit(icone_tethermancer, (260, 320))

class EcranHeros2:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/Fonds d\'ecran/Boutique.png').convert_alpha()
    def affiche(self):
        fenetre.blit(self.fond, (0, 0))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 25 <= pygame.mouse.get_pos()[1] <= 65:
            fenetre.blit(fleche_retour2, (341, 21))
        else:
            fenetre.blit(fleche_retour, (340, 20))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 305 <= pygame.mouse.get_pos()[1] <= 345:
            fenetre.blit(fleche_retour2, (341, 301))
        else:
            fenetre.blit(fleche_retour, (340, 300))
        fenetre.blit(icone_aether, (100, 160))
        fenetre.blit(icone_pureblade, (20, 160))
        fenetre.blit(icone_twilight, (180, 160))
        fenetre.blit(icone_zukong, (260, 160))
        fenetre.blit(icone_hero, (100, 240))
        fenetre.blit(icone_spirithero, (20, 240))
        fenetre.blit(icone_sw, (180, 240))
        fenetre.blit(icone_lancier, (260, 240))
        fenetre.blit(icone_hsuku, (20, 320))
        fenetre.blit(icone_sanguinar, (100, 320))
        fenetre.blit(icone_whistler, (180, 320))
        fenetre.blit(icone_tethermancer, (260, 320))

class EcranSelection:
    def __init__(self, c, liste, hero, y, x = 50):
        self.police = pygame.font.Font('8-bitanco.ttf', 15)
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/arene.png').convert_alpha()
        self.anim = liste
        self.frame = 0
        self.bouton = pygame.image.load("images/Jeu de combat/compteur2.png")
        self.bouton2 = pygame.image.load("images/Jeu de combat/compteur3.png")
        self.valider = self.police.render(("Val ider"), True, noir)
        self.hero = hero
        self.prix = self.police.render((str(self.hero[1])), True, noir)
        self.y = y
        self.x = x
        self.infos = False
        self.caracteristiques = c
    def getinfos(self):
        return self.infos
    def setinfos(self,actif):
        self.infos = actif
    def affiche(self,speed):
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(pygame.image.load(self.anim[int(self.frame)]).convert_alpha(), (self.x, self.y))
        self.frame += speed
        if self.frame >= len(self.anim)-1:
            self.frame = 0
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 25 <= pygame.mouse.get_pos()[1] <= 65:
            fenetre.blit(fleche_retour2, (341, 21))
        else:
            fenetre.blit(fleche_retour, (340, 20))
        if 340 <= pygame.mouse.get_pos()[0] <= 390 and 200 <= pygame.mouse.get_pos()[1] <= 250:
            fenetre.blit(info2, (340, 200))
        else:
            fenetre.blit(info1, (340, 200))
        if self.infos:
            fenetre.blit(self.caracteristiques, (30, 50))
        elif self.hero[0] in joueur1.get_heros():
            fenetre.blit(self.bouton, (140, 330))
            fenetre.blit(self.valider, (165, 345))
        else:
            fenetre.blit(self.bouton, (140, 330))
            fenetre.blit(self.prix, (165, 345))
        
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
    def affiche(self,speed):
        self.num_frame += speed
        self.frame = self.frames[int(self.num_frame)]
        # Si toutes les images ont été jouées :
        if int(self.num_frame) == len(self.frames)-1:
            # On remet tout à 0
            self.num_frame = 0
        fenetre.blit(pygame.image.load(self.frame),(0,0))

connexion = Ecran1()
ecran2 = Ecran2()
boutique = EcranBoutique()
vodka = EcranVodka()
ecran_mort = EcranMort()
ecran_victoire = EcranVictoire()
ecran_black = EcranBlack()
rr = EcranRR()
alcool = EcranAlcool()
hero = EcranHeros1()
hero2 = EcranHeros2()
assassin = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(), [f'images/Jeu de combat/Assassin/Droite/Attaque1/_a_frm{i},100.png' for i in range(10)] + [f'images/Jeu de combat/Assassin/Droite/Attaque2/_a_frm{i},100.png' for i in range(11,18)] + [f'images/Jeu de combat/Assassin/Droite/Marche/_a_frm{i},100.png' for i in range(8)] + [f'images/Jeu de combat/Assassin/Droite/Course/_a_frm{i},70.png' for i in range(8)] + [f'images/Jeu de combat/Assassin/Droite/Saut/_a_frm{i},100.png' for i in range(2,14)] + [f'images/Jeu de combat/Assassin/Mort/_a_frm{i},100.png' for i in range(16)],('Assassin',60000), 50)
maehv = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Maehv.png').convert_alpha(),[f'images/Jeu de combat/Maehv/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Maehv',450000),5)
zendo = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Zendo.png').convert_alpha(),[f'images/Jeu de combat/Zendo/Droite/Inaction/_a_frm{i},60.png' for i in range(14)],('Zendo',125000),5)
zukong = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Zukong/Droite/Inaction/_a_frm{i},80.png' for i in range(14)],('Zukong',100000),56,75)
nighthero = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Hero/Block/Block ({i}).png' for i in range(1,19)],('Night Hero',0),100,100)
spirithero = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Spirit_Hero/Inaction/_a_frm{i},100.png' for i in range(10)],('Spirit Hero',45000),50)
spiritwarior = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/SpiritWarrior.png').convert_alpha(),[f'images/Jeu de combat/Spirit_Warrior/Inaction/_a_frm{i},100.png' for i in range(8)],('Spirit Warior',30000),80,65)
lancier = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Lancier/Inaction/_a_frm{i},100.png' for i in range(8)],('Lancier',45000),70)
hsuku = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Hsuku.png').convert_alpha(),[f'images/Jeu de combat/Hsuku/Droite/Inaction/_a_{i},80.png' for i in range(28)],('Hsuku',250000),10)
sanguinar = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Sanguinar/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Sanguinar',60000),10)
whistler = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Whistler.png').convert_alpha(),[f'images/Jeu de combat/Whistler/Droite/Inaction/_a_{i},100.png' for i in range(18)],('Whistler',60000),80,95)
tethermancer = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Whistler.png').convert_alpha(),[f'images/Jeu de combat/Tethermancer/Droite/Inaction/_a_{i},100.png' for i in range(17)],('Tethermancer',60000),20)
aether = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/NightHero.png').convert_alpha(),[f'images/Jeu de combat/Aether/Droite/Inaction/_a_{i},100.png' for i in range(12)],('Aether',60000),97,93)
pureblade = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Pureblade.png').convert_alpha(),[f'images/Jeu de combat/Pureblade/Droite/Inaction/_a_frm{i},80.png' for i in range(10)],('Pureblade',60000),10)
twilight = EcranSelection(pygame.image.load('images/Jeu de Combat/Infos/Twilight.png').convert_alpha(),[f'images/Jeu de combat/Twilight/Droite/Inaction/_a_{i},80.png' for i in range(14)],('Twilight',60000),20)
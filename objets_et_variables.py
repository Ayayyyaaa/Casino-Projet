from classes import *
from img import *

fenetre.blit(chargement[1], (0, 0))  # Afficher le fond
pygame.display.flip()  # Mettre à jour l'affichage
print("Chargement de objets_et_variables...")

blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (128, 128, 128)
joueur1 = Joueur()
bouton2 = Bouton(160, 25, 0, 0)
bouton3 = Bouton(160, 25, 0, 25)
clock = pygame.time.Clock()
clic = Clic()
boutique = {'Chope de Bière' : 100000, 'Bouteille de Whisky' : 5000}
btn_entrer = Button(entrer2, entrer, 108, 240)
btn_retour = Button(retour2, retour, 108, 240)
btn_boutique = Button(boutique2, boutique1, 10, 65)
btn_fleche = Button(fleche_retour2, fleche_retour, 340, 25)
btn_roulette = Button(roulette2, roulette, 320, 20)
btn_pile_ou_face = Button(imgpof2, imgpof, 320, 90)
btn_machine_a_sous = Button(machine_a_sous2, machine_a_sous1, 320, 160)
btn_blackjack = Button(blackjack2, blackjack1, 320, 230)
btn_jeu_combat = Button(jeucombat2, jeucombat1, 320, 300)
btn_face = Button(face2, face2, 125, 230)
btn_pile = Button(pile2, pile2, 230, 230)


coin = Coin(100, -7)



import sqlite3
import pygame
from objets_et_variables import joueur1
from img import chargement

print("Chargement de SQL.py")

def creer_table():
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "compte" (
            "id_compte"	INTEGER,
            "pseudo" TEXT NOT NULL,
            "mdp" TEXT,
            solde INTEGER DEFAULT 2000,
            "derniere_connexion" TIMESTAMP,
            "code_cb" TEXT,
            "numero_cb"	TEXT,
            PRIMARY KEY("id_compte" AUTOINCREMENT)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS objets(
            nom_objet TEXT PRIMARY KEY,
            prix INTEGER,
            duree INTEGER,
            effet TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventaire (
            id_compte INTEGER,
            nom_objet TEXT,
            quantite_objet INTEGER,
            FOREIGN KEY (id_compte) REFERENCES compte (id_compte),
            FOREIGN KEY (nom_objet) REFERENCES objets (nom_objet),
            PRIMARY KEY(id_compte, nom_objet)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS heros(
            nom_heros TEXT PRIMARY KEY,
            prix INTEGER,
            faction TEXT,
            element TEXT,
            rarete INTEGER,
            lore TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS boss(
            nom_boss TEXT PRIMARY KEY,
            element TEXT,
            difficulte INTEGER,
            lore TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats(
            id_compte INTEGER,
            victoires INTEGER,
            defaites INTEGER,
            nom_boss TEXT,
            FOREIGN KEY(id_compte) REFERENCES compte (id_compte),
            FOREIGN KEY(nom_boss) REFERENCES boss (nom_boss),
            PRIMARY KEY(id_compte, nom_boss)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS casier(
            id_compte INTEGER,
            nom_heros TEXT,
            FOREIGN KEY(id_compte) REFERENCES compte (id_compte),
            FOREIGN KEY(nom_heros) REFERENCES heros (nom_heros),
            PRIMARY KEY(id_compte, nom_heros)
        )
    """)
    conn.commit()
    conn.close()

def verifier_et_ajouter_pseudo(pseudo:str, mdp:str):
    """
    Vérifie si la combinaison pseudo et mdp existe déjà. Si non, l'ajoute.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compte WHERE pseudo = ? AND mdp = ?", (pseudo, mdp))
    compte = cursor.fetchone()
    if compte is None:
        # Ajouter le compte à la base
        cursor.execute("INSERT INTO compte (pseudo, mdp,solde) VALUES (?, ?,?)", (pseudo, mdp,joueur1.get_cagnotte()))
        conn.commit()
        cursor.execute("SELECT id_compte FROM compte WHERE pseudo = ? AND mdp = ?", (pseudo, mdp))
        joueur1.set_cagnotte(200000)
        id_ = cursor.fetchone()
        mettre_a_jour_solde(joueur1.get_cagnotte(), id_[0])
        ajouter_hero_casier(id_[0],'Night_Hero')
        cursor.execute("INSERT INTO inventaire (id_compte) VALUES (?)", (id_[0],))
        conn.commit()
        print(f"Compte créé avec succès ! Bienvenue '{pseudo}' !")
        

    conn.close()

def det_id_compte(pseudo:str,mdp:str) -> int:
    '''
    Récupère l'id du compte correspondant au pseudo et mot de passe fourni dans la base de données.
    Paramètres :
        - pseudo (str) : Le pseudo du joueur
        - mdp (str) : Le mot de passe du joueur
    Returns :
        - L'id du compte correspondant ou None si aucun compte correspondant n'est trouvé
    '''
    assert type(pseudo) == str, "Le pseudo doit être une chaîne de caractères."
    assert type(mdp) == str, "Le mot de passe doit être une chaîne de caractères."
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_compte FROM compte WHERE pseudo = ? AND mdp = ?", (pseudo,mdp))
    id_compte = cursor.fetchone()
    conn.close()
    return id_compte[0] if id_compte else None

def recup_donnees(id_compte:int) -> float:
    """
    Récupère le solde du joueur dans la base de données.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT solde FROM compte WHERE id_compte = ?", (id_compte,))
    solde = cursor.fetchone()
    conn.close()
    return solde[0] if solde else 200000

def ajouter_connexion(id_compte):
    """
    Met à jour la date de dernière connexion.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE compte SET derniere_connexion = CURRENT_TIMESTAMP WHERE id_compte = ?", (id_compte,))
    conn.commit()
    conn.close()

def mettre_a_jour_solde(solde, id_compte):
    """
    Met à jour le solde du joueur dans la base de données.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE compte SET solde = ? WHERE id_compte = ?", (solde, id_compte))
    conn.commit()
    conn.close()

def verifier_et_ajouter_cb(id, num, code):
    """
    Vérifie si la combinaison id est associée au numéro de code de cb. Si non, l'ajoute.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT code_cb,numero_cb FROM compte WHERE id_compte = ?", (id,))
    compte = cursor.fetchone()
    if compte == (None,None):
        # Ajouter le compte à la base
        cursor.execute("UPDATE compte SET code_cb = ?, numero_cb = ? WHERE id_compte = ?", (code,num,id))
        conn.commit()
        cursor.execute("SELECT code_cb,numero_cb FROM compte WHERE id_compte = ?", (id,))
        coordonnes = cursor.fetchone()
        conn.commit()
        if coordonnes:
            print(f"Coordonnées enregistrées avec succès !")
    conn.close()
    return True if compte[0] == code and compte[1] == num else False

def ajout_des_attributs():
    '''
    ajoute les attributs dans la base de donnée
    '''
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()

    #Création des objets 
 
    """#Vodka
    cursor.execute('''INSERT INTO objets VALUES ('Vodka', 1000, 1, 'Augmente les gains de la Roulette Russe de 10% (n est pas compatible avec un autre alcool qui affecte la Roulette Russe)')''')
    #Biere
    cursor.execute('''INSERT INTO objets VALUES ('Biere', 100000, 2, 'Enlève une balle dans la roulette russe et diminue les gains de 10% (n est pas compatible avec un autre alcool qui affecte la Roulette Russe)')''')
    #Vin
    cursor.execute('''INSERT INTO objets VALUES ('Vin', 10000, 1, 'Augmente les gains et les pertes du Blackjack de 10% (n est pas compatible avec un autre alcool qui affecte le Blackjack)')''')
    #Rhum
    cursor.execute('''INSERT INTO objets VALUES ('Rhum', 50000, 1, 'Ajoute une balle à la Roulette Russe et augmente les gains de 30%(n est pas compatible avec un autre alcool qui affecte la Roulette Russe)')''')
    #Whisky
    cursor.execute('''INSERT INTO objets VALUES ('Whisky', 35000, 5, 'Augmente les chances de gagner au pile ou face de 10% et diminue les chances d obtenir 3 fruits dans la machine à sous (n est pas compatible avec un autre alcool qui affecte la machine à sous ou le pile ou face)')''')
    #Mojito
    cursor.execute('''INSERT INTO objets VALUES ('Mojito', 35000, 7, 'Sélectionne aléatoirement deux fruits et augmente les chances de les obtenir de 10% (n est pas compatible avec un autre alcool qui affecte la machine à sous)')''')
    """
    #Création des heros

    #Night_Hero
    cursor.execute('''INSERT INTO heros VALUES ('Night_Hero', 0, 'Abyss', 'Nuit', 1, 'blabla')''')
    #Spirit_Hero
    cursor.execute('''INSERT INTO heros VALUES ('Spirit_Hero', 45000, 'Nécrons', 'Esprit', 2, 'blabla')''')
    #Spirit_Warrior
    cursor.execute('''INSERT INTO heros VALUES ('Spirit_Warrior', 30000, 'Nécrons', 'Esprit', 2, 'blabla')''')
    #Lancier
    cursor.execute('''INSERT INTO heros VALUES ('Lancier', 45000, 'Nécrons', 'Esprit', 2, 'blabla')''')
    #Assassin
    cursor.execute('''INSERT INTO heros VALUES ('Assassin', 60000, 'Mercenaire', 'Neutre', 3, 'blabla')''')
    #Zukong
    cursor.execute('''INSERT INTO heros VALUES ('Zukong', 45000, 'Murim', 'Neutre', 2, 'blabla')''')
    #Maevh
    cursor.execute('''INSERT INTO heros VALUES ('Maevh', 350000, 'Abyss', 'Feu', 5, 'blabla')''')
    #Zendo
    cursor.execute('''INSERT INTO heros VALUES ('Zendo', 200000, 'Murim', 'Air', 4, 'blabla')''')
    #Pureblade
    cursor.execute('''INSERT INTO heros VALUES ('Pureblade', 275000, 'Empire', 'Feu', 5, 'blabla')''')
    #Hsuku
    cursor.execute('''INSERT INTO heros VALUES ('Hsuku', 300000, 'Mercenaire', 'Neutre', 5, 'blabla')''')
    #Sanguinar
    cursor.execute('''INSERT INTO heros VALUES ('Sanguinar', 400000, 'Abyss', 'Nuit', 5, 'blabla')''')
    #Whistler
    cursor.execute('''INSERT INTO heros VALUES ('Whistler', 400000, 'Empire', 'Feu', 5, 'blabla')''')
    #Tethermancer
    cursor.execute('''INSERT INTO heros VALUES ('Tethermancer', 250000, 'Mercenaire', 'Feu', 4, 'blabla')''')
    #Aether
    cursor.execute('''INSERT INTO heros VALUES ('Aether', 175000, 'Empire', 'Air', 4, 'blabla')''')
    #Twilight
    cursor.execute('''INSERT INTO heros VALUES ('Twilight', 180000, 'Créature légendaire', 'Feu', 4, 'blabla')''')
    #Yggdra
    cursor.execute('''INSERT INTO heros VALUES ('Yggdra', 450000, 'Abyss', 'Feu', 5, 'blabla')''')
    #Dusk
    cursor.execute('''INSERT INTO heros VALUES ('Dusk', 200000, 'Mercenaire', 'Foudre', 4, 'blabla')''')
    #Suzumebachi
    cursor.execute('''INSERT INTO heros VALUES ('Suzumebachi', 180000, 'Empire', 'Feu', 4, 'blabla')''')

    #Création des boss
    #Michel
    cursor.execute('''INSERT INTO boss VALUES ('Michel', 'Neutre', 2, 'blabla')''')
    #TankBoss
    cursor.execute('''INSERT INTO boss VALUES ('TankBoss', 'Foudre', 4, 'blabla')''')
    #Cindera
    cursor.execute('''INSERT INTO boss VALUES ('Cindera', 'Feu', 3, 'blabla')''')
    #DarkLord
    cursor.execute('''INSERT INTO boss VALUES ('DarkLord', 'Nuit', 2, 'blabla')''')
    #Astral (il est nul)
    cursor.execute('''INSERT INTO boss VALUES ('Astral (il est nul)', 'Esprit', 0, 'blabla')''')
    #EternityPainter
    cursor.execute('''INSERT INTO boss VALUES ('EternityPainter', 'Esprit', 3, 'blabla')''')
    #Shidai
    cursor.execute('''INSERT INTO boss VALUES ('Shidai', 'Foudre', 4, 'blabla')''')
    #Lilithe
    cursor.execute('''INSERT INTO boss VALUES ('Lilithe', 'Feu', 5, 'blabla')''')
    #Solfist
    cursor.execute('''INSERT INTO boss VALUES ('Solfist', 'Feu', 2, 'blabla')''')
    #Elyx
    cursor.execute('''INSERT INTO boss VALUES ('Elyx', 'Foudre', 3, 'blabla')''')
    #Embla
    cursor.execute('''INSERT INTO boss VALUES ('Embla', 'Glace', 3, 'blabla')''')
    #Sun
    cursor.execute('''INSERT INTO boss VALUES ('Sun', 'Feu', 2, 'blabla')''')
    #Skurge
    cursor.execute('''INSERT INTO boss VALUES ('Skurge', 'Feu', 4,  'blabla')''')
    #NoshRak
    cursor.execute('''INSERT INTO boss VALUES ('NoshRak', 'Foudre', 5, 'blabla')''')
    #Purgatos
    cursor.execute('''INSERT INTO boss VALUES ('Purgatos', 'Feu', 2, 'blabla')''')
    #Ciphyron
    cursor.execute('''INSERT INTO boss VALUES ('Ciphyron', 'Foudre', 2, 'blabla')''')
    #Golem
    cursor.execute('''INSERT INTO boss VALUES ('Golem', 'Foudre', 4, 'blabla')''')
    #Soji
    cursor.execute('''INSERT INTO boss VALUES ('Soji', 'Foudre', 5, 'blabla')''')
    #Prophet
    cursor.execute('''INSERT INTO boss VALUES ('Prophet', 'Nuit', 4, 'blabla')''')
    conn.commit()
    conn.close()


def ajouter_hero_casier(id_compte, nom_hero):
    """
    Ajoute le hero au casier du joueur
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO casier VALUES (?,?)", (id_compte, nom_hero))
    conn.commit()
    conn.close()

def ajouter_objet_inventaire(quantite_objet:int, id_compte:int, nom_objet:str):
    """
    Met a jour la quantite d'un objet dans l'inventaire du joueur, et l'ajoute s'il n'existe pas.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    # Vérifier si l'objet existe déjà pour ce compte
    cursor.execute("SELECT quantite_objet FROM inventaire WHERE id_compte = ? AND nom_objet = ?", (id_compte, nom_objet))
    resultat = cursor.fetchone()
    # Vérifier si l'inventaire pour ce compte est NULL
    cursor.execute("SELECT nom_objet, quantite_objet FROM inventaire WHERE id_compte = ?", (id_compte,))
    inv = cursor.fetchone()
    if resultat:
        # Si l'objet existe déjà on met a jour la qte
        nouvelle_quantite = resultat[0] + quantite_objet
        cursor.execute("UPDATE inventaire SET quantite_objet = ? WHERE id_compte = ? AND nom_objet = ?", 
                       (nouvelle_quantite, id_compte, nom_objet))
    else:
        if inv and inv[0] is None and inv[1] is None:
            # Si l'inventaire est NULL on remplace
            cursor.execute("UPDATE inventaire SET nom_objet = ?, quantite_objet = ? WHERE id_compte = ?", 
                       (nom_objet, quantite_objet, id_compte))
        else:
            # Sinon, on insere la nouvelle valeur
            cursor.execute("INSERT INTO inventaire (id_compte, nom_objet, quantite_objet) VALUES (?, ?, ?)", 
                           (id_compte, nom_objet, quantite_objet))
    
    conn.commit()
    conn.close()

def recup_objet(id_compte,nom_objet):
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT quantite_objet FROM inventaire WHERE id_compte = ? AND nom_objet = ?",(id_compte,nom_objet))
    dispo = cursor.fetchone()
    conn.close()
    return True if dispo else False

def stats_boss_vaincu(victoires,id_compte, nom_boss):
    '''
    Change la stat du nombre de victoire contre un boss
    '''
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE stats SET victoires = ? WHERE id_compte = ? and nom_boss = ?", (victoires, id_compte, nom_boss))
    conn.commit()
    conn.close()

def stats_boss_defaite(defaites,id_compte, nom_boss):
    '''
    Change la stat du nombre de défaite contre un boss
    '''
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE stats SET defaites = ? WHERE id_compte = ? and nom_boss = ?", (defaites, id_compte, nom_boss))
    conn.commit()
    conn.close()

def defaites_total(id_compte,):
    '''
    renvoie le nombre de defaites total
    '''
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT defaites FROM stats WHERE id_compte = ?", (id_compte,))
    toutes_defaites = cursor.fetchone()
    defaite = 0
    for i in range(len(toutes_defaites)):
        defaite += toutes_defaites[i][0]
    return defaite

def victoires_total(id_compte):
    '''
    renvoie le nombre de defaites total
    '''
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT victoires FROM stats WHERE id_compte = ?", (id_compte,))
    toutes_victoires = cursor.fetchone()
    victoire = 0
    for i in range(len(toutes_victoires)):
        victoire += toutes_victoires[i][0]
    return victoire

def supprimer_table():
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE inventaire")
    cursor.execute("DROP TABLE stats")
    cursor.execute("DROP TABLE compte")
    cursor.execute("DROP TABLE casier")
    cursor.execute("DROP TABLE boss")
    cursor.execute("DROP TABLE heros")
    conn.commit()
    conn.close()

def det_heros(id_compte):
    print(id_compte)
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nom_heros FROM casier WHERE id_compte = ?", (id_compte,))
    id_compte = cursor.fetchall()
    conn.close()
    liste_heros = [heros[0] for heros in id_compte]
    return liste_heros

def det_objets(id_compte):
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nom_objet, quantite_objet FROM inventaire WHERE id_compte = ?", (id_compte,))
    obj = cursor.fetchall()
    conn.close()
    dico_objets = {}
    for truc in obj:
        if truc[0] is not None and truc[1] is not None:
            dico_objets[truc[0]] = truc[1]
    print(dico_objets)
    return dico_objets

def maj_stats(id_compte,victoire,defaite,boss):
    """
    Met a jour les stats d'un joueur apres un combat.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    # Vérifier le joueur a deja combattu ce boss
    cursor.execute("SELECT victoires, defaites FROM stats WHERE id_compte = ? AND nom_boss = ?", (id_compte, boss))
    resultat = cursor.fetchone()
    # Vérifier si le joueur a deja combattu un boss
    cursor.execute("SELECT victoires, defaites FROM stats WHERE id_compte = ?", (id_compte,))
    inv = cursor.fetchone()
    if resultat:
        # Si le boss a déja ete combattu
        victoires = resultat[0] + victoire
        defaites = resultat[1] + defaite
        cursor.execute("UPDATE stats SET victoires = ?, defaites = ? WHERE id_compte = ? AND nom_boss = ?", 
                       (victoires, defaites, id_compte, boss))
    else:
        if inv and inv[0] is None and inv[1] is None:
            # Si le joueur n'a jamais combattu de boss
            cursor.execute("UPDATE stats SET victoires = ?, defaites = ? WHERE id_compte = ? AND nom_boss = ?", 
                       (victoires, defaites, id_compte, boss))
        else:
            # Sinon, on insere la nouvelle valeur
            cursor.execute("INSERT INTO stats (id_compte, victoires, defaites, nom_boss) VALUES (?, ?, ?, ?)", 
                           (id_compte, victoire, defaite, boss))
    
    conn.commit()
    conn.close()


#supprimer_table()
creer_table()
#ajout_des_attributs()
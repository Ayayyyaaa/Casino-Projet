import sqlite3
import pygame
from objets_et_variables import joueur1
from img import chargement
from fonctions import afficher_ecran_chargement

afficher_ecran_chargement(chargement[5])
print("Chargement de SQL.py")

def creer_table():
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS compte (
            id_compte INTEGER PRIMARY KEY AUTOINCREMENT,
            pseudo TEXT NOT NULL,
            mdp TEXT,
            derniere_connexion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventaire (
            id_compte INTEGER PRIMARY KEY,
            solde INTEGER DEFAULT 2000,
            FOREIGN KEY (id_compte) REFERENCES compte (id_compte)
        )
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS "cd_bancaires" (
    "code_cb"	TEXT,
    "numero_cb"	TEXT,
    "id_compte"	INTEGER,
    FOREIGN KEY("id_compte") REFERENCES "compte"("id_compte"))""")

    conn.commit()
    conn.close()

creer_table()

def verifier_et_ajouter_pseudo(pseudo, mdp):
    """
    Vérifie si la combinaison pseudo et mdp existe déjà. Si non, l'ajoute.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compte WHERE pseudo = ? AND mdp = ?", (pseudo, mdp))
    compte = cursor.fetchone()
    if compte is None:
        # Ajouter le compte à la base
        cursor.execute("INSERT INTO compte (pseudo, mdp) VALUES (?, ?)", (pseudo, mdp))
        conn.commit()
        cursor.execute("SELECT id_compte FROM compte WHERE pseudo = ? AND mdp = ?", (pseudo, mdp))
        id_ = cursor.fetchone()
        if id_:
            joueur1.set_cagnotte(200000)
            cursor.execute("INSERT INTO inventaire (id_compte, solde) VALUES (?, ?)", (id_[0], joueur1.get_cagnotte()))
            conn.commit()
            print(f"Compte créé avec succès ! Bienvenue '{pseudo}' !")

    conn.close()

def det_id_compte(pseudo,mdp):
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_compte FROM compte WHERE pseudo = ? AND mdp = ?", (pseudo,mdp,))
    id_compte = cursor.fetchone()
    conn.close()
    return id_compte[0] if id_compte else None

def recup_donnees(id_compte:int):
    """
    Récupère le solde du joueur dans la base de données.
    Paramètres:
    - id_compte: int
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT solde FROM inventaire WHERE id_compte = ?", (id_compte,))
    inventaire = cursor.fetchone()
    conn.close()
    return inventaire[0] if inventaire else None

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
    cursor.execute("UPDATE inventaire SET solde = ? WHERE id_compte = ?", (solde, id_compte))
    conn.commit()
    conn.close()

def verifier_et_ajouter_cb(ide, num, code):
    """
    Vérifie si la combinaison id est associée au numéro de code de cb. Si non, l'ajoute.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT code_cb,numero_cb FROM compte WHERE id_compte = ?", (ide,))
    compte = cursor.fetchone()
    if compte == (None,None):
        # Ajouter le compte à la base
        cursor.execute("UPDATE compte SET code_cb = ?, numero_cb = ? WHERE id_compte = ?", (code,num,ide))
        conn.commit()
        cursor.execute("SELECT code_cb,numero_cb FROM compte WHERE id_compte = ?", (ide,))
        coordonnes = cursor.fetchone()
        conn.commit()
        if coordonnes:
            print(f"Coordonnées enregistrées avec succès !")
    conn.close()
    return True if compte[0] == code and compte[1] == num else False

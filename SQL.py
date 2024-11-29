import sqlite3

def creer_table():
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    #cursor.execute("""DROP TABLE IF EXISTS compte""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS compte (
        id_compte INTEGER PRIMARY KEY AUTOINCREMENT,
        pseudo TEXT UNIQUE NOT NULL,
        mdp TEXT,
        inventaire INTEGER DEFAULT 0)
        """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventaire (
        id_compte INTEGER PRIMARY KEY,
        solde INTEGER,
        FOREIGN KEY (id_compte) REFERENCES compte (id_compte) )
        """)
    conn.close

creer_table()

def verifier_et_ajouter_pseudo(pseudo):
    """
    Vérifie si le pseudo existe déjà. Si non, il l'ajoute.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compte WHERE pseudo = ?", (pseudo,))
    compte = cursor.fetchone()
    if compte is None:
        # Ajouter le pseudo à la base
        cursor.execute("INSERT INTO compte (pseudo) VALUES (?)", (pseudo,))
        conn.commit()
        cursor.execute('''SELECT id_compte FROM compte WHERE pseudo = ?''', (pseudo,))
        id_ = cursor.fetchone()
        # Insérer dans la table inventaire
        cursor.execute('''INSERT INTO inventaire VALUES (?, ?)''', (id_[0], 2000))
        conn.commit()
        print(f"Le pseudo '{pseudo}' a été ajouté.")
        conn.close()


def det_id_compte(pseudo):
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_compte FROM compte WHERE pseudo = ?", (pseudo,))
    id_compte = cursor.fetchone()
    conn.close()
    return id_compte[0]

def mettre_a_jour_solde(solde, id_compte):
    """
    Met à jour le solde du joueur dans la base de données.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE inventaire SET solde = ? WHERE id_compte = ?", (solde, id_compte))
    conn.commit()
    conn.close()

def derniere_co():
    import sqlite3

def ajouter_connexion(id_compte):
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE compte SET derniere_connexion = CURRENT_TIMESTAMP WHERE id_compte = (?)", (id_compte,))
    conn.commit()
    conn.close()


def recup_donnees(id_compte):
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT solde FROM inventaire WHERE id_compte = ?", (id_compte,))
    conn.commit()
    inventaire = cursor.fetchone()
    conn.close()
    return inventaire



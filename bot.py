import pandas as pd
import os

# Mettre le path allant vers son fichier xlsx.
fichier_excel = './files/UNICEF Vaccination Stats.xlsx'

# Nom du dossier où enregistrer les CSV. 
dossier_csv = 'Data_Extracts'

# Crée le dossier s'il n'existe pas
if not os.path.exists(dossier_csv):
    os.makedirs(dossier_csv)

# Charge le fichier Excel avec toutes les feuilles
xls = pd.ExcelFile(fichier_excel)

# Boucle sur chaque feuille et enregistre chaque feuille dans un fichier CSV dans le dossier
for sheet_name in xls.sheet_names:
    # Lire la feuille dans un DataFrame
    df = pd.read_excel(xls, sheet_name=sheet_name)
    # Crée le chemin du fichier CSV dans le dossier choisi
    fichier_csv = os.path.join(dossier_csv, f"{sheet_name}.csv")
    # Sauvegarder le DataFrame dans un fichier CSV
    df.to_csv(fichier_csv, index=False)
    print(f"Feuille '{sheet_name}' enregistrée en tant que '{fichier_csv}'")

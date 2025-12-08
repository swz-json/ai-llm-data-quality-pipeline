import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def clean_clients(clients: pd.DataFrame) -> pd.DataFrame:
    df = clients.copy()

    # Standardiser noms de colonnes
    df.columns = df.columns.str.lower()

    # Nettoyer emails (enlever espaces, mettre en minuscule)
    df["email"] = df["email"].str.strip().str.lower()

    # Retirer doublons
    df = df.drop_duplicates()

    # Retirer lignes vides
    df = df.dropna(how="all")

    return df

def clean_commandes(commandes: pd.DataFrame) -> pd.DataFrame:
    df = commandes.copy()
    df.columns = df.columns.str.lower()  # Commandeid → commandeid, DateCommande → datecommande

    # Convertir la colonne datecommande en datetime
    if "datecommande" in df.columns:
        df["datecommande"] = pd.to_datetime(df["datecommande"], errors="coerce")
    else:
        print("Colonne 'datecommande' non trouvée")

    # Quantité négative → anomalie
    if "quantité" in df.columns:
        df.loc[df["quantité"] <= 0, "quantité"] = 1

    # Total négatif → anomalie (LLM devra analyser)
    if "total" in df.columns:
        df.loc[df["total"] < 0, "total"] = None

    return df


def clean_produits(produits: pd.DataFrame) -> pd.DataFrame:
    df = produits.copy()
    df.columns = df.columns.str.lower()
    df = df.drop_duplicates()
    return df

def save_processed(df: pd.DataFrame, name: str):
    path = PROCESSED_DIR / name
    df.to_csv(path, index=False)
    print(f"✔️ Saved: {path}")

def clean_all(clients, commandes, produits):
    print("🧹 Cleaning datasets...")

    clients_clean = clean_clients(clients)
    commandes_clean = clean_commandes(commandes)
    produits_clean = clean_produits(produits)

    # Save
    save_processed(clients_clean, "clients_clean.csv")
    save_processed(commandes_clean, "commandes_clean.csv")
    save_processed(produits_clean, "produits_clean.csv")

    print("Cleaning done!")

    return clients_clean, commandes_clean, produits_clean

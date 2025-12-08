import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

def load_clients():
    return pd.read_csv(RAW_DIR / "clients.csv")

def load_commandes():
    return pd.read_csv(RAW_DIR / "commandes.csv")

def load_produits():
    return pd.read_csv(RAW_DIR / "produits.csv")

def load_all():
    print("📥 Loading raw datasets...")
    clients = load_clients()
    commandes = load_commandes()
    produits = load_produits()

    print("✔️ clients:", clients.shape)
    print("✔️ commandes:", commandes.shape)
    print("✔️ produits:", produits.shape)

    return clients, commandes, produits

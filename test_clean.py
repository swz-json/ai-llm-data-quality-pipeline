from pipelines.ingest import load_all
from pipelines.clean import clean_all

clients, commandes, produits = load_all()
clients_c, commandes_c, produits_c = clean_all(clients, commandes, produits)

print(commandes_c.head())

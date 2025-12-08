from pipelines.ingest import load_all

clients, commandes, produits = load_all()
print(clients.head())

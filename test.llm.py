from pipelines.ingest import load_all
from pipelines.clean import clean_all
from pipelines.llm_validation import validate_with_llm

clients, commandes, produits = load_all()
clients_c, commandes_c, produits_c = clean_all(clients, commandes, produits)

validate_with_llm(commandes_c)

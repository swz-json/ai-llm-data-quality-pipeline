import streamlit as st
import pandas as pd
import json
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
VALIDATED_DIR = Path("data/validated")

@st.cache_data
def load_data():
    clients = pd.read_csv(PROCESSED_DIR / "clients_clean.csv")
    commandes = pd.read_csv(PROCESSED_DIR / "commandes_clean.csv")
    produits = pd.read_csv(PROCESSED_DIR / "produits_clean.csv")

    with open(VALIDATED_DIR / "commandes_report.json", "r", encoding="utf-8") as f:
        report = json.load(f)

    return clients, commandes, produits, report

def main():
    st.set_page_config(
        page_title="E-commerce Data Quality – LLM Pipeline",
        layout="wide"
    )

    st.title("AI-Powered E-commerce Data Pipeline")
    st.caption("Ingestion → Cleaning → LLM Data Quality → Dashboard")

    clients, commandes, produits, report = load_data()

    # ===== KPIs =====
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Clients", len(clients))
    with col2:
        st.metric("Commandes", len(commandes))
    with col3:
        st.metric("Produits", len(produits))
    with col4:
        st.metric("Chiffre d'affaires total", f"{commandes['total'].sum():.2f}")

    st.markdown("---")

    # ===== Ventes dans le temps =====
    st.subheader("Ventes au fil du temps")
    commandes_date = commandes.copy()
    commandes_date["datecommande"] = pd.to_datetime(commandes_date["datecommande"])
    by_date = commandes_date.groupby("datecommande")["total"].sum().reset_index()
    st.line_chart(by_date.set_index("datecommande"))

    # ===== Tableau des commandes =====
    st.subheader("Aperçu des commandes nettoyées")
    st.dataframe(commandes.head(20))

    st.markdown("---")

    # ===== Anomalies détectées =====
    st.subheader("Anomalies détectées automatiquement")

    anomalies = report.get("anomalies_detected", {})
    missing = anomalies.get("missing_values", {})
    quantite_suspecte = anomalies.get("quantite_suspecte", [])
    totaux_negatifs = anomalies.get("totaux_negatifs", [])
    dates_invalides = anomalies.get("dates_invalides", [])

    colA, colB = st.columns(2)

    with colA:
        st.markdown("**Valeurs manquantes par colonne**")
        if missing:
            st.json(missing)
        else:
            st.write("Aucune valeur manquante détectée.")

        st.markdown("**Quantités suspectes (≤ 0)**")
        if quantite_suspecte:
            st.dataframe(pd.DataFrame(quantite_suspecte))
        else:
            st.write("Aucune quantité suspecte.")

    with colB:
        st.markdown("**Totaux négatifs**")
        if totaux_negatifs:
            st.dataframe(pd.DataFrame(totaux_negatifs))
        else:
            st.write("Aucun total négatif.")

        st.markdown("**Dates invalides**")
        if dates_invalides:
            st.dataframe(pd.DataFrame(dates_invalides))
        else:
            st.write("Aucune date invalide.")

    st.markdown("---")

    # ===== Analyse LLM =====
    st.subheader("Analyse générée par le LLM")

    llm_analysis = report.get("llm_analysis", "Aucune analyse disponible.")
    st.text_area("Rapport LLM", llm_analysis, height=250)

if __name__ == "__main__":
    main()

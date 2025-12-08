# AI-Powered E-commerce Data Quality Pipeline

### Pipeline complet de qualité de données + validation LLM + dashboard analytique

### 🔗 Figma (Dashboard + Architecture interactive)
#### -> https://www.figma.com/make/v0DRrtrvwKEjx9iA1PZjNa/Confetti-Explosion-on-Click?node-id=0-1&p=f&t=FtZFFkbh4LwivS3J-0&fullscreen=1


## 📌 Aperçu du Projet

Ce projet met en place un pipeline de qualité de données moderne pour un site e-commerce, intégrant :

➡️ Ingestion → Nettoyage → Validation LLM → Dashboard analytique

## Le pipeline :

Charge automatiquement les données brutes (clients, produits, commandes)

Nettoie et standardise les données

Détecte les anomalies via règles Python

Génère un rapport narratif intelligent via un LLM (OpenAI GPT-4)

Affiche les métriques, KPIs et visualisations dans un dashboard Streamlit moderne

Fournit une architecture professionnelle (documentée dans Figma)

Ce projet démontre des compétences en Data Engineering, LLM appliqué, analyse métier, automatisation et visualisation avancée.

## Architecture du Pipeline

🔗 Voir l’architecture détaillée sur Figma
-> https://www.figma.com/make/v0DRrtrvwKEjx9iA1PZjNa/Confetti-Explosion-on-Click?node-id=0-1&p=f&t=FtZFFkbh4LwivS3J-0&fullscreen=1

## Architecture du système :

data/raw : données brutes

pipelines/ingest.py : chargement des CSV

pipelines/clean.py : nettoyage + standardisation

pipelines/llm_validation.py : détection avancée via LLM

data/processed : données nettoyées

data/validated : anomalies + rapport narratif LLM

app/dashboard.py : visualisation Streamlit

## ✨ Fonctionnalités Clés
### 📥 1. Ingestion Automatique

Chargement sécurisé des fichiers clients / produits / commandes

Standardisation des types de données

### 🧹 2. Nettoyage & Qualité de Données

Détection de valeurs manquantes

Anomalies de prix, quantités, dates

Outliers et montants incohérents

Génération d’un dataset nettoyé exploitable

### 🤖 3. Validation LLM (OpenAI GPT-4)

Le LLM produit automatiquement :

Résumé exécutif

Problèmes identifiés

Recommandations stratégiques

Impact business estimé

### 📌 Exemple :

“Taux de conformité : 94,8%, amélioration de 2,1%.
47 anomalies détectées, principalement sur quantités et valeurs manquantes.”

### 📊 4. Dashboard Analytique (Streamlit)

KPIs affichés :

Clients actifs

Commandes totales

Chiffre d’affaires

Taux de conversion

Qualité globale des données

Visualisations :

Évolution des ventes

Tableau des anomalies détectées

Aperçu des commandes nettoyées



## 🛠️ Technologies Utilisées

Python 3.10+

Pandas / NumPy

Streamlit

OpenAI GPT-4

Matplotlib / Plotly

Figma (architecture + UI design)

## ▶️ Comment Exécuter le Projet
### 1. Installer les dépendances
pip install -r requirements.txt

### 2. Lancer le pipeline
python pipelines/ingest.py
python pipelines/clean.py
python pipelines/llm_validation.py

### 3. Lancer le dashboard
streamlit run app/dashboard.py

## 🌟 Auteur

👤 Wassim Elmoufakkir

Linkedin : [https://portfolio-main-five-inky.vercel.app/](https://www.linkedin.com/in/wassim-elmoufakkir/)

GitHub : https://github.com/swz-json

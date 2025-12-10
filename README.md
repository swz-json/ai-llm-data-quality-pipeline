# 🚀 AI-Powered E-commerce Data Quality Pipeline

Un pipeline complet de qualité de données pour e-commerce intégrant validation LLM et dashboard analytique interactif.

[🔗 Figma – Dashboard & Architecture](https://www.figma.com/make/v0DRrtrvwKEjx9iA1PZjNa/Confetti-Explosion-on-Click?node-id=0-1&p=f&t=FtZFFkbh4LwivS3J-0&fullscreen=1)

---

## 📌 Aperçu du Projet

Ce projet met en place un pipeline moderne de traitement et validation de données e-commerce, incluant :

- **Ingestion → Nettoyage → Validation LLM → Dashboard analytique**
- Automatisation du chargement, nettoyage et validation des données clients, produits et commandes
- Génération d’un **rapport narratif intelligent** grâce à OpenAI GPT-4
- Visualisation des **KPIs clés** et des anomalies dans un dashboard **Streamlit** moderne
- Architecture professionnelle documentée sous **Figma**

---


🔗 **Voir l’architecture interactive sur Figma**  
[👉 Accès Figma](https://www.figma.com/make/v0DRrtrvwKEjx9iA1PZjNa/Confetti-Explosion-on-Click?node-id=0-1&p=f&t=FtZFFkbh4LwivS3J-0&fullscreen=1)

---

## ✨ Fonctionnalités Clés

### 📥 1. Ingestion Automatique
- Chargement sécurisé des fichiers clients, produits, commandes (CSV)
- Standardisation des types de données

### 🧹 2. Nettoyage & Qualité de Données
- Détection de valeurs manquantes
- Anomalies de prix, quantités, dates
- Suppression des outliers et incohérences
- Génération d’un dataset propre et exploitable

### 🤖 3. Validation par LLM (OpenAI GPT-4)
- Génère automatiquement :
  - Résumé exécutif
  - Problèmes détectés
  - Recommandations
  - Estimation de l’impact business

📌 Exemple :  
> “Taux de conformité : 94,8%, amélioration de 2,1%.  
> 47 anomalies détectées, principalement sur quantités et valeurs manquantes.”

### 📊 4. Dashboard Analytique (Streamlit)
- **KPIs affichés** :
  - Clients actifs
  - Commandes totales
  - Chiffre d’affaires
  - Taux de conversion
  - Qualité globale des données

- **Visualisations** :
  - Évolution des ventes
  - Tableau des anomalies détectées
  - Aperçu des commandes nettoyées



---

## ▶️ Comment Exécuter le Projet

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancer le pipeline
```bash
python pipelines/ingest.py
python pipelines/clean.py
python pipelines/llm_validation.py
```
### 3. Démarrer le dashboard
```bash
streamlit run app/dashboard.py
```
## 🛠️ Technologies Utilisées

Python 3.10+

Pandas / NumPy

Streamlit (Dashboard)

OpenAI GPT-4 (Validation & Résumés)

Matplotlib / Plotly (Visualisation)

Figma (Design UI & Architecture technique)

##📚 Documentation

Architecture complète et interface UI sur Figma

Scripts bien commentés dans le dossier pipelines/

Tests unitaires pour chaque étape du pipeline

## 🧪 Exemples de Résultats LLM
✅ Taux de conformité : 94,8% (+2,1%)
🚨 47 anomalies détectées :
 - Quantités incohérentes : 21
 - Valeurs manquantes : 18
 - Outliers : 8

## 📈 Recommandation :
 - Revoir les processus de saisie pour les produits à forte valeur
 - Implémenter des seuils automatiques pour les quantités critiques

## 🧑‍💻 Auteur

👤 Wassim Elmoufakkir

💼 Linkedin : (https://www.linkedin.com/in/wassim-elmoufakkir/)

💻 GitHub : @swz-json

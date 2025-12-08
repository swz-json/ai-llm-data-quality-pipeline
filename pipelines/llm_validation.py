import pandas as pd
import json
from pathlib import Path
from openai import OpenAI

VALIDATED_DIR = Path("data/validated")
VALIDATED_DIR.mkdir(parents=True, exist_ok=True)

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def detect_anomalies(df: pd.DataFrame) -> dict:
    anomalies = {}

    # Valeurs manquantes
    missing = df.isna().sum()
    anomalies["missing_values"] = missing[missing > 0].to_dict()

    # Quantités suspectes
    anomalies["quantite_suspecte"] = df[df["quantité"] <= 0].to_dict("records")

    # Totals négatifs
    anomalies["totaux_negatifs"] = df[df["total"] < 0].to_dict("records")

    # Dates manquantes
    anomalies["dates_invalides"] = df[df["datecommande"].isna()].to_dict("records")

    return anomalies

from openai import OpenAI, OpenAIError   # en haut

def llm_analyze(anomalies: dict) -> str:
    prompt = f"""
    Tu es un expert data. J'ai analysé un dataset e-commerce et trouvé ces anomalies :

    {json.dumps(anomalies, indent=2)}

    Explique-moi :
    - Quelles anomalies sont graves
    - Pourquoi elles peuvent poser problème business
    - Comment les corriger dans un pipeline ETL
    - Que recommanderais-tu pour améliorer la qualité des données
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tu es expert en data quality et data engineering."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        # Mode mock si quota / clé / réseau bloque
        print(f"⚠️ Impossible d'appeler le LLM (mode mock activé) : {e}")
        return (
            "Simulated LLM report:\n"
            "- Some quantities are suspicious (0 or negative).\n"
            "- Negative totals should be corrected or filtered.\n"
            "- Missing dates make it hard to analyse sales over time.\n"
            "- In a real pipeline, enforce constraints at source and add validation rules."
        )


def validate_with_llm(df: pd.DataFrame, name="commandes_report.json"):
    anomalies = detect_anomalies(df)
    llm_report = llm_analyze(anomalies)

    result = {
        "anomalies_detected": anomalies,
        "llm_analysis": llm_report
    }

    path = VALIDATED_DIR / name
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f" Rapport LLM sauvegardé : {path}")

from openai import OpenAI
import os

key = os.getenv("OPENAI_API_KEY")
print("KEY SEEN BY PYTHON:", key)

if not key:
    print("❌ Aucune clé trouvée, arrêt du test.")
else:
    client = OpenAI(api_key=key)
    print("✅ Import OpenAI OK, clé détectée.")

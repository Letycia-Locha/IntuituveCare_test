from flask import Flask, request, jsonify
import pandas as pd
from unidecode import unidecode
import os

app = Flask(__name__)

# Caminho relativo para o CSV
csv_path = os.path.join("..", "..", "banco_de_dados", "operadoras", "Relatorio_cadop.csv")
df = pd.read_csv(csv_path, sep=";", encoding="utf-8")

# Normaliza o nome para facilitar buscas
df["NOME_NORMALIZADO"] = df["Nome_Fantasia"].astype(str).apply(lambda x: unidecode(x.lower()))

@app.route("/buscar-operadora")
def buscar_operadora():
    query = request.args.get("query", "")
    query = unidecode(query.lower().replace("_", " "))  # ← AQUI está a mudança!
    
    resultados = df[df["NOME_NORMALIZADO"].str.contains(query, na=False)].head(10)
    return jsonify(resultados.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
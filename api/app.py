from flask import Flask, jsonify
from pathlib import Path
import pandas as pd

app = Flask(__name__)
DATA_DIR = Path(__file__).resolve().parents[1] / "data"


@app.route("/users", methods=["GET"])
def get_users():
    file_path = DATA_DIR / "users_transformed.csv"
    if not file_path.exists():
        return jsonify({"error": "Arquivo users_transformed.csv não encontrado. Rode a ETL primeiro."}), 404

    df = pd.read_csv(file_path)
    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)

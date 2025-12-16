import os
import json
from typing import Dict
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = """
Você é um assistente de marketing para uma plataforma de cursos de tecnologia.
Dado o perfil de um usuário (nome, email, cidade), crie:
- Um resumo do perfil (profile_summary).
- Uma recomendação de trilha de estudos (learning_path).
Retorne SEMPRE um JSON com os campos: profile_summary, learning_path.
Responda sempre em português do Brasil.
"""

def generate_profile_for_user(user: Dict) -> Dict:
    name = user.get("name")
    email = user.get("email")
    username = user.get("username")

    address = user.get("address")
    city = None
    if isinstance(address, dict):
        city = address.get("city")

    user_prompt = f"""
    Gere informações para o seguinte usuário:

    Nome: {name}
    Username: {username}
    Email: {email}
    Cidade: {city}

    Regras:
    - profile_summary: no máximo 2 parágrafos curtos.
    - learning_path: sugestão objetiva de trilha (ex: Backend Java, Dados com Python, Frontend React, etc.).
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content
    data = json.loads(content)

    return {
        "profile_summary": data.get("profile_summary"),
        "learning_path": data.get("learning_path")
    }

def transform_users(df: pd.DataFrame) -> pd.DataFrame:
    transformed_rows = []

    for _, row in df.iterrows():
        user = row.to_dict()
        ai_data = generate_profile_for_user(user)
        transformed_rows.append({
            **user,
            **ai_data
        })

    return pd.DataFrame(transformed_rows)

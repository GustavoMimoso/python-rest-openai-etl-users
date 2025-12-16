import requests
import pandas as pd

JSONPLACEHOLDER_USERS_URL = "https://jsonplaceholder.typicode.com/users"

def extract_users_from_api() -> pd.DataFrame:
    """
    Extrai usuarios da api JsonplaceHolder e retorna um Dataframe
    """
    response = requests.get(JSONPLACEHOLDER_USERS_URL, timeout=10)
    response.raise_for_status()
    users = response.json()
    df = pd.DataFrame(users)
    return df
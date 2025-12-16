from etl.extract import extract_users_from_api
from etl.transform import transform_users
from etl.load import load_to_csv


def run_etl():
    print("Extraindo usuários da API externa...")
    df_raw = extract_users_from_api()

    print("Transformando usuários com OpenAI...")
    df_transformed = transform_users(df_raw)

    print("Carregando dados transformados para CSV...")
    load_to_csv(df_transformed)

    print("Pipeline ETL com API externa concluída com sucesso!")


if __name__ == "__main__":
    run_etl()

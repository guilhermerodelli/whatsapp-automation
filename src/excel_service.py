import pandas as pd


def carregar_motoristas(caminho_arquivo):

    df = pd.read_excel(caminho_arquivo)

    return df.to_dict(orient="records")
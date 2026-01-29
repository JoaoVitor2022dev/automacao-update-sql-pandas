from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

caminho = os.getenv("CAMINHO").replace('"', '')
database = os.getenv("SQL_DATABASE")
conection = os.getenv("CONECTION").replace('"', '')

engine = create_engine(conection)

df_rcs = pd.read_csv(caminho, sep=';', encoding='utf-8')

df_rcs = df_rcs[['Pessoa_Cpf']].copy()

df_rcs['Validação'] = "SMS ENVIADO"


with engine.begin() as conn:
    for index, linha in df_rcs.iterrows():
        query = text(f"""
            UPDATE {database} 
            SET [Situacao_Nome_Da_Situacao] = :validacao 
            WHERE [Pessoa_Cpf] = :cpf
        """)
        
        conn.execute(query, {
            "validacao": linha['Validação'],
            "cpf": linha['Pessoa_Cpf']
        })

print("Update concluído com sucesso!")
import pandas as pd
# Criando um DataFrame a partir de um dicionário
dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Manuel"],
    "Idade": [23, 34, 29, 20],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Luanda"]
}

df = pd.DataFrame(dados)
print(df)
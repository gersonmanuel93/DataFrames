import pandas as pd
# Criando um DataFrame a partir de um dicionário
dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 34, 29],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(dados)
print(df)

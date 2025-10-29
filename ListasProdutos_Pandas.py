import pandas as pd

Produtos = [
	{"Nome": "IPad", "Preco": 1200, "Quantidade": 500},
	{"Nome": "IPhone", "Preco": 800, "Quantidade": 1000},
	{"Nome": "Airpod", "Preco": 3000, "Quantidade": 800},
	{"Nome": "Applewatch", "Preco": 4000, "Quantidade": 300},
	{"Nome": "MacBook", "Preco": 15000, "Quantidade": 300}
]


#Teste para imprimir uma parte de cada vez:
tb_produtos = pd.DataFrame(Produtos)
# print(tb_produtos)

# tb_produtos["Faturamento_Total"] = (tb_produtos["Preco"] * tb_produtos["Quantidade"])
#print(tb_produtos)


# Define uma função para aplicar desconto com base na quantidade
# Define a function to apply discount based on Quantity
def aplica_desconto(row):
  if row['Quantidade'] > 500:  # Condição de desconto: se a quantidae for > 500
                                # condition: discount if Quantity > 500
    return row['Preco'] * 0.10 # Desconto de 10% - 10% discount
  else:
    return 0  # Não recebe desconto - No discount

# Aplicar a função para criar uma nova coluna "Desconto"
# Apply the function to create a new 'Desconto' column
tb_produtos['Desconto'] = tb_produtos.apply(aplica_desconto, axis=1)

# Aplicação do desconto no faturamento total
# Update the 'Faturamento_Total' to reflect the discount
tb_produtos['Faturamento_Total_com_Desconto'] = (tb_produtos['Preco'] - tb_produtos['Desconto']) * tb_produtos['Quantidade']

print(tb_produtos)
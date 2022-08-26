# https://pages.hashtagtreinamentos.com/minicurso-python-automacao-obrigado
# Minicurso Python

import pandas as pd

# importar a base de dados
tabela_vendas = pd.read_excel("anexos/Minicurso_de_Automacao/Vendas.xlsx")

# visualizar a base de dados
pd.set_option('display.max_columns', None)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
faturamento = faturamento.rename(columns={'Valor Final':'Faturamento'})

# quantidade de produtos vendido por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# ticket médio por produto em cada loja
tiket_medio = (faturamento['Faturamento'] / quantidade['Quantidade']).to_frame()
tiket_medio = tiket_medio.rename(columns={0:'Tiket Médio'})

# enviar um email com o relatório


#print(tiket_medio)
display(faturamento)
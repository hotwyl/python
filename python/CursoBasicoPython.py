# https://www.youtube.com/playlist?list=PLpdAy0tYrnKyCZsE-ifaLV1xnkXBE9n7T
# Curso de Python

#logica de programação

#passo 0 - Entender os desafio que você quer resolver

#passo 1 - Percorrer todos os arquivos da pasta base de dados ( Pasta Vendas )
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("/content/drive/MyDrive/01-20 - Curso de Python - Aula 2/Vendas")
tabela_total = pd.DataFrame()

#passo 2 - Importar as bases de dados vendas
for arquivo in lista_arquivo:
  #se tem "vendas" no nome do arquivo então:
  if "vendas"  in arquivo.lower():
    # importar o arquivo
    tabela = pd.read_csv(f"/content/drive/MyDrive/01-20 - Curso de Python - Aula 2/Vendas/{arquivo}")
    tabela_total = tabela_total.append(tabela)

#passo 3 - Tratar / compilar as bases de dados
#display(tabela_total)

#passo 4 - Calcular o produto mais vendido ( em quantidade )
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
#display(tabela_produtos)

#passo 5 - Calcular o produto que mais faturou ( em faturamento )
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida']*tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
#display(tabela_faturamento)

#passo 6 - calcular a loja/cidade que mais vendeu ( em faturamento ) - criar um gráfico/deshboard
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
#display(tabela_lojas)

#grafico

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()
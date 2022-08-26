# Como Ler Tabelas em PDF Usando o Python [Extrair Tabelas de um Arquivo PDF]
# https://www.youtube.com/watch?v=8eNxZI-3Bxs&t=961s

#from tabula import read_pdf
#from tabulate import tabulate

import PyPDF2
import tabula as tb
import pandas as pd

#leitura do arquivo para pegar todas as paginas
file = 'anexos/pdf/Food Calories List.pdf'

pdf_file = open(file,'rb')

dados_do_pdf = PyPDF2.PdfReader(pdf_file)

pagina1 = dados_do_pdf.getPage(0)

texto_da_pagina1 = pagina1.extractText()

print(texto_da_pagina1)

#totalPaginas = tb.read_pdf(file, pages='all')
#print('inicio')

#tabela = read_pdf(file,pages="all")
#extrate_tabela = tabulate(tabela)
#print(extrate_tabela)

#display(tabela)
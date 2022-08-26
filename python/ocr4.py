# Como Ler Arquivo PDF, Como Mesclar (merge) arquivos PDF, PDF para Texto com Python , PyPDF2
# https://www.youtube.com/watch?v=MRmqMRLleK

import PyPDF2

#abrindo arquivo em modo binario e leitura
arq1 = open('anexos/pdf/Exemplo-de-PDF1.pdf','rb')
arq2 = open('anexos/pdf/Exemplo-de-PDF2.pdf','rb')
arq3 = open('anexos/pdf/Exemplo-de-PDF3.pdf','rb')

#lendo os dados do binario de PDF
dados_do_arq1 = PyPDF2.PdfReader(arq1)
dados_do_arq2 = PyPDF2.PdfReader(arq2)
dados_do_arq3 = PyPDF2.PdfReader(arq3)

#declarando um objeto do tiupo merge
merge = PyPDF2.PdfMerger()

#dando appende no Marge dos meus dados de pdf
merge.append(dados_do_arq1)
merge.append(dados_do_arq2)
merge.append(dados_do_arq3)

#escrevendo o novo arquivo pdf!
merge.write('anexos/export/ArqSaidaMargiado.pdf')
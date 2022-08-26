# Como Ler Arquivo PDF, Como Mesclar (merge) arquivos PDF, PDF para Texto com Python , PyPDF2
# https://www.youtube.com/watch?v=MRmqMRLleK

import PyPDF2

#abrindo arquivo em modo leitura e lendo o binario
pdf_file = open('anexos/pdf/texto.pdf','rb')

#após pegar o binario, pegamos os dados de PDF desse Binário
dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)

print('Números de paginas: ' + str(dados_do_pdf.numPages))

# setando a variave pagina1 com o objeto pagina1
pagina1 = dados_do_pdf.getPage(0)

#pegando o texto estraido da pagina1
texto_da_pagina1 = pagina1.extractText()

print(texto_da_pagina1)
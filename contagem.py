import os

def contar_arquivos_por_pasta(diretorio):

    contagem_por_pasta = {}

    for pasta_atual, _, arquivos in os.walk(diretorio):

        num_arquivos = len(arquivos)
        contagem_por_pasta[pasta_atual] = num_arquivos

    return contagem_por_pasta


caminho_diretorio = r'XXX'

contagem_arquivos = contar_arquivos_por_pasta(caminho_diretorio)

for pasta, num_arquivos in contagem_arquivos.items():
    print(f'A pasta {pasta} contém {num_arquivos} arquivo(s).')

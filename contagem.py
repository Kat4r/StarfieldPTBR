import os

def contar_arquivos_por_pasta(diretorio):
    # Inicializa um dicionário para armazenar o número de arquivos em cada pasta
    contagem_por_pasta = {}

    # Percorre o diretório e suas subpastas
    for pasta_atual, _, arquivos in os.walk(diretorio):
        # Obtém o número de arquivos na pasta atual
        num_arquivos = len(arquivos)

        # Armazena a contagem no dicionário
        contagem_por_pasta[pasta_atual] = num_arquivos

    return contagem_por_pasta


caminho_diretorio = r'E:\Área de Trabalho\Projeto Dublagem Starfield\Audios\sound\voice\starfield.esm'

# Obtém a contagem de arquivos por pasta
contagem_arquivos = contar_arquivos_por_pasta(caminho_diretorio)

# Exibe os resultados
for pasta, num_arquivos in contagem_arquivos.items():
    print(f'A pasta {pasta} contém {num_arquivos} arquivo(s).')

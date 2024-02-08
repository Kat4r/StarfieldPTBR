import os

def contar_linhas_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return sum(1 for linha in f)

def contar_linhas_txts(diretorio):
    total_linhas = 0
    for pasta_raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                caminho_arquivo = os.path.join(pasta_raiz, arquivo)
                linhas = contar_linhas_arquivo(caminho_arquivo)
                print(f"O arquivo {arquivo} tem {linhas} linhas.")
                total_linhas += linhas
    print(f"\nO total de linhas em todos os arquivos TXT é: {total_linhas}")

diretorio = "E:\Área de Trabalho\Projeto Dublagem Starfield\legendas"
contar_linhas_txts(diretorio)

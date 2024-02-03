import os

def ler_txt(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    return linhas

def verificar_e_criar_txt(txt_linhas, pasta_arquivos):
    frases_nao_encontradas = []

    for linha in txt_linhas:
        codigo = linha.split('*')[1].strip()
        nome_arquivo = f"{codigo}.wem"

        if not os.path.exists(os.path.join(pasta_arquivos, nome_arquivo)):
            frases_nao_encontradas.append(linha)

    if frases_nao_encontradas:
        with open('frases_nao_encontradas.txt', 'w', encoding='utf-8') as file:
            file.writelines(frases_nao_encontradas)
        print("Arquivo 'frases_nao_encontradas.txt' criado com sucesso.")
    else:
        print("Todos os códigos foram encontrados nos arquivos.")

if __name__ == "__main__":
    pasta_arquivos = "XXX"
    arquivo_txt = "emprod.txt"

    if os.path.exists(pasta_arquivos) and os.path.exists(arquivo_txt):
        linhas_txt = ler_txt(arquivo_txt)
        verificar_e_criar_txt(linhas_txt, pasta_arquivos)
    else:
        print("Certifique-se de fornecer caminhos válidos para a pasta de arquivos e o arquivo txt.")

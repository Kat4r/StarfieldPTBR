import os

def listar_arquivos_em_pasta(pasta):
    try:
        # Verifica se o diretório existe
        if not os.path.exists(pasta):
            raise FileNotFoundError(f'A pasta "{pasta}" não existe.')

        # Lista de arquivos na pasta
        arquivos = os.listdir(pasta)

        # Caminho completo para cada arquivo na pasta
        caminhos_arquivos = [os.path.join(pasta, arquivo) for arquivo in arquivos]

        return caminhos_arquivos
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def escrever_arquivos_em_txt(arquivos, nome_arquivo_saida):
    try:
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            for arquivo in arquivos:
                arquivo_saida.write(f"{arquivo}\n")
        print(f"Arquivos listados e escritos em '{nome_arquivo_saida}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever o arquivo: {e}")

if __name__ == "__main__":
    # Defina o diretório que deseja listar
    pasta = "E:\\Area de Trabalho\\projeto dub glados\\balbuço"
    # Lista os arquivos na pasta
    arquivos = listar_arquivos_em_pasta(pasta)

    # Nome do arquivo de saída
    nome_arquivo_saida = "lista_de_arquivos.txt"

    # Escreve os arquivos em um arquivo de texto
    escrever_arquivos_em_txt(arquivos, nome_arquivo_saida)

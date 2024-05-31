def remover_linhas_none_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()  # Lê todas as linhas do arquivo

    # Filtra as linhas que não começam com as strings especificadas
    strings_para_remover = ('None')
    linhas_filtradas = [linha for linha in linhas if not linha.startswith(strings_para_remover)]

    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.writelines(linhas_filtradas)  # Escreve as linhas filtradas de volta para o arquivo de saída

if __name__ == "__main__":
    arquivo_entrada = 'D:\\Meus Códigos\\Dub Starfield\\Textos\\emprod.txt'
    arquivo_saida = 'D:\\Meus Códigos\\Dub Starfield\\Textos\\emprod.txt'

    remover_linhas_none_arquivo(arquivo_entrada, arquivo_saida)
    print("Linhas indesejadas foram removidas do arquivo.")
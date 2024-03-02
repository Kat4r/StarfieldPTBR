import os


def listar_nomes_pastas(diretorio, arquivo_saida):
    try:
        nomes_pastas = [nome for nome in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, nome))]

        with open(arquivo_saida, 'w', encoding='utf-8') as file:
            file.writelines('\n'.join(nomes_pastas))

        print(f'Nomes das pastas foram gravados em {arquivo_saida}')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')


# Substitua o caminho do diretório pela pasta que você deseja listar
diretorio_a_listar = 'C:\\Users\\vini_\\OneDrive\\Documentos\\My Games\\Starfield\\Data\\Sound\\voice\\starfield.esm'
arquivo_saida = 'nomes_pastas.txt'

listar_nomes_pastas(diretorio_a_listar, arquivo_saida)

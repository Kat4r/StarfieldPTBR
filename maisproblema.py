def ler_arquivo_como_set(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return {linha.strip() for linha in arquivo.readlines()}

arquivo_diferencas = 'diferencas_entre_arquivos.txt'
arquivo_legenda_codigo = 'arquivo_bruto_com_legendas.txt'
arquivo_atualizado = 'arquivo_atualizado.txt'

diferencas = ler_arquivo_como_set(arquivo_diferencas)

with open(arquivo_legenda_codigo, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    linhas_atualizadas = [linha.strip() + '\n' for linha in linhas if any(codigo in linha for codigo in diferencas)]

with open(arquivo_atualizado, 'w', encoding='utf-8') as arquivo:
    arquivo.writelines(linhas_atualizadas)

print(f'O arquivo foi atualizado com as legendas correspondentes aos códigos encontrados em {arquivo_atualizado}')

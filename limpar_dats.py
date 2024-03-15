import os

def listar_arquivos_sem_extensao_wem(diretorio):
    arquivos_nao_wem = []
    for pasta_raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if not arquivo.endswith(".wem"):
                arquivos_nao_wem.append(os.path.join(pasta_raiz, arquivo))
    return arquivos_nao_wem

def excluir_arquivos(arquivos):
    for arquivo in arquivos:
        try:
            os.remove(arquivo)
            print(f"Arquivo '{arquivo}' excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir o arquivo '{arquivo}': {e}")

diretorio_principal = os.path.normpath(r"C:\Users\vini_\OneDrive\Documentos\My Games\Starfield\Data\Sound\voice")

if os.path.isdir(diretorio_principal):
    arquivos_sem_wem = listar_arquivos_sem_extensao_wem(diretorio_principal)
    if arquivos_sem_wem:
        print("Arquivos encontrados que não são .wem:")
        for arquivo in arquivos_sem_wem:
            print(arquivo)
        confirmacao = input("Deseja excluir esses arquivos? (s/n): ")
        if confirmacao.lower() == "s":
            excluir_arquivos(arquivos_sem_wem)
        else:
            print("Operação cancelada.")
    else:
        print("Não foram encontrados arquivos que não são .wem.")
else:
    print("O caminho fornecido não é um diretório válido.")

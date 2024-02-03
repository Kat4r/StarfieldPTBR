import os
import shutil

diretorio_dublados = "XXX"
diretorio_faltando = "XXX"
diretorio_destino = "XXX"


arquivos_dublados = set(os.listdir(diretorio_dublados))
arquivos_faltando = set(os.listdir(diretorio_faltando))
arquivos_a_serem_dublados = arquivos_faltando - arquivos_dublados


for arquivo in arquivos_a_serem_dublados:
    caminho_origem = os.path.join(diretorio_faltando, arquivo)
    caminho_destino = os.path.join(diretorio_destino, arquivo)
    shutil.move(caminho_origem, caminho_destino)

print(f"Arquivos movidos para a pasta de destino: {arquivos_a_serem_dublados}")

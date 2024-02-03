import os
import shutil

diretorio_dublados = "E:\Área de Trabalho\Projeto Dublagem Starfield\Dublados/npcmwalterstroud"
diretorio_faltando = "E:\Área de Trabalho\Projeto Dublagem Starfield\Em ingles/npcmwalterstroud"
diretorio_destino = "E:/Área de Trabalho/Projeto Dublagem Starfield/Falta"


arquivos_dublados = set(os.listdir(diretorio_dublados))
arquivos_faltando = set(os.listdir(diretorio_faltando))
arquivos_a_serem_dublados = arquivos_faltando - arquivos_dublados


for arquivo in arquivos_a_serem_dublados:
    caminho_origem = os.path.join(diretorio_faltando, arquivo)
    caminho_destino = os.path.join(diretorio_destino, arquivo)
    shutil.move(caminho_origem, caminho_destino)

print(f"Arquivos movidos para a pasta de destino: {arquivos_a_serem_dublados}")

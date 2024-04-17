import os
import shutil

diretorio_dublados = "H:\SteamLibrary\steamapps\common\Portal\portal\sound\\vo\\aperture_ai"
diretorio_faltando = "E:\Area de Trabalho\projeto dub glados\Glados"
diretorio_destino = "E:\Meus Códigos\Dub Starfield\Textos"


arquivos_dublados = set(os.listdir(diretorio_dublados))
arquivos_faltando = set(os.listdir(diretorio_faltando))
arquivos_a_serem_dublados = arquivos_faltando - arquivos_dublados


for arquivo in arquivos_a_serem_dublados:
    caminho_origem = os.path.join(diretorio_faltando, arquivo)
    caminho_destino = os.path.join(diretorio_destino, arquivo)
    shutil.move(caminho_origem, caminho_destino)

print(f"Arquivos movidos para a pasta de destino: {arquivos_a_serem_dublados}")

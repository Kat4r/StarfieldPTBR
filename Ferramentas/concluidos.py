import os
import shutil

# Definindo os caminhos das pastas
pasta_final = r'C:\Users\vini_\OneDrive\Documentos\My Games\Starfield\Data\Sound\voice\starfield.esm'
pasta_legendas = r'D:\Area de Trabalho\Projeto Dublagem Starfield\legendas'
pasta_restantes = r'D:\Area de Trabalho\Projeto Dublagem Starfield\legendas_restantes'

# Criar a pasta para os arquivos restantes se não existir
os.makedirs(pasta_restantes, exist_ok=True)

# Obter a lista de arquivos na pasta final e na pasta de legendas
arquivos_final = set(os.listdir(pasta_final))
arquivos_legendas = os.listdir(pasta_legendas)

# Mover arquivos que não estão na pasta final para a pasta restantes
for arquivo in arquivos_legendas:
    if arquivo not in arquivos_final:
        src_path = os.path.join(pasta_legendas, arquivo)
        dst_path = os.path.join(pasta_restantes, arquivo)
        shutil.move(src_path, dst_path)
        print(f'Movido: {arquivo}')

print('Movimentação de arquivos concluída.')
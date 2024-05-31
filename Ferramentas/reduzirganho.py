from pydub import AudioSegment
import os

diretorio_audios = 'D:\\Area de Trabalho\\Projeto Dublagem Starfield\\Dublados\\WEM'
output_dir = 'D:\\Area de Trabalho\\Projeto Dublagem Starfield\\Dublados\\WEM'

# Verifica se o diretório de saída existe, se não, cria-o
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Percorre todas as pastas e subpastas
for root, dirs, files in os.walk(diretorio_audios):
    for arquivo in files:
        if arquivo.endswith(
                ('.wav', '.mp3', '.flac', '.ogg', '.aac')):  # Adapte as extensões de acordo com seus arquivos
            caminho_completo = os.path.join(root, arquivo)
            audio = AudioSegment.from_file(caminho_completo)
            audio = audio - 8

            # Cria o caminho correspondente no diretório de saída
            relative_path = os.path.relpath(root, diretorio_audios)
            output_path = os.path.join(output_dir, relative_path)

            # Verifica se o diretório de saída específico existe, se não, cria-o
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # Exporta o arquivo com o ganho reduzido
            audio.export(os.path.join(output_path, arquivo), format="wav")

print("Processamento concluído.")

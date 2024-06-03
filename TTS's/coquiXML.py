import os
import torch
from TTS.api import TTS
from time import sleep
from pydub import AudioSegment
import xml.etree.ElementTree as ET  # Importa o módulo ElementTree para trabalhar com XML

diretorio_textos = "C:\\Projects\\Dublagens\\Starfield\\Textos\\"
diretorio_saidas = "C:\\Projects\\Dublagens\\Starfield\\Dublado\\"
diretorio_audios_producao = "C:\\Projects\\Dublagens\\Starfield\\Dublando\\"

# Configuração do dispositivo
device = "cuda" if torch.cuda.is_available() else "cpu"

# Inicializa o modelo TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

tts.to(device)


# Função para diminuir o volume do áudio em 8 decibéis
def diminuir_volume(caminho_arquivo_audio):
    audio = AudioSegment.from_file(caminho_arquivo_audio)
    audio = audio - 6  # Reduz o volume em 6 decibéis
    audio.export(caminho_arquivo_audio, format="ogg")


def verificar_arquivo(caminho):
    if os.path.isfile(caminho):
        return True
    else:
        print(f"Arquivo não encontrado: {caminho}")
        return False


# Processa os arquivos de texto no diretório diretorio_textos
i = 0
for arquivo_txt in os.listdir(diretorio_textos):
    if arquivo_txt.endswith(".xml"):
        caminho_arquivo_txt = os.path.join(diretorio_textos, arquivo_txt)

        # Parsing do arquivo XML para obter o texto da tag <Dest>
        tree = ET.parse(caminho_arquivo_txt)
        root = tree.getroot()

        # Iterar sobre os subdiretórios em diretorio_audios_producao
        for subdir, dirs, files in os.walk(diretorio_audios_producao):
            for file in files:
                if file.endswith(".ogg"):
                    caminho_arquivo_ogg = os.path.join(subdir, file)

                    # Obtendo o nome do arquivo .wem correspondente ao arquivo .ogg
                    nome_arquivo_wem = os.path.splitext(file)[0] + ".wem"

                    # Buscando o texto equivalente na tag <Dest> do arquivo XML
                    texto_dest = None
                    for string_tag in root.findall('.//String'):
                        fuz_tag = string_tag.find('.//Fuz')
                        if fuz_tag is not None and fuz_tag.text.endswith(nome_arquivo_wem):
                            dest_tag = string_tag.find('Dest')
                            if dest_tag is not None:
                                texto_dest = dest_tag.text
                                break

                    # Se encontrou o texto equivalente, seguir com o processamento
                    if texto_dest is not None:
                        # Ignorar o processo se o texto iniciar com "*"
                        if texto_dest.startswith("*"):
                            print(f"Ignorado: {texto_dest}")
                            continue

                        texto_dest = texto_dest.replace('.', ',')
                        # Criar o subdiretório correspondente em diretorio_saidas
                        subdir_relativo = os.path.relpath(subdir, diretorio_audios_producao)
                        caminho_subdiretorio_saida = os.path.join(diretorio_saidas, subdir_relativo)
                        os.makedirs(caminho_subdiretorio_saida, exist_ok=True)

                        # Caminho do arquivo de saída
                        caminho_arquivo_audio = os.path.join(caminho_subdiretorio_saida, file)
                        while True:
                            try:
                                # Gera e salva a síntese de voz usando o Coqui TTS
                                tts.tts_to_file(text=texto_dest, speaker_wav=caminho_arquivo_ogg, language="pt",
                                                speed=1.3, file_path=caminho_arquivo_audio, emotion='neutral')
                                i += 1
                                caminho_arquivo_audio = caminho_arquivo_audio.replace("\\", "/")
                                diminuir_volume(caminho_arquivo_audio)  # Aplica a redução de volume
                                print(f"Já foram dublados {i} áudios.")
                                break
                            except Exception as erro:
                                print(f"Erro ao gerar áudio: {erro}")
                                continue

print("Processamento concluído.")
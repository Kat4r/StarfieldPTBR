import os
import torch
from TTS.api import TTS
from time import sleep
import logging

device = "cuda" if torch.cuda.is_available() else "cpu"

logging.basicConfig(level=logging.ERROR)

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts.to(device)

# Diretórios de entrada e saída
diretorio_textos = "D:\\Meus Códigos\\Dub Starfield\\Textos"
diretorio_saidas = "D:\\Area de Trabalho\\Projeto Dublagem Starfield\\Dublados\\WEM\\crimsonfleetfemale02\\"
diretorio_audios_producao = "D:\\Area de Trabalho\\Projeto Dublagem Starfield\\em produção\\crimsonfleetfemale02\\"

def verificar_arquivo(caminho):
    if os.path.isfile(caminho):
        return True
    else:
        print(f"Arquivo não encontrado: {caminho}")
        return False

# Cria o diretório de saída se não existir
os.makedirs(diretorio_saidas, exist_ok=True)

# Processa os arquivos de texto
i = 0
for arquivo in os.listdir(diretorio_textos):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(diretorio_textos, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()

        for linha in linhas:
            # Verifica se a linha contém mais de um asterisco ou contém 'None'
            if linha.count('*') != 1 or 'None' in linha:
                print(f"{linha.strip()}: ignorada.")
                continue

        for linha in linhas:
            partes = linha.split("*")

            if len(partes) >= 2:
                texto = partes[0].strip().replace('.', ',')
                codigo_arquivo = partes[1].strip().replace(".wem", "")
                caminho_voz = f"{diretorio_audios_producao}{codigo_arquivo}.ogg"

                if verificar_arquivo(caminho_voz):
                    while True:
                        try:
                            caminho_audio = f"{diretorio_saidas}{codigo_arquivo}.wav"
                            tts.tts_to_file(text=texto, speaker_wav=caminho_voz, language="pt", file_path=caminho_audio, emotion='neutral')
                            i += 1
                            print(f"Já foram dublados {i} áudios, restam {len(linhas) - i}.")
                            break
                        except Exception as erro:
                            print(f"Erro ao gerar áudio: {erro}")
                            break

print('Processamento concluído.')

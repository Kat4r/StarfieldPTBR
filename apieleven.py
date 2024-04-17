#Onde a dublagem acontece

import os
import requests
from gtts import gTTS
i = 0

API_KEY = "119c1ba95e120c491c1ba3cb08fbf747"
URL = "https://api.elevenlabs.io/v1/text-to-speech/n7k4ucAvjQ3hsiXOF449"
diretorio_textos = "E:\Meus Códigos\Dub Starfield\Textos"

def get_eleven_tts(text):
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.40,
            "similarity_boost": 0.75,
            "style": 0.25
        }
    }

    response = requests.post(URL, json=data, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print(f"Erro na solicitação TTS: {response.text}")
        print(f"Foram dublados {i} audios")
        exit()

for arquivo in os.listdir(diretorio_textos):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(diretorio_textos, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()

        for linha in linhas:
            partes = linha.split("*")

            if len(partes) >= 2:
                texto = partes[0].strip()
                codigo_arquivo = partes[1].strip().replace(".wem", "")

                audio_data = get_eleven_tts(texto)

                if audio_data:
                    i += 1
                    caminho_audio = f"E:\Area de Trabalho\Projeto Dublagem Starfield\Dublados\WEM\\npcfhadrian/{codigo_arquivo}.mp3"
                    with open(caminho_audio, "wb") as audio_file:
                        audio_file.write(audio_data)

                    print(f" Já foram dublados {i} audios, restam {len(linhas) - i}.")
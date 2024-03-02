#Onde a dublagem acontece

import os
import requests
from gtts import gTTS
i = 0

API_KEY = "11543db9e9882ab6d2b908bc6d6da3a2"
URL = "https://api.elevenlabs.io/v1/text-to-speech/pBs3ZAmoL0NjRrk65kXJ"
diretorio_textos = "D:\Meus Códigos\Dub Starfield\Textos"

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
            "stability": 0.50,
            "similarity_boost": 0.70,
            "style": 0.30
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
                    caminho_audio = f"D:\Area de Trabalho\Projeto Dublagem Starfield\Dublados\WEM\\npcmjustinsnead/{codigo_arquivo}.mp3"
                    with open(caminho_audio, "wb") as audio_file:
                        audio_file.write(audio_data)

                    print(f" Já foram dublados {i} audios, restam {len(linhas) - i}.")
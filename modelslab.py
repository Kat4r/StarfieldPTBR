import os
import requests
import json
from pydub import AudioSegment
from time import sleep

i = 0

API_KEY = "qFkMinGRf7dlPz1iLkIOcH80OTLztQVkWbMJBpT06U1LwIyg8iviSeQnVx3h"
URL = "https://modelslab.com/api/v6/voice/text_to_audio"
diretorio_textos = "E:\Meus Códigos\Dub Starfield\Textos"

def gerar_link(caminho):

    u_url = "https://tmpfiles.org/api/v1/upload"

    arqs = {"file":  open(caminho, 'rb')}

    response = requests.post(u_url, files=arqs)

    if response.status_code == 200:
        return response.json()['data']['url']

    else:
        print("Erro ao gerar arquivo")



def get_modelslab_tts(text, voz):
    headers = {
        "Content-Type": "application/json",
    }

    data = json.dumps({
    "key": API_KEY,
    "prompt": text,
    "init_audio": voz,
    "language": "brazilian portuguese",
    "emotion": "neutral",
    "webhook": None,
    "track_id": None
    })

    response = requests.request("POST", URL, data=data, headers=headers)

    if response.status_code == 200:
        return response.content


    else:
        print(f"Erro na solicitação TTS: {response.text}")
        print(f"Foram dublados {i} áudios")
        exit()



for arquivo in os.listdir(diretorio_textos):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(diretorio_textos, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()

        for linha in linhas:
            partes = linha.split("*")

            if len(partes) >= 2:
                texto = partes[0].strip().replace('.',',')
                codigo_arquivo = partes[1].strip().replace(".wem", "")
                voz = gerar_link(f"E:\Area de Trabalho\Projeto Dublagem Starfield\em produção\\neonsecurityfemale01\\{codigo_arquivo}.wav")
                voz = voz.replace(".org/", ".org/dl/")
                audio_data = get_modelslab_tts(texto, voz=voz)
                audio_dict = eval(audio_data)
                audio_url = audio_dict['output'][0]
                audio_url = audio_url.replace("\\",'')

                caminho_audio = f"E:\Area de Trabalho\Projeto Dublagem Starfield\Dublados\WEM\\neonsecurityfemale01/{codigo_arquivo}.wav"

                while True:
                    try:
                        response = requests.get(audio_url)

                        if response.status_code == 200:
                            i += 1
                            with open(caminho_audio, 'wb') as file:
                                file.write(response.content)
                            print(f" Já foram dublados {i} áudios, restam {len(linhas) - i}.")
                            break

                    except:
                        print(f"Erro ao realizar o arquivo: {response.status_code}")
                        sleep(2)
                        continue



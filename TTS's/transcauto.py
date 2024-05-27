import os
import soundfile as sf

def verificar_codec_wem(caminho_arquivo):
    try:
        info = sf.info(caminho_arquivo)
        bitrate = info.bitrate  # Taxa de bits do arquivo
        codec = "Vorbis High Quality" if bitrate > 192000 else "Vorbis Standard Quality"
        return codec
    except Exception as e:
        return f"Erro ao ler arquivo: {e}"



def analisar_pasta_starfield(caminho_pasta):
    for pasta_atual, _, arquivos in os.walk(caminho_pasta):
        for arquivo in arquivos:
            if arquivo.endswith(".wem"):
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                codec = verificar_codec_wem(caminho_arquivo)
                print(f"Arquivo {arquivo}: {codec}")

# Caminho da pasta "starfield.esm"
caminho_pasta = "C:\\Users\\vini_\\OneDrive\\Documentos\\My Games\\Starfield\\Data\\Sound\\voice\\starfield.esm"

# Analisar os arquivos .wem dentro da pasta "starfield.esm"
analisar_pasta_starfield(caminho_pasta)

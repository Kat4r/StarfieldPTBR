from pydub import AudioSegment
import os


diretorio_audios = 'E:\Area de Trabalho\Projeto Dublagem Starfield\Dublados\WEM\\neonsecurityfemale01'

for arquivo in os.listdir(diretorio_audios):
    caminho_completo = os.path.join(diretorio_audios, arquivo)
    audio = AudioSegment.from_file(caminho_completo)
    audio = audio - 8
    audio.export(f"E:\Area de Trabalho\Projeto Dublagem Starfield\Dublados\WEM\menosgain\{arquivo}", format="wav")
import os
import torch
import whisper
from deep_translator import GoogleTranslator


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def transcAuto(pathPasta,nomeArq):
    model = whisper.load_model("medium")
    arquivos = os.listdir(pathPasta)
    i = len(arquivos)

    with open(nomeArq, "w", encoding="utf-8") as f:

        for arquivo in arquivos:
            i -= i
            resultado = model.transcribe(os.path.join(pathPasta, arquivo))
            #f.write(f"{resultado['text']}   {arquivo}\n\n") #resultado em ingles
            f.write(f"{GoogleTranslator(source='en', target='pt').translate(resultado['text'])}  *  {arquivo}\n") #resultado em portugues <<<
            print(f"linha escrita, restam {i}")
            #só colocar um # na frente de qual você escolher pra traduzir

caminho = 'E:\Área de Trabalho\Projeto Dublagem Starfield\Em ingles/npcfanyagriffon'.replace("\\","/")

transcAuto(caminho, os.path.basename(os.path.normpath(caminho)) + ".txt")
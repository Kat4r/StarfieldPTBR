# Caminhos para os arquivos
correto_txt_path = 'npcfsarahmorgan.txt'
incorreto_txt_path = 'npcfsarahmorganold.txt'
diferenca_txt_path = 'correcoes.txt'

import codecs
# Lê as linhas dos arquivos
with codecs.open(correto_txt_path, 'r', encoding='utf-8') as f:
    correto_lines = f.readlines()
with codecs.open(incorreto_txt_path, 'r', encoding='utf-8') as f:
    incorreto_lines = f.readlines()

# Encontra a diferença entre os dois conjuntos de linhas
diferenca_lines = set(correto_lines) - set(incorreto_lines)

# Escreve a diferença em um novo arquivo
with open(diferenca_txt_path, 'w', encoding='utf-8') as f:
    f.writelines(diferenca_lines)

print('Arquivo de diferença criado com sucesso.')
import codecs

correto_txt_path = 'xxx.txt'
incorreto_txt_path = 'xxx.txt'
diferenca_txt_path = 'XXX.txt'

with codecs.open(correto_txt_path, 'r', encoding='utf-8') as f:
    correto_lines = f.readlines()
with codecs.open(incorreto_txt_path, 'r', encoding='utf-8') as f:
    incorreto_lines = f.readlines()

diferenca_lines = set(correto_lines) - set(incorreto_lines)

with open(diferenca_txt_path, 'w', encoding='utf-8') as f:
    f.writelines(diferenca_lines)

print('Arquivo de diferença criado com sucesso.')
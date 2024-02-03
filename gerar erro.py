import os
import xml.etree.ElementTree as ET
import codecs

# Caminho para o arquivo XML
xml_file_path = 'tradu.xml'

# Parse do XML
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Diretório base onde todas as pastas devem estar
base_directory = 'E:\\Área de Trabalho\\Projeto Dublagem Starfield\\Legendasold'

# Dicionário para mapear cada personagem com suas pastas
character_folders = {}

# Itera sobre os elementos String no XML
for string_element in root.iter('String'):
    # Obtém o nome da pasta e o código
    fuz_element = string_element.find('FuzInfo/Fuz')
    if fuz_element is not None:
        fuz_text = fuz_element.text
        folder_name = fuz_text.split('\\')[-2]
        code = fuz_text.split('\\')[-1].split('.')[0]

        # Adiciona o texto em português ao dicionário associado ao personagem
        dest_text_pt = string_element.find('Dest').text
        if folder_name not in character_folders:
            character_folders[folder_name] = []
        character_folders[folder_name].append((f'{dest_text_pt} * {code}.wem\n'))

# Escreve os textos em português nos arquivos TXT dentro de cada pasta de personagem
for folder_name, texts in character_folders.items():
    folder_path = os.path.join(base_directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    txt_file_path = os.path.join(folder_path, f'{folder_name}.txt')
    with codecs.open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.writelines(texts)

print('Concluído!')

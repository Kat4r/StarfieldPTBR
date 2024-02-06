import os
import xml.etree.ElementTree as ET
import codecs


xml_file_path = 'tradu.xml'


tree = ET.parse(xml_file_path)
root = tree.getroot()
base_directory = 'E:\Área de Trabalho\Projeto Dublagem Starfield\legold'


character_folders = {}


for string_element in root.iter('String'):

    fuz_element = string_element.find('FuzInfo/Fuz')
    if fuz_element is not None:
        fuz_text = fuz_element.text
        folder_name = fuz_text.split('\\')[-2]
        code = fuz_text.split('\\')[-1].split('.')[0]
        dest_text_pt = string_element.find('Dest').text
        if folder_name not in character_folders:
            character_folders[folder_name] = []
        character_folders[folder_name].append((f'{dest_text_pt} * {code}.wem\n'))


for folder_name, texts in character_folders.items():
    folder_path = os.path.join(base_directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    txt_file_path = os.path.join(folder_path, f'{folder_name}.txt')
    with codecs.open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.writelines(texts)

print('Concluído!')

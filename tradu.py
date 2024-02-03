
import os
import xml.etree.ElementTree as ET
import codecs

xml_file_path = 'tradu.xml'

tree = ET.parse(xml_file_path)
root = tree.getroot()

base_directory = 'E:\Área de Trabalho\Projeto Dublagem Starfield\legpt'


for string_element in root.iter('String'):
    fuz_elements = string_element.findall('FuzInfo/Fuz')
    if fuz_elements is not None:
        for fuz_element in fuz_elements:
            fuz_text = fuz_element.text
            folder_name = fuz_text.split('\\')[-2]
            code = fuz_text.split('\\')[-1].split('.')[0]


            dest_text_pt = string_element.find('Dest').text

            directory_path = os.path.join(base_directory, folder_name)
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)


            txt_file_path = os.path.join(directory_path, f'{folder_name}.txt')
            with codecs.open(txt_file_path, 'a', encoding='utf-8') as txt_file:
                txt_file.write(f'{dest_text_pt} * {code}.wem\n')

print('Concluído!')

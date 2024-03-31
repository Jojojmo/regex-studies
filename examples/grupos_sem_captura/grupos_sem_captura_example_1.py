import re

document_list = [
'Maçã verde',
'Peira',
'Maçã',
'Kiwi',
'Maçã vermelha'
]

pattern = re.compile(r'Maçã\s(?:verde|vermelha)')

for document in document_list:
    match = pattern.match(document)
    if match:
        print(document)

#Maçã verde
#Maçã vermelha
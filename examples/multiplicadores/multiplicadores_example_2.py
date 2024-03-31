import re

document = "abbbbbccc"

pattern = re.compile(r'b{,3}')  # Procura por no máximo 3 letras 'b' em sequência
extract = pattern.findall(document)
print(extract)  # Saída: ['', 'bbb', 'bb', '', '', '', '']

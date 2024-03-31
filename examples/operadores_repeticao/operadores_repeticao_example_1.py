import re

document = "abcdeefg"

pattern = re.compile(r'e*')  # Procura por zero ou mais letras 'e' em sequência
extract = pattern.findall(document)
print(extract)  # Saída: ['', '', '', '', 'ee', '', '', '']
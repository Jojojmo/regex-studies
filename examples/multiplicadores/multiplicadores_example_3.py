import re

document = "xxyyzzz"

pattern = re.compile(r'z{2,3}')  # Procura por 2 a 3 letras 'z' em sequência
extract = pattern.findall(document)
print(extract)  # Saída: ['zzz']

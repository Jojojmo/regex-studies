import re

document = "Técnico-I, Enfermeiro, Engenheiro-III"

pattern = re.compile(r'[^,\s]+I')  # Procura por pelo menos um I e no máximo n
extract = pattern.findall(document)
print(extract)  # Saída: ['Técnico-I', 'Engenheiro-III']


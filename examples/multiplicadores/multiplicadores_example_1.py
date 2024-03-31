import re

document = "111222333"

pattern = re.compile(r'\d{3}')  # Procura por exatamente 3 dígitos em sequência
extract = pattern.findall(document)
print(extract)  # Saída: ['111', '222', '333']

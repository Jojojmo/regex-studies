import re

document = "alto aalto aaaaaalto lto"

pattern= re.compile(r'\ba?lto')  #Procura no minimo 0 e máximo 1 caractere "a" 

extract = pattern.findall(document)
print(extract)  # Saída: ['alto', 'lto']
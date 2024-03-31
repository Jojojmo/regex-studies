import re

document = "Este é um exemplo de busca de palavras com 'fronteira'"

pattern = re.compile(r'\bpalavras\b')  

extract = pattern.findall(document)
print(extract)  

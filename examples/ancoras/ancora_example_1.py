import re

document = """Olá, este é um exemplo de texto.
Ele demonstra como usar ^ para encontrar o início de uma linha.
"""

pattern = re.compile(r'^Olá')  
match = pattern.match(document)

if match:
    print(document)
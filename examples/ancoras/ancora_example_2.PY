import re

document = """
Este é um exemplo de texto.
Ele demonstra como usar $ para encontrar o final de uma linha."""

pattern = re.compile(r'linha.$')  
match = pattern.search(document)

if match:
    print(f'Indice do match: {match.span()}')
    print(f'Palavra com match: {match.group()}') 

import re

document= """
Cargo: Eletricista Pleno,
Cargo: Desenvolvedor de software Senior,
Cargo: CEO Alt-meios,
Cargo: Analista Junior,
Cargo: Padeiro 2 anos
"""

pattern = re.compile(r"Cargo:\s(.*Junior|.*Pleno|.*Senior)")

extract = re.findall(pattern,document)

print(extract)

#Saída:
#['Eletricista Pleno', 'Desenvolvedor de software Senior', 'Analista Junior']
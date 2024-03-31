import re

document= """
Primário Completo
Ensino-médio Completo
Empresa Junior
Superior Completo
Fundamentos do Python Feito
Pós-graduação Cursando
"""

pattern = re.compile(r"(.*)(Completo|Cursando)")

extract = re.findall(pattern,document)

print(extract)

#saída:
#[('Primário ', 'Completo'), ('Ensino-médio ', 'Completo'), ('Superior ', 'Completo'), ('Pós-graduação ', 'Cursando')]
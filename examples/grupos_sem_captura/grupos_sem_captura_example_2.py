import re

document= """
USD10.20
R$100.23
ARS756.30
JPY4.25
USD1.00
R$.22
"""

pattern = re.compile(r"(?:USD|R\$)\d+.\d{2}")

extract = re.findall(pattern,document)

print(extract)

#Saída:
#['USD10.20', 'R$100.23', 'USD1.00']
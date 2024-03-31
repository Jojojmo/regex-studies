import re

document = """"
Nota: 1
Nota: 2
Nota: 3
Nota: 4
Nota: 5
Nota: 6
Nota: 7
Nota: 8
Nota: 9
"""

pattern= re.compile(r"Nota: [^1-7]")

extract= re.findall(pattern,document)

print(extract)
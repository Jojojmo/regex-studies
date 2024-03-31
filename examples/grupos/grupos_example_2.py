import re

document= """
10/10/2022
12/30/1970
1970/02/01
2000-10-10
04/02/2024
"""

pattern = re.compile(r"(\d{2})\/(\d{2})\/(\d{4})")

extract = re.findall(pattern,document)

print(extract)

#Saída:
#[('10', '10', '2022'), ('12', '30', '1970'), ('04', '02', '2024')]
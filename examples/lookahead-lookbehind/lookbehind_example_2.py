import re

texto = """
10
-5
20
-15
"""

pattern = re.compile(r"(?<!-)\b\d+\b")

extract = re.findall(pattern, texto)

print(extract)

#Saída:
#['10', '20']
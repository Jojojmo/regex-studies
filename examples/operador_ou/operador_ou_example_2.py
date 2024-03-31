import re

document = """
eles foram na natação, já elas para faculdade.
Os amigos torceram para Pedro e ele ganhou uma medalha.
Ana estudou com as amigas e ela passou na matéria
"""

pattern = re.compile(r"el(?:a|e)s?")

extract =  re.findall(pattern,document)

print(extract)
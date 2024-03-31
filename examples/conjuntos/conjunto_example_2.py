import re

#Singular e plural

document = """"
Em minha juventude de atleta, já corri muito. Agora que sou pai, 
só corro quando meu filho corre de mim.
"""

pattern= re.compile(r'corr[eoi]')

extract= re.findall(pattern,document)

print(extract)
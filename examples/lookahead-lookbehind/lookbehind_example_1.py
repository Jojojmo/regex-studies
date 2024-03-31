import re

document= """
AMD Ryzen Threadripper Pro 5995WX
INTEL Core I3-13100F 4.5GHz. LGA 1700
AMD AM4 mATX DDR4
INTEL Arc A770 Phantom Gaming asRock, 16GB GDDR6
"""

pattern = re.compile(r"(?<=INTEL\s).+")

extract = re.findall(pattern,document)

print(extract)

#Saída:
#['Core I3-13100F 4.5GHz. LGA 1700', 'Arc A770 Phantom Gaming asRock, 16GB GDDR6']
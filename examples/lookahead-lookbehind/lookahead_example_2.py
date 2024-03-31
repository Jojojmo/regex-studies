import re

#Nome científico de algumas corujas brasileiras em CamelCase
document= """
MegascopsCholiba
MegascoposAtricapillus	
MegascopsSanctaecatarinae	
MegascopsWatsonii	
MegascopsUsta	
MegascopsGuatemalae
"""

pattern = re.compile(r"Megascops(?!Usta)")

extract = re.findall(pattern,document)

print(extract)


#saída:
#['Megascops', 'Megascops', 'Megascops', 'Megascops']

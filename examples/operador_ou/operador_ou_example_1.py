import re

document = "banana, couve, laranja, arroz"

pattern = re.compile(r"banana|laranja")

extract =  re.findall(pattern,document)

print(extract)
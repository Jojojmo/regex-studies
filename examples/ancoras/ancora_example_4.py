import re

document = "Começo e final"

pattern= re.compile(r"^Começo e final$")

match = re.fullmatch(pattern,document)

if match:
    print(document)
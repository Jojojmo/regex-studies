import re

document_1 = "Paulo"

document_2 = "Alexandre"

document_3 = "Bianca"

document_4 = "Alexandra"

document_list = [document_1,document_2,document_3,document_4]

pattern= re.compile(r"Alexandr[ae]")


print('-'*24)
for index,document in enumerate(document_list):
    if re.match(pattern,document):
        print(f"Match indice {index}:{document}")
        print('-'*24)

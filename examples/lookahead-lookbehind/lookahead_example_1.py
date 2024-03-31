import re

document_list = [
'100kms',
'80mi',
'60kms',
'40mi',
'35mi',
'200kms'
]

pattern = re.compile(r'\d+(?=kms)')

for document in document_list:
    match = pattern.match(document)
    if match:
        print(match.group())

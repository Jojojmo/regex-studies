import re

document = """
protocolo-M, protocolo-D, protocolo-Y, protocolo-Q, protocolo-X, protocolo-S, protocolo-T, 
protocolo-P, protocolo-C, protocolo-Z, protocolo-R, protocolo-I, protocolo-N, protocolo-H, 
protocolo-U, protocolo-O, protocolo-K, protocolo-J, protocolo-G, protocolo-B, protocolo-W, 
protocolo-L, protocolo-V, protocolo-E, protocolo-F, protocolo-A
"""

pattern= re.compile(r'protocolo-[A-G]')

extract= re.findall(pattern,document)

print(extract)
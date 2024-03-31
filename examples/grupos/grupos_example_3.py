import re

document= """
instagram: @g1rl_me,
tiktok: @the_teodoro,
instagram: .http_edu,
youtube: @canal_du_jao,
linkedin: @the_vendor,
"""

pattern = re.compile(r"(instagram|tiktok):(\s@.*),")

extract = re.findall(pattern,document)

print(extract)

#Saída:
#[('instagram', ' @g1rl_me'), ('tiktok', ' @the_teodoro')]
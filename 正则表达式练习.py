import re
ip=100
n=re.fullmatch(r'\d[1-9]\d|1\d{2}|2[0-5]{2}',ip)
n.group()
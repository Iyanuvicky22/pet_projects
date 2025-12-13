import re

username = "apotiks224"
pattern = re.compile(r'^[a-z][a-z0-9-]{1,32}$')

print(pattern.match(username) is not None)

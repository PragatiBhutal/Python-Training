import re

s = input().strip()
sub = input().strip()

matches = list(re.finditer(f'(?={sub})', s))

if matches:
    for match in matches:
        print((match.start(), match.start() + len(sub) - 1))
else:
    print((-1, -1))

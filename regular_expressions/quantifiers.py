import re

print(re.fullmatch('(ab)?', 'ab'))

print(re.fullmatch('(ab)*', ''))

print(re.fullmatch('(ab)*', 'abababababab'))

print(re.findall('[abc]+', '123 abc 5643 abc@tgfd'))

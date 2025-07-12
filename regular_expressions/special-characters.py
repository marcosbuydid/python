import re

# first name (capitalized) and last name
print(re.match('[A-Z][a-z]+ [A-Z][a-z]+', 'Marcos Buydid'))

# name followed by number
print(re.match('[a-zA-Z_][a-zA-Z0-9_]*', 'name1'))

# time format hh:mm
print(re.match(r'([01]?[0-9]|2[0-3]):[0-5][0-9]', '3:33'))

# domain name (may not include all domains)
print(re.fullmatch('[a-zA-Z0-9]+\\.(com|org|net|gov)$', 'marcosbuydid.com'))

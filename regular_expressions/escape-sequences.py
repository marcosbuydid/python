import re

# date format dd/mm/yyyy
print(re.match(r'\d{2}/\d{2}/\d{4}', '13/08/1989'))

# password (sample only)
print(re.match(r'[\w_]{10,}', 'asdV_12345'))

# email (sample only)
print(re.match(r'\w+\.?\w+@\w+\.(com|org|gov)\Z', 'my.email@mail.com'))

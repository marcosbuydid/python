import re

print(re.match('abc', 'abcdef'))

print(re.fullmatch('python', 'python').group())

print(re.search('like', 'I like saturdays'))

print(re.findall('travel', 'travel with someone or travel alone around the world'))

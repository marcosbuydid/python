words_set = {'plea', 'medical', 'listen', 'leap', 'decimal', 'silent', 'pale', 'enlist'}
result = set()

for w1 in words_set:
    for w2 in words_set:
        if w1 != w2 and sorted(w1) == sorted(w2):
            pair = tuple(sorted((w1, w2)))
            result.add(pair)

print('Scrambled words:')
for pair in result:
    print(pair)

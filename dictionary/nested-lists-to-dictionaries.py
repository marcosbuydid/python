header = ['name', 'age', 'country']

data = [['Marc', 35, 'UY'], ['Sophie', 32, 'UY'], ['Clari', 25, 'DE'],
        ['Aubrey', 29, 'US'], ['Candace', 38, 'CAN'], ['Terry', 28, 'UK']]

result = []
length = len(header)

for i in range(length):
    dictionary = {}
    for row in data:
        if row[i] not in dictionary:
            dictionary[row[i]] = row
        else:
            dictionary[row[i]].append(row)
    result.append(dictionary)

print("Dictionaries:")
for i in range(length):
    print('\n' + header[i])
    for key, value in result[i].items():
        print(f"{key:<10}: {value}")

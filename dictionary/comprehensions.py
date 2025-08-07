L1 = [(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]
dictionary = {x: y for x, y in L1}
print(dictionary)

L2 = [10, 20, 30, 40]
L3 = ['Ten', 'Twenty', 'Thirty', 'Forty']
dictionary_1 = {x:y for x,y in zip(L1, L2)}
print(dictionary_1)

L4 = ['Ten', 'Eleven', 'Twelve', 'Thirteen']
dictionary_2 = {x:y for x,y in enumerate(L3, start=10)}
print(dictionary_2)

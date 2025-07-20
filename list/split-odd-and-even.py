l = [56,44,34,21,10,67,89,43,22]
odd_result = []
even_result = []
for i in l:
    if i % 2 == 0:
        odd_result.append(i)
    else:
        even_result.append(i)
print(odd_result)
print(even_result)
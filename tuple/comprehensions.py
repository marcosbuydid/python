# how to iterate

T = (*(x for x in range(1, 5)),)
print(T)

T1 = (*(x ** 2 for x in range(2, 8)),)
print(T1)

T2 = (*(x.lower() for x in 'pANDaS'),)
print(T2)

T3 = (*(int(x) for x in '12345'),)
print(T3)

T4 = (*(x for x in 'ab*cfr7u' if x.isalpha()),)
print(T4)

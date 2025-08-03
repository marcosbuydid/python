A = {1, 3, 5, 7, 9}
B = {2, 3, 4, 5, 6, 8, 10}

# union
C = A | B
print(C)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# other way and auto assign to A
# A = A | B
# print(A)

# intersection
D = A & B
print(D)  # {3, 5}

# difference
E = A - B
print(E)  # {1, 9, 7}

# symmetric difference
F = A ^ B
print(F)  # {1, 2, 4, 6, 7, 8, 9, 10}

# union is when joining all elements of both sets including the common ones.
# intersection is the result of the elements that are only in both sets.
# difference is the result of the elements that are only in one set and
# not in the other set nor in the intersection also.
# symmetric difference is the result of joining all the elements that are
# in both sets but excluding the common ones.

A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}

C = A.union(B)
print(C)  # {1, 2, 3, 5, 7, 9, 10, 11}

D = A.intersection(B)
print(D)  # {5,7}

E = A.difference(B)
print(E)  # {1, 2, 3}

F = A.symmetric_difference(B)
print(F)  # {1, 2, 3, 9, 10, 11}

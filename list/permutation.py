import itertools as it

l = ['A', 'B', 'C', 'D', 'E', 'F']
permutations = it.permutations(l, r=2)

permutation_list = list(permutations)
print('Permutations:',permutation_list)

for i in permutation_list:
    print(i)
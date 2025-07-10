for i in range(1, 4):
    for j in range(1, 4):
        print(i, ',', j, end=' ')
    print('')

# prime numbers from 1-100
interval = 200
prime_qty = 0
factors_qty = 0
for i in range(1, interval + 1):
    for j in range(1, interval + 1):
        if i % j == 0:
            factors_qty += 1
    if factors_qty == 2:
        prime_qty += 1
    factors_qty = 0
print('there are', prime_qty, 'prime numbers in the interval 1 to', interval)

# draw patterns
# draw * on a 5x5 matrix
for k in range(1, 6):
    for l in range(1, 6):
        print('*', end=' ')
    print('')

# draw * on the half bottom-left of a 5x5 matrix
for m in range(1, 6):
    for n in range(1, 6):
        if m >= n:
            print('*', end=' ')
    print('')

# draw * on the half top-left of a 5x5 matrix
for o in range(1, 6):
    for p in range(1, 6):
        if o <= p:
            print('*', end=' ')
    print('')

# draw * on the half top-right of a 5x5 matrix
for q in range(1, 6):
    for r in range(1, 6):
        if r >= q:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')

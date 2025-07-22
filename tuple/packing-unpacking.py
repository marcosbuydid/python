# concatenation
T = (1, 2, 3)
T1 = (9, 8, 7)
T2 = T + T1
print(T2)

# repetition
T3 = T1 * 4
print(T3)  # (9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7)

# packing unpacking
T4 = 20, 21, 22, 23
print(T4)  # (20, 21, 22, 23)

T5 = 6, 7, 8, 9
a, b, c, d = T5
print(a, b, c, d)  # 6 7 8 9

T6 = 3, 4, 5, 6
*a, b, c = T6
print(a, b, c)  # [3, 4] 5 6

T7 = 1, 4, 2, 5
a, *b, c = T7
print(a, b, c)  # 1 [4, 2] 5

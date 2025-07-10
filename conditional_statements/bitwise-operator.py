# representation in binary of a given number
n = 16
print(format(n, 'b'))

# bitwise AND (&)
# this operator returns a new number where each bit is 1
# only if the corresponding bits in both operands are 1
a = 8  # 1000 in binary
b = 4  # 0100 in binary
result_and = a & b
print('bitwise AND of', a, 'and', b, 'is', result_and)

# bitwise OR (|)
# this operator returns a new number where each bit is 1 if
# at least one of the corresponding bits in the operands is 1
c = 2  # 0010 in binary
d = 3  # 0011 in binary
result_or = c | d
print('bitwise OR of', c, 'and', d, 'is', result_or)

# bitwise NOT (~)
# this unary operator inverts all the bits of its operand.
# for positive integers, the result is typically equivalent to -(x + 1)
e = 12  # 1100 in binary
result_not = ~e
print('bitwise NOT of', e, 'is', result_not)

# bitwise XOR (^)
# this operator returns a new number where each bit is 1 if the corresponding
# bits in the operands are different
f = 7  # 0111 in binary
g = 9  # 1001 in binary
result_xor = f ^ g
print('bitwise XOR of', f, 'and', g, 'is', result_xor)

# bitwise Left Shift (<<)
# this operator shifts the bits of the operand to the left by a specified
# number of positions, filling the vacated positions on the right with zeros
# this is equivalent to multiplying the number by 2 raised to the power of the shift amount
h = 10  # 1010 in binary
result_left_shift = h << 2
print('bitwise left shift of', h, 'by 2 is', result_left_shift)

# bitwise Right Shift (>>)
# this operator shifts the bits of the operand to the right by a specified
# number of positions. for positive numbers, it fills the vacated positions on the left with zeros
# this is equivalent to floor division of the number by 2 raised to the power of the shift amount
i = 20  # 10100 in binary
result_right_shift = i >> 2
print('bitwise right shift of', i, 'by 2 is', result_right_shift)

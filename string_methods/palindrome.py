# check if a string is palindrome
s = 'radar'
s_inverted = s[::-1]
is_palindrome = True

for i in range(len(s)):
    if s[i] != s_inverted[i]:
        is_palindrome = False
        print(s, 'is not palindrome')
        break  # if any difference is found
    if not is_palindrome:
        break

if is_palindrome:
    print(s, 'is palindrome')

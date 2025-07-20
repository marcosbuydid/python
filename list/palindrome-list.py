l = [4, 3, 3, 4]
l1 = l.copy()
l1.reverse()
isPalindrome = True

for i in range(len(l)):
    if l[i] != l1[i]:
        isPalindrome = False
        break
if isPalindrome:
    print('The list is palindrome')
else:
    print('The list is not palindrome')

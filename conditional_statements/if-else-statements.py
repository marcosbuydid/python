# tell if a number is even or odd
n = 23
if n % 2 == 0:
    print('Even')
else:
    print('Odd')

# tell if a person is able to vote
age = 17
if age >= 18:
    print('You are able to vote')
else:
    print('You are not able to vote')

# tell if a letter is vowel or consonant
letter = 'z'
if (letter == 'a' or letter == 'e' or
        letter == 'i' or letter == 'o' or letter == 'u'):
    print('the letter is vowel')
else:
    print('the letter is consonant')

# nested if and elif
temperature = 30
if temperature == 25:
    print('The temperature of the room is normal')
else:
    if temperature < 25:
        print('The temperature of the room is cold')
    else:
        print('The temperature of the room is hot')

# tell if given a year is leap or not
year = 2000
if year % 100 == 0:
    if year % 400 == 0:
        print('The year is a leap year')
    else:
        print('The year is not a leap year')
elif year % 4 == 0:
    print('The year is a leap year')
else:
    print('The year is not a leap year')

# string comparison (dictionary order)
s1 = 'software'
s2 = 'hardware'
if s1 > s2:
    print(s1, 'is after', s2, 'in the dictionary')
else:
    print(s1, 'is before', s2, 'in the dictionary')

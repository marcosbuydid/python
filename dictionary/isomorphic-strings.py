# Two isomorphic strings are strings where the characters in one
# can be replaced to get the other, while preserving the order and
# uniqueness of character mapping.

string1, string2 = 'snowflake', 'trbzmxquv'
isomorphic = True

if len(string1) != len(string2):
    isomorphic = False
else:
    map1, map2 = {}, {}
    for c1, c2 in zip(string1, string2):
        if c1 in map1:
            if map1[c1] != c2:
                isomorphic = False
        else:
            map1[c1] = c2
        if c2 in map2:
            if map2[c2] != c1:
                isomorphic = False
        else:
            map2[c2] = c1
if isomorphic:
    print('The strings are isomorphic')
else:
    print('The strings are not isomorphic')

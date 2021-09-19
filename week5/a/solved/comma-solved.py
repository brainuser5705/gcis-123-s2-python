"""
Print the list of letters the word "pillow", each separated by a comma.
The output must not end with a comma

Output: 
p, i, l, l, o, w
"""

prefix = ''
i = 0
while i < len('pillow'):
    print(prefix + 'pillow'[i], end='')
    prefix = ', '
    i += 1

print('\n')

j = 0
while j < len('pillow'):
    print('pillow'[j], end='')
    if (j != len('pillow') - 1):
        print(', ', end='')
    j += 1






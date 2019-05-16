s = input()
from string import ascii_lowercase
letters = list(ascii_lowercase)
for i in s.lower():
    if i in letters:
        letters.remove(i)

if len(letters)>0:
    print('not pangram')
else:
    print('pangram')

import difflib

s = input()

result = 0
for c in range(len(s)):
    if s[c] != 'SOS'[c%3]:
        result+=1
print(result)
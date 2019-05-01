l = int(input())
s = input()
r = int(input())

result = ""
for c in s:
    if c.isalpha():
        a = 'A' if c.isupper() else 'a'
        c = chr(ord(a) + (ord(c) - ord(a) + r)%26);
    result+=c
print(result)
import re

n = input()
s = input()

num = re.findall('[0-9]', s)
l = re.findall('[a-z]', s)
u = re.findall('[A-Z]', s)
ss = re.findall('[\!\@\#\$\%\^\&\*\(\)\-\+]', s)
# print(num, l, u, ss)

c=0
count = 6-len(s)
if not l:
    c+=1
if not num:
    c+=1
if not u:
    c+=1
if not ss:
    c+=1
print(max(c, count))

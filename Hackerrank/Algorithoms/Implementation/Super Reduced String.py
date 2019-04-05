s=input()
l=[]
for i in s:
    if l and i == l[-1]:
        l.pop()
    else:
        l.append(i)
if len(l):
    print(''.join(l))
else:print('Empty String')
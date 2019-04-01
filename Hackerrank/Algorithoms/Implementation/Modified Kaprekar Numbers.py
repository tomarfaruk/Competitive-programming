n=int(input())
m=int(input())

p = False
for i in range(n, m+1):
    sq = i**2
    numtostr = str(sq)
    l= len(numtostr)
    if l>1:
        s1, s2 = numtostr[:l//2], numtostr[l//2:]
    else:s1, s2 = numtostr, ''


    num=0
    if len(s2)>0:
        if int(s2)>0:
            num = int(s1)+int(s2)
    else: num = int(s1)

    if num == i:
        print(i, end=' ')
        p=True

if not p:
    print('INVALID RANGE')
else: print()
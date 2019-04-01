t = int(input())
for _ in range(t):
    n = int(input())
    m=[]
    for i in range(n):
        m.append(list(map(int, input().split())))

    con1 = con2 = []
    for i in range(n):
        con1.append(0)
        con2.append(sum(m[i]))
        print(m[i])
        for j in range(n):
            con1[i] += m[j][i]

    con1.sort()
    con2.sort()

    if con1 == con2:
        print('Possible')
    else:
        print('Impossible')
for _ in range(int(input())):
    s = input()

    h = "hackerrank"
    j=0
    l = len(h)
    result = 0
    for c in h:
        if c in s:
            i = s.index(c)
            s = s[i+1:]
            print(i,s)
            j+=1
        else:
            print('NO')
            break
    if j==l:
        print('YES')
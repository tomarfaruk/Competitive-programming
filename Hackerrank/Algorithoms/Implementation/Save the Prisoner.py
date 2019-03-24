m, n, s = map(int, input().split())

if (n+s-1)%m == 0:
    print(m)
else:
    print((n+s-1)%m)
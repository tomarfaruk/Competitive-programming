def chocolateFeast(n, c, m):
    totalCocklet = n//c
    wraper = totalCocklet
    while wraper >= m:
        wrapCocklet = wraper//m
        totalCocklet += wrapCocklet
        wraper = wraper%m + wrapCocklet
    return totalCocklet

t = int(input())
for _ in range(t):
    ncm = input().split()
    n = int(ncm[0])
    c = int(ncm[1])
    m = int(ncm[2])
    result = chocolateFeast(n, c, m)
    print(result)
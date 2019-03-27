def surfaceArea(A):
    ans=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            ans += (A[i][j]*4)+2
            if j > 0: ans -= min(A[i][j-1], A[i][j])*2
            if i > 0: ans -= min(A[i-1][j], A[i][j])*2
    return ans

h, w = map(int, input().split())

a = []
for _ in range(h):
    a.append(list(map(int, input().split())))

print(surfaceArea(a))
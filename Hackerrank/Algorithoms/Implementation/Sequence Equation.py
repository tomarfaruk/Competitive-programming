n = int(input())
p = list(map(int, input().split()))

for i in range(1, n+1):
    f = p.index(i)+1
    print(p.index(f)+1)
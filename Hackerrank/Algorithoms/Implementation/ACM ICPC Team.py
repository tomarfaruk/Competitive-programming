from itertools import combinations
n, m = map(int, input().split())

data=[]
for _ in range(n):
    data.append(input())

results=[]
for a, b in combinations(data, 2):
    a = int(a, 2)
    b = int(b, 2)
    n = str(bin(a|b))[2:].count('1')
    results.append(n)

print(max(results), results.count(max(results)), sep='\n')
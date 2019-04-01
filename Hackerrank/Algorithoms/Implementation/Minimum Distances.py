from collections import Counter

l=int(input())
p = list(map(int, input().split()))

c=Counter(p)
mindis=l
for key, value in c.items():
    if value>1:
        fposition = p.index(key)
        sposition = p.index(key, fposition+1)
        if mindis > sposition-fposition:
            mindis = sposition-fposition

print(mindis if mindis !=l else -1)
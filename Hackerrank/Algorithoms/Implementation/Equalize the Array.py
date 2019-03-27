from collections import Counter
n = int(input())
val = list(map(int, input().split()))
c = Counter(val)
print(n - val.count(max(c, key=c.get)))
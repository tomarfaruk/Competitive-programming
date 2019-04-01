p, d, m, s = map(int, input().split())

count=0
while True:
    if s < p:
        break
    s -= p
    p -= d
    if p < m:
        p = m
    count+=1
    print(s, p)
print(count)
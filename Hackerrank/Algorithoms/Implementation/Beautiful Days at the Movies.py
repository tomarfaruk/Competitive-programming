i, j, k = map(int, input().split())
count = 0
for r in range(i, j + 1):
    if abs(r - int(str(r)[::-1])) % k == 0:
        count += 1
print(count)
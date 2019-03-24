n, s = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(0, n, s):
    result += 1
    if arr[(i+s)%n] == 1:
        result += 2
print(100 - result)
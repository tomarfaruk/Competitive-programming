n = int(input())
p = 5
result=0
for _ in range(n):
    result += p//2
    p = (p//2)*3
    print(p)
print(result)
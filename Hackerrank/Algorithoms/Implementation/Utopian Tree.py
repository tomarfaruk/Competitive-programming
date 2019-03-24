n = int(input())
result=0
for i in range(n+1):
    if i % 2 == 0:
        result += 1
        print(result)
    else:
        result *= 2
        print(result)
n, a = input(), list(map(int, input().split()))
print(max([a.count(_)+a.count(_+1) for _ in set(a)]))
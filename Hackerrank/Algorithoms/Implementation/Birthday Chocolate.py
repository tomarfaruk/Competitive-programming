n = int(input())
arr = list(map(int, input().split(' ')))
d, m = map(int, input().split())

print(sum([1 for i in range(n) if sum(arr[i:i+m])== d]))
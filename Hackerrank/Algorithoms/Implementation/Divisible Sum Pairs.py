from itertools import combinations
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(sum([1 for pair in combinations(arr,2) if sum(pair)%k==0]))
import numpy as np

pre = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
]

# s = list(map(int, input().split()))
s=[]
for _ in range(3):
    s += map(int, input().split())
print(s)
min_cost = 81
for p in pre:
    re = np.subtract(s, p)
    # re = re.tolist()
    re = sum(list(map(lambda x:abs(x), re)))
    min_cost = min(min_cost, re)
print(min_cost)

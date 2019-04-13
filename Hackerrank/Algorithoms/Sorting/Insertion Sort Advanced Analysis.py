def xQuery(data, i, size):
  j, s = i, 0
  while i > 0: s += data[i]; i = i & (i-1)
  while j < size: data[j] += 1; j += j & -j
  return s

def insertionSort(arr):
  size = 10**7
  data = size*[0]
  return sum(i-xQuery(data, v, size) for i, v in enumerate(arr))


t = int(input())
for t_itr in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = insertionSort(arr)
    print(result)

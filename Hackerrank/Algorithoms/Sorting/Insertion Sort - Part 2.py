n, arr = int(input()), list(map(int, input().split()))

for i in range(1, n):
    key = arr[i]
    j = i
    while j>0 and key<arr[j-1]:
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = key
    print(*arr)

n, arr = int(input()), list(map(int, input().split()))

count = [0]*max(len(arr),n)
for i in arr:
    count[i]+=1

print(*count)
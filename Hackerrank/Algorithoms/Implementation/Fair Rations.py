n = int(input())
arr = list(map(int, input().split()))

if sum(arr)%2 == 1:
    print('NO')

count = 0
for i in range(n):
    if arr[i]%2 != 0:
        arr[i]+=1
        arr[i+1]+=1
        count+=2

print(count)
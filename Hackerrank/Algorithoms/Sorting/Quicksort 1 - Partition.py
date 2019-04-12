n, arr = int(input()), list(map(int, input().split()))
count=0
key=arr[0]
arrleft, arrright=[], []
for i in range(n):
    if arr[i] >= key:
        arrright.append(arr[i])
    else:
        arrleft.append(arr[i])
print(*arrleft, *arrright)
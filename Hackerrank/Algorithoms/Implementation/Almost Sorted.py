
n = input()
arr = list(map(int, input().split()))
s = sorted(arr)

d1=d2=-1
totaldif=0
for i in range(int(n)):
    if arr[i] != s[i]:
        totaldif+=1
        if d1 == -1:
            d1=i
        else:
            d2=i
if arr==s:
    print('yes')
elif totaldif==2:
    arr[d1], arr[d2] = arr[d2], arr[d1]
    if arr==s:
        print('yes')
        print("swap %d %d"%(d1+1, d2+1))
    else:
        print('no')
else:
    arr = arr[:d1] + arr[d1:d2+1][::-1] + arr[d2+1:]
    if arr==s:
        print('yes')
        print("reverse %d %d"%(d1+1, d2+1))
    else:
        print('no')
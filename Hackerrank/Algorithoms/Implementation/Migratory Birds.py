input()
arr = list(map(int, input().split()))
a= [0]*6
for id in arr:
    a[id]+=1
print(a.index(max(a)))
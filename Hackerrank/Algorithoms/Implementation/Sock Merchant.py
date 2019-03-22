n = int(input())
arr = list(map(int, input().split()))
pair=[]
count=0
for item in arr:
    if item in pair:
        count+=1
        pair.remove(item)
    else: pair.append(item)

print(count)
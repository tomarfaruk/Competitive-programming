n, k = map(int, input().split())
inarr = list(map(int, input().rstrip().split()))

luckypage = 0
page=0
for s in inarr:
    arr = list(range(s+1))
    nums = [arr[x:x+k] for x in range(1, s+1, k)]
    for i in nums:
        page+=1
        # print(i, page)
        if page in i:
            luckypage += 1

print(luckypage)



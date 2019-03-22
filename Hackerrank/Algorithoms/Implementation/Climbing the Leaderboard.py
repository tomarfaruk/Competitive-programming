s, score = input(), list(map(int, input().split()))
a, alice = input(), list(map(int, input().split()))
score = sorted(list(set(score)), reverse=True)
results=[]
l=len(score)
for po in alice:
    while l>0 and po>= score[l-1]:
        l-=1
    print(l+1)
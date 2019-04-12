n, arr = int(input()), list(map(int, input().split()))

count = [0]*100
for i in arr:
    count[i]+=1

sortedarr = []
for i in range(100):
    sortedarr+= [i]*count[i]


print(*sortedarr)


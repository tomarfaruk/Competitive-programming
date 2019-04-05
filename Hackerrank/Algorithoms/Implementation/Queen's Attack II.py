n, k = map(int, input().strip().split())
rQueen, cQueen = map(int, input().strip().split())
ObList = []
for a0 in range(k):
    rObstacle, cObstacle = map(int, input().strip().split())
    ObList.append((rObstacle, cObstacle))
ObSet = set(ObList)
Delta = [(0,1), (1,1), (1,0), (0,-1), (-1,-1), (-1,0), (1,-1), (-1,1)]
Count = 0
for shift in Delta:
    Pos = (rQueen, cQueen)
    while 1 <= Pos[0] + shift[0] <= n and 1 <= Pos[1] + shift[1] <= n:
        Pos = (Pos[0]+shift[0], Pos[1]+shift[1])
        if Pos in ObSet:
            break
        Count += 1
print(Count)

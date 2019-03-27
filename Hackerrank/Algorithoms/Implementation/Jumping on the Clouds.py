def jumpingOnClouds(c):
    re=i=0

    while i <len(c):
        if i+2 < len(c):
            if c[i+2] == 1: i+=1
            else: i+=2
        else: i+=1
        re+=1
    return re-1

n = int(input())
c = list(map(int, input().rstrip().split()))
print(jumpingOnClouds(c))
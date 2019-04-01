t = int(input())

for _ in range(t):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    if bc == wc or abs(bc-wc) <= z:
        print(b*bc+w*wc)
    else:
        cost = (b+w)*min(bc,wc)
        if bc >= wc:
            cost += z*b
        else: cost += z*w
        print(cost)

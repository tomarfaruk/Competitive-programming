

d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
if d1[2] > d2[2]:
    print(10000)
elif d1[2] < d2[2]:
    print(0)
elif d1[1] > d2[1]:
    print(500 * abs(d1[1] - d2[1]))
elif d1[1] < d2[1]:
    print(0)
elif d1[0] > d2[0]:
    print(15 * abs(d1[0] - d2[0]))
else:
    print(0)
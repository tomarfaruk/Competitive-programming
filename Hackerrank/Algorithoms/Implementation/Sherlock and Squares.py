from math import sqrt, floor, ceil
n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    j=0
    # for i in range(int(sqrt(s)), ceil(sqrt(e))+1):
    #     if s <= i**2 <= e:
    #         j+=1
    # print(j)
    print(floor(sqrt(e)) - ceil(sqrt(s)) + 1 )
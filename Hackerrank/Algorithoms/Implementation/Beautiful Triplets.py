nd = input().split()

n = int(nd[0])

d = int(nd[1])

arr = list(map(int, input().rstrip().split()))


def beautifulTriplets(d, seq):
    return sum([(i+d and i+d+d in seq) for i in seq])


result = beautifulTriplets(d, set(arr))
print(result)
T = int(input())


def stones(n, a, b):
    return sorted(set([i*b+(n-1-i)*a for i in range(n)]))


for T_itr in range(T):
    n = int(input())
    a = int(input())
    b = int(input())
    result = stones(n, a, b)
    print(' '.join(map(str, result)))
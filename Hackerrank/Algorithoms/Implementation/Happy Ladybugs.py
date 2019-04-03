from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    if b.count('_'):
        b = list(b)
        while b.count('_'):
            b.remove('_')

        s = Counter(b)
        if 1 in s.values():
            return 'NO'
        else:
            return 'YES'
    else:
        s = Counter(list(b))
        if 1 in s.values():
            return 'NO'
        else:
            p = list(b)
            for i in range(1, len(b)-1):
                if b[i] != b[i+1] and b[i] != b[i-1]:
                    return 'NO'
            return 'YES'

g = int(input())
for g_itr in range(g):
    n = int(input())
    b = input()
    result = happyLadybugs(b)
    print(result)


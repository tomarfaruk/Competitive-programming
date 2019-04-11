n, s = int(input()), list(map(int, input().split()))

p=s[-1]
print(p)
i=len(s)-1
while i > 0:
    if s[i-1] <= p:
        s[i] = p
        print(*s)
        break
    else:
        s[i] = s[i - 1]
        print(*s)
        i -= 1


if s[0] >p:
    s[1] = s[0]
    s[0]=p
    print(*s, sep=' ')



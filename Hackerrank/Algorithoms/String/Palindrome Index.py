def solve():
    s = list(input().strip())
    st = ''.join(s)
    # print(st)
    # print(s)
    temp=s
    s=st
    # print(s)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            arr = s[i + 1: len(s) - i]
            if arr== arr[::-1]:
                return i
            else:
                return len(s)-i-1
            # return arr.join('') == arr.reverse().join('') ? i: s.length - i - 1;
    return -1


for _ in range(int(input())):
    print(solve())

for _ in range(int(input())):
    s = input()
    has_greater = False
    for i in range(len(s)-1)[::-1]:
        if s[i] < s[i+1]:
            break


    for j in range(i + 1, len(s))[::-1]:
        if s[i] < s[j]:
            lis = list(s)
            lis[i], lis[j] = lis[j], lis[i]
            print("".join(lis[:i + 1] + lis[i + 1:][::-1]))
            has_greater = True
            break

    if has_greater == False:
        print("no answer")
n, k = map(int, input().split())
for _ in range(n):
    a = list(map(int, input().split()))
    arr_stu = list(map(lambda x:1 if x <= 0 else 0, a))
    print(arr_stu.count(1))
    if arr_stu.count(1) >= 2:
        print('NO')
    else: print("YES")
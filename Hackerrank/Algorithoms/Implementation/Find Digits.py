n = int(input())

for _ in range(n):
    m = int(input())
    div_num = list(map(lambda x: 1 if m%x==0 else 0, [int(i) for i in str(m) if i !='0']))
    print(div_num)
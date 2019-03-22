n, k = map(int, input().split(' '))
bill = list(map(int, input().split(' ')))
bb = int(input())

total = sum(bill)//2 - bill[k]//2
if total == bb:
    print("yes")
else:
    print(abs(bb-total))
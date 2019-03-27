from math import *
s = input().replace(" ",'')
s_l = len(s)
low, height = floor(sqrt(s_l)), ceil(sqrt(s_l))
if low*height < s_l:
    low += 1

count =0
results = []
for _ in range(low+1):
    results.append(s[_::height])
    count += low
    if count>= s_l:
        break
print(*results)

str1 = input()
str2 = input()
k = int(input())
i = 0
L = len(str1)+len(str2)
while str1[i] == str2[i] and i != min(len(str1), len(str2)) -1:
    i += 1

if L <= k + i*2 and L%2 == k%2 or L < k:
    print('YES')
else: print('NO')
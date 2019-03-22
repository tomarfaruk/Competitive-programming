n = input()
s = input()
c = v = 0
for i in s:
    if i=='U':
        v+=1
    else: v-=1
    #up from see level
    if v==0 and i=='U':
        c+=1
print(c)
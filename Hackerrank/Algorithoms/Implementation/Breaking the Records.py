n,a= int(input()),list(map(int, input().split()))
max=min=a[0];c1=c2=0
for i in range(1,n):
    if a[i]>max:
        c1+=1;max=a[i]
    if a[i]<min:
        c2+=1;min=a[i]
print(c1,c2,sep=' ')

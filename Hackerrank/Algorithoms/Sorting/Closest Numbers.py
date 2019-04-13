n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans=[]
mindif=abs(nums[1]-nums[0])
for i in range(1, len(nums)-1):
    dif = abs(nums[i]-nums[i+1])
    if dif < mindif:
        ans=[]
        ans.append(nums[i])
        ans.append(nums[i+1])
        mindif=dif
    elif mindif == abs(nums[i]-nums[i+1]):
        ans.append(nums[i])
        ans.append(nums[i + 1])
print(*ans)
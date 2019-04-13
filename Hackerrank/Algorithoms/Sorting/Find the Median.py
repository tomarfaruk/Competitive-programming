n = int(input())
nums = list(map(int, input().split()))
nums.sort()
median=nums[(n//2)]
if n%2==0:
    median = (nums[n//2]+nums[(n//2)+1])/2
print(median)
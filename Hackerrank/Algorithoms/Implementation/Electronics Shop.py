b, k, d = map(int, input().split())
keyboards = list(map(int, input().split()))
devices = list(map(int, input().split()))

result = [key+ dev for key in keyboards for dev in devices if key+dev < b]
if len(result)==0:
    print(-1)
else:
    print(max(result))
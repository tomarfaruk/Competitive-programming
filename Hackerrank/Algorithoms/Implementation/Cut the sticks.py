n = input()
arr = list(map(int, input().split()))

while len(arr) > 0:
    print(arr)
    print(len(arr))
    min_value = min(arr)
    arr = [ i-min_value for i in arr if i-min_value > 0 ]

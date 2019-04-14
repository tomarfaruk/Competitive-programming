def countsort(data):
    arr = [0]*201
    for i in data:
        arr[i]+=1
    return arr

def med_even(data, reser):
    res = 0
    count = None
    temp0 = reser // 2
    temp1 = temp0 + 1
    for i, value in enumerate(data):
        res += value
        if res == temp0:
            count = i
        if res > temp0:
            if count != None:
                count += i
                return count
            else:
                return 2*i
def med_odd(data, reser):
    res = 0
    temp = reser // 2
    for i, value in enumerate(data):
        res += value
        if res > temp:
            return 2*i

def median(data, lenght):
    if lenght%2:
        mid = med_odd(data, lenght)
    else:
        mid = med_even(data, lenght)
    return mid

n, d = map(int, input().split())
data = list(map(int, input().split()))
sorteddata = countsort(data[0:d])
notification = 0
firsttime = True
for i in range(d-1, n-1):
    if firsttime:
        firsttime=False
    else:
        sorteddata[data[i - d]] -= 1

    mediannum = median(sorteddata, d)
    nextday = data[i+1]
    # print(nextday)
    sorteddata[nextday] += 1
    if mediannum <= nextday:
        notification += 1
print(notification)
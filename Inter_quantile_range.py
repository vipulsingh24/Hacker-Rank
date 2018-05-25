def calc_median(arr, start, stop):
    len_ = stop - start + 1
    mid = start + len_ // 2
    if (len_ % 2 == 0):
        return(arr[mid-1] + arr[mid]) / 2
    else:
        return(arr[mid])

def quartiles(temp):
    temp = sorted(temp)
    len_ = len(temp)
    q2 = calc_median(temp, 0, len_ - 1)
    mid = len_ // 2
    if (len_ % 2 == 0):
        q1 = calc_median(temp, 0, mid-1)
        q3 = calc_median(temp, mid, len_ - 1)
    else:
        q1 = calc_median(temp, 0, mid-1)
        q3 = calc_median(temp, mid + 1, len_ - 1)
    return q1, q2, q3

def iqr(elem, freq):
    len_ = len(elem)
    temp = []
    for i in range(len_):
        temp.extend([elem[i]]*freq[i])
    temp.sort()
    qs = quartiles(temp)
    result = float(qs[2] - qs[0])
    return result
        
n = int(input())
elem = [int(x) for x in input().split()]
freq =[int(x) for x in input().split()]
print(iqr(elem, freq))

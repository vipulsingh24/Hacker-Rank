def mean(a, n):
    result = 0
    for i in a:
        result += i
    result /= n
    return result

def median(a, n):
    sort_a = sorted(a)
    mid = (n - 1) // 2
    if n % 2 == 0:
        return (sort_a[mid] +sort_a[mid+1]) / 2
    else:
        return sort_a[mid]
    
def mode(a):
    counter = {}
    result = None
    for i in a:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
        if (result is None) or (counter[i] > counter[result]):
            result = i
        elif (counter[i] == counter[result]) and (i < result):
            result = i
    return result

def std_dev(a, n):
    m = mean(a, n)
    result = 0
    for i in a:
        result += (i - m) ** 2
    result = (result / n) ** (0.5)
    return result

#Confidence Interval
def conf_int(a, n):
    conf_level = 1.96
    m = mean(a, n)
    sd = std_dev(a, n)
    low_bound = m - conf_level * (sd / n ** (1/2))
    upper_bound = m + conf_level * (sd / n ** (1/2))
    return low_bound, upper_bound
    
x = int(input())
a = [int(x) for x in input().split()]
n = len(a)

print(mean(a, n))
print(median(a, n))
print(mode(a))
print(round(std_dev(a, n), 1))
l, u = conf_int(a, n)
print(l, u)

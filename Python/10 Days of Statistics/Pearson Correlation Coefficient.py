def mean(a, n):
    result = 0
    for i in a:
        result += i
    result /= n
    return round(result, 3)

def std_dev(a, n):
    m = mean(a, n)
    result = 0
    for i in a:
        result += (i - m) ** 2
    result = (result / n) ** (0.5)
    return round(result, 3)

def cov(x, y, x_m, y_m, n):
    result = 0
    for i in range(n):
        x[i] -= x_m
        y[i] -= y_m
    for i in range(n):
        result +=  (x[i] * y[i])
	
	# 1-for loop
#	for i in range(n):
#		result += ((x[i] - x_m) * (y[i] - y_m))
    return result / n

n = int(input())
x = [float(x) for x in input().split()]
y = [float(x) for x in input().split()]
x_m = mean(x, n)
y_m = mean(y, n)
num = cov(x, y, x_m, y_m, n)
denom = std_dev(x, n) * std_dev(y, n)
print(round((num / denom), 3))

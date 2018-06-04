def mean(a, n):
    result = 0
    for i in a:
        result += i
    result /= n
    return result

def std_dev(a, n):
    m = mean(a, n)
    result = 0
    for i in a:
        result += (i - m) ** 2
    result = (result / n) ** (0.5)
    return result

def cov(x, y, x_m, y_m, n):
    result = 0
    for i in range(n):
        result += ((x[i] - x_m) * (y[i] - y_m))
    return result / n

n = 10
# x = [float(x) for x in input().split()]
x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
# y = [float(x) for x in input().split()]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
x_m = mean(x, n)
y_m = mean(y, n)
sd_x = std_dev(x, n)
sd_y = std_dev(y, n)
num = cov(x, y, x_m, y_m, n)
denom = sd_x * sd_y
r = num / denom
slope = r * (sd_y / sd_x)
# slope = round(slope, 3)
# Intercept is y_m - b(x_m)
intercept = y_m - (slope * x_m)
# x = 10
pred = (slope * 10) + intercept
print(round(pred, 1))

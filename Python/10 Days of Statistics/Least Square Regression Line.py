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

n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
x_mean = mean(x, n)
y_mean = mean(y, n)
sd_x = std_dev(x, n)
sd_y = std_dev(y, n)
rho = 0
for i in range(n):
    rho += ((x[i] - x_mean) * (y[i] - y_mean))
rho /= (n * sd_x * sd_y)

b = rho * (sd_y / sd_x)
a = y_mean - (b * x_mean)

predict = a + (b * 80)
print(round(predict, 3))

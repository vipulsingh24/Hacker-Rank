import math

def cdf(m, s, x):
    result = (1 + (math.erf((x - m) / (s * math.sqrt(2))))) / 2
    return result

mean, std = [70, 10]

# Percentage of students scored Grade > 80
# print('%.2f' % (100 * (cdf(mean, std, 100) - cdf(mean, std, 80))))
print(100 * round((cdf(mean, std, 100) - cdf(mean, std, 80)), 2))

# Percentage of students scored Grade >= 60
# print('%.2f' % (100  * (cdf(mean, std, 100) - cdf(mean, std, 60))))
print(100 * round((cdf(mean, std, 100) - cdf(mean, std, 60)), 2))

# Percentage of students scored Grade < 60
# print('%.2f' % (100 * (cdf(mean, std, 60) - cdf(mean, std, 0))))
print(100 * round((cdf(mean, std, 60) - cdf(mean, std, 0)), 2))

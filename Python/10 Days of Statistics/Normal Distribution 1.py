import math

def cdf(m, s, x):
    result = (0.5) * (1 + math.erf((x - m) / (s * (2 ** 0.5))))
    return result

mean, std = [float(x) for x in input().split()]
x1 = float(input())
x2 = [float(x) for x in input().split()]

print('%.3f' % cdf(mean, std, x1))
print('%.3f' % (cdf(mean, std, x2[1]) - cdf(mean, std, x2[0])))

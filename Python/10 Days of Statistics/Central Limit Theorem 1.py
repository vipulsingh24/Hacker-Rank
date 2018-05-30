import math

def cdf(m, sd, x):
    result = (1 + math.erf((x - m) / (sd * math.sqrt(2)))) / 2
    return result

max_wt = 9800
n = 49
m = 205
sd = 15

# Central Limit Theorem
m = n * m
sd = math.sqrt(n) * sd

print('%.4f' % (cdf(m, sd, max_wt)))


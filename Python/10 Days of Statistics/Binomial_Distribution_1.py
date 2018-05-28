def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combination(r, n = 6):
    num = factorial(n)
    denom = factorial(r) * factorial(n - r)
    return num / denom    

def bernoulli(x, y):
    p = 1.09 / 2.09
    q = 1 / 2.09
    pq = (p ** x) * (q ** y)
    return pq

result = 0; j = 3
for i in range(3, 7):
    result += combination(i, n = 6) * bernoulli(i, j)
    j -= 1
print('%.3f' % result)

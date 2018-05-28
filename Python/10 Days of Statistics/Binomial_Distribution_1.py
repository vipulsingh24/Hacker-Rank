'''
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e.,  1.234format).
'''


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
    p = 1.09 / 2.09	#Probability of boy
    q = 1 / 2.09	#Probability of girl
    pq = (p ** x) * (q ** y)
    return pq

result = 0; j = 3
for i in range(3, 7):
    result += combination(i, n = 6) * bernoulli(i, j)
    j -= 1
print('%.3f' % result)

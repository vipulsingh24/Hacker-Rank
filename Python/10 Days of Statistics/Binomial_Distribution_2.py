'''
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?
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
    p = 0.12	#Probability of rejected
    q = 1 - p	
    pq = (p ** x) * (q ** y)
    return pq

# No more than 2 rejects

result = 0; j = 10; n = 10
for i in range(3):
    result += combination(i, n) * bernoulli(i, j)
    j -= 1
print('%.3f' % result)

# At least 2 rejects
result = 0; j = 10; n = 10
for i in range(2):
    result += combination(i, n) * bernoulli(i, j)
    j -= 1
result = 1 - result
print('%.3f' % result)

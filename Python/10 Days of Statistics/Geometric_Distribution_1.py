'''
The geometric distribution is a special case of the negative binomial distribution that deals with the number of Bernoulli trials required to get a success (i.e., counting the number of failures before the first success).

Geometric Dist = q^(n-1) * p
'''
def geometric(n):
    p = 1/3	
    q = 1 - p	
    pq = (q ** (n - 1)) * p
    return pq

n = 5
print('%.3f' % geometric(n))

'''
Poisson Distribution is given by,
P(k, lambda)  = (lambda^k * e^-lambada) / k!
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def poisson(lamb, k):
    e = 2.71828
    num = (lamb ** k) * (e ** (-lamb))
    result = num / factorial(k)
    return result
    
lamb = 2.5
X = 5
print('%.3f' % poisson(lamb, X))

'''
The number of tickets purchased by each student for the University X vs. University Y football game\
follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left,
what is the probability that all 100 students will be able to purchase tickets?
'''

import math

def cdf(m, sd, x):
    result = (1 + math.erf((x - m) / (sd * math.sqrt(2)))) / 2
    return result

max_tickets = 250
n = 100
m = 2.4
sd = 2.0

# Central Limit Theorem
m = n * m
sd = math.sqrt(n) * sd

print('%.4f' % (cdf(m, sd, max_tickets)))


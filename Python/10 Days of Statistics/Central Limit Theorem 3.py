'''
You have a sample of 100 values from a population with mean 500 and with standard deviation 80.
Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words,
compute A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96.
'''

import math

n = 100 # Sample Size
m = 500 # Mean
sd = 80 # Standard Deviation
z = 1.96
moe = z * (sd / math.sqrt(n))   # Margin of Error

# Lower level (A)
print(round(m - moe, 2))
print(round(m + moe, 2))


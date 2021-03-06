'''
y1 = a + b1x11 + b2x21 + .. + bnxn1
y2 = a + b1x21 + b2x22 + .. + bnxn2
.
.


X = | 1 x11 x21 x31 ... xn1 |
    | 1 x21 x22 x32 ... xn3 |
    | 1 ..  .. ... ... ...  |

Y = |y1|
    |y2|
    |y3|

Y = XB

B = inv(X.T . X) . X.T . Y

'''

import numpy as np

m, n = [int(x) for x in input().split()]
x = []; X = []; Y = []

for i in range(n):
    x.append([float(x) for x in input().split()])
for i in range(n):
    X.append(x[i][:-1])
    
X =  np.c_[np.ones(n), np.array(X)]

for i in range(n):
    Y.append(x[i][-1])
    
Y = np.array(Y).reshape(-1,1)
B = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), Y)

q = int(input())
x_test = []
for i in range(q):
    x_test.append([float(x) for x in input().split()])
X_test = np.c_[np.ones(q), np.array(x_test)]

Y_test = np.dot(X_test, B)
for i in Y_test:
    print(round(i[0], 2))

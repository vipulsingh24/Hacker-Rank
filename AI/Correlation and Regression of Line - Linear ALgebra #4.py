import numpy as np

A = np.array([[4,5], [20, -9]])
b = bp.array([-33, 107])
res = np.linalg.solve(A, b)
print('x-mean: ', res[0])
print('y-mean: ', res[1])

# line of y on x
y_on_x = lambda x: 4/5 * x + 33/5

# line of x on y
x_on_y = lambda y: (9/20) * y + 107/20

print(x_on_y(7)) #8.5

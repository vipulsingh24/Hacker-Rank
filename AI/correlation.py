# Physics scores
x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
# History Score
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

def sum_list(lis):
    result = 0
    for i in lis:
        result += i
    return result

n = len(x)
sum_x = sum_list(x)
sum_y = sum_list(y)
sum_xy = sum_list([a * b for a, b in zip(x, y)])
sum_x2 = sum_list([a**2 for a in x]) # Summation x^2
sum_y2 = sum_list([a**2 for a in y]) # Summation y^2

num = (n * sum_xy) - (sum_x * sum_y)
denom = (((n*sum_x2 - (sum_x)**2)) * ((n*sum_y2 - (sum_y)**2)))**(1/2)
r = num/denom
print(r)


def rank(arr, n):
    rank = dict((j, i+1) for i, j in enumerate(sorted(set(arr))))
    return rank

def srcc(d, n):
    num = 6 * d
    denom = n * ((n ** 2) -1)
    result = 1 - (num / denom)
    return result
    
n = int(input())
x = [float(x) for x in input().split()]
y = [float(x) for x in input().split()]
rank_x = rank(x, n)
rank_y = rank(y, n)

rank_x = [rank_x[i] for i in x]
rank_y = [rank_y[i] for i in y]

sum_diff = 0
for i in range(n):
    sum_diff += ((rank_x[i] - rank_y[i]) ** 2)
print(round(srcc(sum_diff, n), 3))

def get_coordinates_for(matrix, val):
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col == val:
                return (x, y)

def nextMove(n,r,c,grid):
    princess = get_coordinates_for(grid, 'p')
    move = None
    row_diff = princess[0] - r
    col_diff = princess[1] - c
    if not row_diff == 0:
        if row_diff > 0:
            move = 'DOWN'
        else:
            move = 'UP'
    elif not col_diff == 0:
        if col_diff > 0:
            move = 'RIGHT'
        else:
            move = 'LEFT'
    return move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

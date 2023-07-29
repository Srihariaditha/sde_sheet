# Min Cost to react from one cell to another
##################################

def findMinCost(costs, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return costs[0][0]
    else:
        op2 = findMinCost(costs, row-1, col)
        op1 = findMinCost(costs, row, col-1)
        return costs[row][col] + min(op1, op2)


costs = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3]
]
print(findMinCost(costs, 3, 3))


# Number of ways to reach last cell with given cost
################################################################

def numOfPaths(costs, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if costs[0][0]-cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numOfPaths(costs, 0, col-1, cost - costs[row][col])
    elif col == 0:
        return numOfPaths(costs, row-1, 0, cost - costs[row][col])
    else:
        op1 = numOfPaths(costs, row-1, col, cost - costs[row][col])
        op2 = numOfPaths(costs, row, col-1, cost - costs[row][col])
        return op1 + op2


print(numOfPaths(costs, 3, 3, 25))

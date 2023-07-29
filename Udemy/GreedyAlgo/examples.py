# What is GA?
# Select the best first, second best next ....
# GA  is algo paradigm which builds the solution piece by piece
# in each step choose the piece which offersmost obvious and immediate benefit
# it fits perfectly for those solutions in which Local optimal solution leads to Global solution

# InsertionSort
################################


# selection sort
################################


# Topological sort
################################


# Prim's Algorithm
################################


# Kruskal's Algorithm
################################

# Activity Selection  Problem

def printMaxActivities(start, end):
    activities = []
    for i in range(len(start)):
        activities.append(['A'+str(i), start[i], end[i]])
    activities.sort(key=lambda x: x[2])
    i = 0
    print(activities[i][0])

    for j in range(len(activities)):
        # print(j)
        # print(activities)
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
        i = j


start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 9, 7, 9, 8]
printMaxActivities(start, end)
# start[]  =  {1, 3, 0, 5, 8, 5}, finish[] =  {2, 4, 6, 7, 9, 9};


# Coin Change Problems
################################

def getDenomination(coins, value):
    coins.sort(reverse=True)
    i = 0
    while True:
        if value >= coins[i]:
            print(coins[i])
            value -= coins[i]
        else:
            i += 1
        if i >= len(coins):
            print("Cannot find denominations exactly")
            break
        if value == 0:
            break


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]

getDenomination(coins, 3888)


# Fractional Knapsack Problem
################################
class Item:
    def __init__(self, wt, val):
        self.weight = wt
        self.val = val
        self.ratio = val/wt


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.val, reverse=True)
    usedCapacity = 0
    totalVal = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalVal += i.val
        else:
            unusedCapacity = capacity - usedCapacity
            value = i.ratio * unusedCapacity
            totalVal += value
            usedCapacity = capacity + unusedCapacity
        if usedCapacity == capacity:
            break
# print knapsackMethod(i, 50)

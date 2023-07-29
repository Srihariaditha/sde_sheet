# Zero one knapsack problem
################################


class Item:
    def __init__(self, wt, profit):
        self.weight = wt
        self.profit = profit


def zoKnapsack(items, capacity, index):
    if capacity <= 0 or index < 0 or index >= len(items):
        return 0
    elif capacity >= items[index].weight:
        profit1 = items[index].profit + \
            zoKnapsack(items, capacity -
                       items[index].weight, index+1)
        profit2 = zoKnapsack(items, capacity, index+1)
        return max(profit1, profit2)
    else:
        return 0


mango = Item(3, 30)
orange = Item(5, 25)
banana = Item(8, 45)
apple = Item(6, 65)

items = [mango, orange, banana, apple]

print(zoKnapsack(items, 13, 0))

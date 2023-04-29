import argparse

class Item:
    def __init__(self, name, cost, weight):
        self.name = name
        self.cost = cost
        self.weight = weight
    def __repr__(self):
        return f'Item({self.name}, {self.cost}, {self.weight})'
    
items = []
def add_item(name, cost, weight):
    global items
    items.append(Item(name, cost, weight))

parser = argparse.ArgumentParser()
                     
parser.add_argument('--max_weight', type=int, default=10)
parser.add_argument('--items', nargs='+', default=[])
parser.add_argument('--costs', nargs='+', default=[])
parser.add_argument('--weights', nargs='+', default=[])

def process_knap(max_weight):
    global items
    backpack = []
    total_cost = 0
    total_weight = 0
    for item in items:
        if total_weight + item.weight <= max_weight:
            backpack.append(item)
            total_weight += item.weight
            total_cost += item.cost
    return backpack, total_weight

args = parser.parse_args()

if args.items:
    for item, cost, weight in zip(args.items, args.costs, args.weights):
        add_item(item, int(cost), int(weight))
else:
    print("No items added")
    exit(1)


backpack, total_weight = process_knap(args.max_weight)
print(f'Backpack: {backpack}')
print(f'Total weight: {total_weight}')
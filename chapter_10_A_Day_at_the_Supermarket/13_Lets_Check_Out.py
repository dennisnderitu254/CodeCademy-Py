shopping_list = ["banana", "orange", "apple"]

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    costs = 0.0
    for item in food:
        if stock[item] > 0:
            stock[item] -= 1
            costs += prices[item]
    
    return costs
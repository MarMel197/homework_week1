# WRITE YOUR FUNCTIONS HERE

# Test 1:Get petshop name
def get_pet_shop_name(list):
    return list["name"]

# Test 2: Get total cash 
def get_total_cash(list):
    total_cash = 0
    for sold in list():
        total_cash += sold["cash"]
    return total_cash

# Test 3 and 4: Add or remove cash 
def add_or_remove_cash(list, cash):
    total_cash = list["total_cash"]
    if cash >= 0:
        total_cash += cash
    elif cash < 0:
        total_cash -= cash
    else:
        total_cash = total_cash
    return total_cash

# Test 5: Get pets sold
def get_pets_sold(list):
    sold_pets = []
    for sales in list:
        sold_pets = sales["name"]
    return sold_pets


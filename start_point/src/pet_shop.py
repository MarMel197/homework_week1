import pdb

# Test 1:Get petshop name
def get_pet_shop_name(list):
    return list["name"]

# Test 2: Get total cash 
def get_total_cash(list):
    return list["admin"]["total_cash"]

# Test 3 and 4: Add or remove cash 
# def add_or_remove_cash(list, cash):
#     total_cash = list["admin"]["total_cash"] 
#     print(total_cash)
    
# Test 5: Get pets sold
def get_pets_sold(list):
    return list["admin"]["pets_sold"]

# Test 6: Increase pets sold
def increase_pets_sold(list, sale):
    total_sales = list["admin"]["pets_sold"]
    total_sales += sale
    list["admin"]["pets_sold"] = total_sales

# Test 7: Get stock count
def get_stock_count(list):
    return len(list["pets"])

def get_pets_by_breed(list, breed):
    breed_list = []
    for pet in list["pets"]:
        if pet["breed"] == breed:
            breed_list.append(["breed"])
    
    return breed_list

# Test 10 & 11: Find pet by name

def find_pet_by_name(list, pet_name):
    for name in list["pets"]:
        if name["name"] == pet_name:
            return name

# Test 12: Remove pet by name

def remove_pet_by_name(list, pet_name):
    for pet in list["pets"]:
        if pet["name"] == pet_name:
            list["pets"].remove(pet)

# Test 12: Add pet to stock

def add_pet_to_stock(list, new_pet):
    list["pets"].append(new_pet)

# Test 13: Get cutomer cash

def get_customer_cash(list):
    return list["cash"]

# Test 14: Remove customer cash
def remove_customer_cash(list, cash_sale):
    cust_cash = list["cash"]
    cust_cash -= cash_sale
    list["cash"] = cust_cash

#Test 15: Get customer pet count








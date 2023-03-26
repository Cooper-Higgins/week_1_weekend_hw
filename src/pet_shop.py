# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Feel like I'm overcomplicating this but been at it for hours and can't get it (it fails)
# Tried it as updating a dictionary entry, but kept getting string and integer errors
def add_or_remove_cash(pet_shop, transaction):
    total_cash = pet_shop["admin"]["total_cash"]
    transaction = input(int())
    if transaction > 0:
        new_balance = total_cash + transaction
    elif transaction < 0:
        new_balance = total_cash - transaction
    return new_balance

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Doesn't work, returning 0 - like sales as a variable isn't adding
def increase_pets_sold(pet_shop, sales):
    sales = 2
    total_sales = pet_shop["admin"]["pets_sold"] + sales
    return total_sales

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# Also doesn't work, I think the test wants it as a length of a list but it's returning 4?
def get_pets_by_breed(pet_shop, breed):
    pets = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets += pet["breed"]
        else:
            pass

    return len(pets)

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet["name"] = None
    return

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return len(pet_shop["pets"])

def get_customer_cash(customers):    
    return customers["cash"]

# Not working, same integer / string issue as earlier - feel like I'm just using the wrong method
def remove_customer_cash(customers, removed_cash):
    removed_cash = 100
    return print(customers["cash"] - removed_cash)
    
def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

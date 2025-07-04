run = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

coin = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * coin["quarters"]
    dimes = int(input("How many dimes? ")) * coin["dimes"]
    nickels = int(input("How many nickels? ")) * coin["nickels"]
    pennies = int(input("How many pennies? ")) * coin["pennies"]

    total = quarters + dimes + nickels + pennies
    return total

def make_coffee(coffee_type):
    if coffee_type not in MENU:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
        return False
    
    # Check if resources are sufficient
    for ingredient, amount in MENU[coffee_type]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    
    #calculate the cost and process coins
    cost = MENU[coffee_type]["cost"]
    process_coins = process_coins()
    if process_coins < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = process_coins - cost
        print(f"Here is ${change:.2f} in change.")
        resources["money"] += cost

    # Deduct ingredients from resources
    for ingredient, amount in MENU[coffee_type]["ingredients"].items():
        resources[ingredient] -= amount
    
    # Serve the coffee
    if coffee_type == "espresso":
        print("Here is your espresso ☕. Enjoy!")
    elif coffee_type == "latte":
        print("Here is your latte ☕. Enjoy!")
    elif coffee_type == "cappuccino":
        print("Here is your cappuccino ☕. Enjoy!")




while run:
    print("What whould you like? (espresso/latte/cappuccino):")
    choice = input().lower()

    if choice == "off":
        run = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
    else: 
        make_coffee(choice)

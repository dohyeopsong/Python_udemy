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

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def process_coins():
    """Prompt user to insert coins and calculate the total value."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * COINS["quarters"]
    dimes = int(input("How many dimes? ")) * COINS["dimes"]
    nickels = int(input("How many nickels? ")) * COINS["nickels"]
    pennies = int(input("How many pennies? ")) * COINS["pennies"]

    total = quarters + dimes + nickels + pennies
    return total


def check_resources(coffee_type):
    """Check if there are enough resources to make the selected coffee."""
    for ingredient, amount in MENU[coffee_type]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def make_coffee(coffee_type):
    """Process the coffee order if possible."""
    if coffee_type not in MENU:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
        return False
    
    # Check if resources are sufficient
    if not check_resources(coffee_type):
        return False
    
    # Calculate the cost and process coins
    cost = MENU[coffee_type]["cost"]
    print(f"The cost is ${cost:.2f}.")
    payment = process_coins()
    
    if payment < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    
    # Process payment and give change
    change = payment - cost
    print(f"Here is ${change:.2f} in change.")
    resources["money"] += cost

    # Deduct ingredients from resources
    for ingredient, amount in MENU[coffee_type]["ingredients"].items():
        resources[ingredient] -= amount
    
    # Serve the coffee
    print(f"Here is your {coffee_type} ☕. Enjoy!")
    return True


def display_report():
    """Display the current resource levels."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def main():
    """Run the coffee machine program."""
    running = True
    
    while running:
        print("\nWhat would you like? (espresso/latte/cappuccino):")
        choice = input().lower()

        if choice == "off":
            running = False
            print("Coffee machine shutting down...")
        elif choice == "report":
            display_report()
        else:
            make_coffee(choice)


if __name__ == "__main__":
    main()

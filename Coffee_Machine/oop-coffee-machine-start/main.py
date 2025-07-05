from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    menu_items = menu.get_items()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    running = True

    while running:
        choice = input(f"What would you like? ({menu_items}):").lower()

        if choice == "off":
            running = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
                else:
                    print("Sorry, not enough resources to make that drink.")
            else:
                print("Invalid choice. Please select a valid drink.")
    print("Coffee machine shutting down...")
if __name__ == "__main__":
    main()
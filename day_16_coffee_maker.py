from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
money_machine.report()
my_drink = CoffeeMaker()
my_drink.report()
menu = Menu()
IsOn = True
while IsOn:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == "off":
        IsOn = False
    elif choice == "report":
        my_drink.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_drink.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                my_drink.make_coffee(drink)

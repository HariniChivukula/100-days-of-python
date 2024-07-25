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
}

profit = 0


def is_resource_enough(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry not enough {item}.")
            return False

    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here's your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money. Amount refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}. Enjoy!")


machine_on = True

while machine_on:
    user_choice = input("What would you like? Espresso/latte/cappuccino ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_enough(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(user_choice,drink['ingredients'])
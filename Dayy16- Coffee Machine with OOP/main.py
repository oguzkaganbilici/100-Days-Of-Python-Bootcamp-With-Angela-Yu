from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = True

choice = CoffeeMaker()
current = MoneyMachine()
menu1 = Menu()

while flag:
    text = "What would you like? (" + menu1.get_items() + ")"
    order = input(text)
    if order == "report":
        choice.report()
        current.report()

    elif order == "off":
        print("Maintance mod")
        flag = False
    else:
        cost = menu1.find_drink(order)
        if order == "espresso":
            if choice.is_resource_sufficient(cost) and current.make_payment(cost.cost) == True:
                choice.make_coffee(cost)

        elif order == "latte":
            if choice.is_resource_sufficient(cost) and current.make_payment(cost.cost):
                choice.make_coffee(cost)

        elif order == "cappuccino":
            if choice.is_resource_sufficient(cost) and current.make_payment(cost.cost):
                choice.make_coffee(cost)

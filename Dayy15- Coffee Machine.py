# -*- coding: utf-8 -*-
"""
Created on Sat May 21 13:36:29 2022

@author: 061885
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}

menu = MENU
resc = resources

def fee(menu,choice):
    water, milk,coffee = ingredients(menu, choice)
    r_water, r_milk,r_coffee,r_money = Resources(resc)
    
    if water > r_water:
        print("Sorry, there is not enough water")
        return 0
    elif milk > r_milk:
        print("Sorry, there is not enough milk")
        return 0
    elif coffee > r_coffee:
        print("Sorry, there is not enough cofee")
        return 0
    else:     
        fee = menu[choice]["cost"]
        print(f"Your cost is ${fee}")
        print("Please insert the coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * .25 + dimes * .1 + nickles * .5 + pennies * .01
        change = round(total - fee,2)
        if total > fee:
            print(f"Cost is {fee}. Here is {change} change. Don't forget it.")
            print("Here is your espresso.☕  Enjoy!")
            r_water -= water
            r_milk -= milk
            r_coffee -= coffee
            r_money += fee
            updateResources(resc, r_water, r_milk, r_coffee,r_money)
        elif total == fee:
            print(f"Here is your {choice}.☕  Enjoy!")
            r_water -= water
            r_milk -= milk
            r_coffee -= coffee
            r_money += fee
            updateResources(resc, r_water, r_milk, r_coffee,r_money)
        else:
            print("Sorry. That's not enough money. Money is refunded")

def ingredients(menu, choice):
    water = menu[choice]["ingredients"]["water"]
    milk = menu[choice]["ingredients"]["milk"]
    coffee = menu[choice]["ingredients"]["coffee"]
    return water,milk,coffee

def Resources(rr):
    r_water = rr["water"]
    r_milk = rr["milk"]
    r_coffee = rr["coffee"]
    r_money = rr["money"]
    return r_water, r_milk, r_coffee,r_money

def updateResources(rr, water,milk,coffee,money):
    rr["water"] = water
    rr["milk"] = milk
    rr["coffee"] = coffee
    rr["money"] = money
    
def addResources(rr, water,milk,coffee):
    rr["water"] += water
    rr["milk"] += milk
    rr["coffee"] += coffee
    
flag = True
while flag:
    choice = input("What would you like? (espresso, latte, cappuccino):")
    if choice == "report": 
        r_water, r_milk,r_coffee,r_money = Resources(resc)
        print(f"Water:{r_water} ml \nMilk:{r_milk} ml \nCoffee:{r_coffee} ml\nMoney:${r_money} ")
    elif choice == "add":
        wat = int(input("add water: "))
        mil = int(input("add milk: "))
        cof = int(input("add coffee: "))
        addResources(resc, wat, mil, cof)
    elif choice == "off":
        print("Maintenance Mode")
        flag = False
    else:
        xx = fee(menu, choice)

        
    
    
    
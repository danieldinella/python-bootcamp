from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
mm = MoneyMachine()
cm = CoffeeMaker()

user_input = input("What would you like? (" + m.get_items() + ") ")
while user_input != "off":
    if user_input.lower() == "report":
        mm.report()
    else:
        drink = m.find_drink(user_input)
        if not cm.is_resource_sufficient(drink):
            break
        else:
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)
    user_input = input("What would you like? (" + m.get_items() + ") ")



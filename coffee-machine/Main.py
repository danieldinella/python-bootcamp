MENU = {
    "espresso": {
        "ingredients": {
            "water": 500,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Controllo risorse
def check_resources(user_input):
    for mKey, mValue in MENU[user_input]["ingredients"].items():
            if mValue > resources[mKey]:
                print("Sorry, there is not enough " + str(mKey))
                return False
    return True

#Controllo pagamento
def transaction(user_input):
    print("Please, insert coins.")
    myMoney = int(input("How many quarters? ")) * 0.25
    myMoney += int(input("How many dimes? ")) * 0.1
    myMoney += int(input("How many nickels? ")) * 0.05
    myMoney += int(input("How many pennies? ")) * 0.01
    if myMoney < MENU[user_input]["cost"]:
        print("Sorry, that is not enough money. Money refund.")
        return False
    elif myMoney > MENU[user_input]["cost"]:
        print("Here is your change: £" + str(myMoney))
    return True

#Report sulle risorse della macchina
def report():
    for key, value in resources.items():
        print(str(key) + ": " + str(value))
    print(profit)
    return

#Main
user_input = input("What would you like? ")
while user_input != "off":
    if user_input.lower() == "report":
        report()
    elif not check_resources(user_input):
        break
    else:
        if transaction(user_input):
            print("Here is your " + user_input + " ☕. Enjoy!")
    user_input = input("What would you like? ")



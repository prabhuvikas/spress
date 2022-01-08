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
    "coffee": 100
}
money = 0
machine_status = True

## TODO 1 Select Coffee
def selectCoffee():
    choice = input("Which coffee would you like today?(espresso/latte/cappuccino):")
    return choice
## Todo 2 turn off the machine
def machine_off():
    choice = input("Would you like to turn off the machine?yes/no")
    if choice == 'yes':
        return False
    else:
        return True

## Todo 3 Print report
def print_report(resources,money):
    print(f"Water:{resources['water']}ml")
    print(f"Milk:{resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}g")
    print(f"Money:${money}")

## Todo 4 Brew Coffee function with type
def brew_coffee(coffee,resource):
    for key in coffee:
        resource[key] -= coffee[key]
    return resource
## Todo 5 Process payment
def process_payment(amount ,coffee_money,holding):
    if amount < coffee_money:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else :
        change = amount - coffee_money
        print(f"Here is ${change} dollars in change.")
    return holding + coffee_money
## Todo 6 Accept Payment
def accept_payment():
    penny = int(input("How many pennies?"))
    dime = int(input("How many dimes?"))
    nickel = int(input("How many nickels?"))
    quarter = int(input("How many quarters?"))
    total = penny*.01 + dime*.10 + nickel*.05 + quarter*.25
    return total

## Todo 7 Check resources
def check_resources(resources,ctypedata):
    for key in ctypedata:
        if ctypedata[key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True
while machine_status:
    choice = selectCoffee()
    if choice == "off":
        machine_off()
    elif choice == "report":
        print_report(resources,money)
    elif not check_resources(resources,MENU[choice]["ingredients"]) :
        continue
    else:
        money_input = accept_payment()
        accept = process_payment(money_input,MENU[choice]["cost"],money)
        if accept > 0 :
            print_report(resources,money)
            money = accept
            resources = brew_coffee(MENU[choice]["ingredients"],resources)
            print(f"Here is your {choice}. Enjoy!")
            print_report(resources, money)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def machine():
    menu = Menu()
    coffe_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    machine_on = True

    while(machine_on):
        answer = input("What would you like?(espresso/latte/cappuccino/):")
        if answer == 'off':
            machine_on = False
        elif answer == 'report':
            coffe_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(answer)
            if drink and coffe_maker.is_resource_sufficient(drink):
                coffe_maker.make_coffee(drink)
                money_machine.make_payment(drink.cost)
                


machine()

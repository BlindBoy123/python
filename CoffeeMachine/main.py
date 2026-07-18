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


# TODO: 2. create an off prompt
def offline():
    print(f'code accepted. coffee maker going offline...')
    return machine_status == False


# TODO: 3. print report
def report():
    print(f"report \n-----------------\nwater: {WATER}\nmilk: {MILK}\ncoffee: {COFFEE}\nmoney: R{total_earnings}\n")
    return None

# TODO: 4. resources
def compare_ingredients(user, water, milk, coffee):
    """checks the resources dict for sufficient ingredients needed for drink"""

    if water < espWater and user == 'espresso':
        print(f'espresso cannot be made. error: water')
    elif coffee < espCoffee and user == 'espresso':
        print('no espresso. error: coffee')

    if water < latteWater and user == 'latte':
        print('no latte. error: water')
    elif milk < latteMilk and user == 'latte':
        print('no latte. error: milk')
    elif coffee < latteCoffee and user == 'latte':
        print('no latte. error: coffee')

    if water < cappWater and user == 'cappuccino':
        print('no cappuccino. error: water')
    elif milk < cappMilk and user == 'cappuccino':
        print('no cappuccino. error: milk')
    elif coffee < cappCoffee and user == 'cappuccino':
        print('no cappuccino. error: coffee')

    return None

# TODO: 5. process coins
def payment(cash,paid,pennies,nickles,dimes,quarters):
    """takes in coins as payment and validates enough coins per drink"""
    print('please insert coins: ')
    pennies = int(input('how many pennies: '))
    nickles = int(input('how many nickles: '))
    dimes = int(input('how many dimes: '))
    quarters = int(input('how many quarters: '))

    number_of_pennies = pennies * 0.01
    number_of_nickles = nickles * 0.05
    number_of_dimes = dimes * 0.1
    number_of_quarters = quarters * 0.25

    paid = number_of_pennies + number_of_nickles + number_of_dimes + number_of_quarters

    cash = cash + paid
    print(f'you have inserted: {paid}')

    return None


# TODO: 6. check transaction
def check_transaction(total, coins, espresso, latte, cappuccino):
    if total < espresso:
        print(f'no espresso. payment error, return {total}')
        total = total - coins

    return None

                            # """                             MAIN                            """

# TODO: 1. prompt user

total_earnings = 0.0
coins_inserted = 0.0

penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25

espressoPrice = MENU["espresso"]['cost']
lattePrice = MENU["latte"]['cost']
cappuccinoPrice = MENU["cappuccino"]['cost']

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]

espWater = MENU["espresso"]['ingredients']['water']
espCoffee = MENU["espresso"]['ingredients']['coffee']

latteWater = MENU["latte"]['ingredients']['water']
latteMilk = MENU["latte"]['ingredients']['milk']
latteCoffee = MENU["latte"]['ingredients']['coffee']

cappWater = MENU["cappuccino"]['ingredients']['water']
cappMilk = MENU["cappuccino"]['ingredients']['milk']
cappCoffee = MENU["cappuccino"]['ingredients']['coffee']

machine_status = True

while machine_status:
    print('welcome to the midnight coffee machine!\n---------------------')
    user_choice = input(f"what would you like? ('espresso'/'latte'/'cappuccino'): \n")

    if user_choice == 'off':
        machine_status = offline()
    elif user_choice == 'report':
        report()
    elif user_choice == 'espresso':
        compare_ingredients(user_choice,WATER,MILK,COFFEE)
        payment(total_earnings, coins_inserted, penny, nickel, dime, quarter)
        check_transaction(coins_inserted, total_earnings, espressoPrice, lattePrice, cappuccinoPrice)
        if machine_status:
            print(f'\nthank you and enjoy\n---------------------------------')
    elif user_choice == 'latte':
        compare_ingredients(user_choice,WATER,MILK,COFFEE)
        payment(total_earnings, coins_inserted, penny, nickel, dime, quarter)
        if machine_status:
            print(f'\nthank you and enjoy\n---------------------------------')
    elif user_choice == 'cappuccino':
        compare_ingredients(user_choice,WATER,MILK,COFFEE)
        payment(total_earnings, coins_inserted, penny, nickel, dime, quarter)
        if machine_status:
            print(f'\nthank you and enjoy\n---------------------------------')
    else:
        print('invalid option, please restart')


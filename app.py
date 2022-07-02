from utils import database

print('Welcome to ECB Exchange Rate Checker!')
print('Please enter your choice')
print()
USER_CHOICE = """
Enter:
- 's' check specified rate'
- 'a' see all rates'
- 'q' to quit
Your choice: """


def menu():
    database.create_db_table()
    database.add_daily_rates()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 's':
            prompt_get_rate()
        elif user_input == 'a':
            prompt_get_allrates()
        user_input = input(USER_CHOICE)


def prompt_get_rate():
    single_rate = input('Which ECB Rate do you want to check?: ')
    rate = database.get_rate(single_rate)
    for i in rate:
        print()
        print(f"With rates of {i['Date']} 1€ is {i['Rate']} {i['Currency']}")


def prompt_get_allrates():
    for rates in database.get_all_rates():
        print(f"With rates of {rates['Date']}: 1€ is {rates['Rate']} {rates['Currency']}")


menu()
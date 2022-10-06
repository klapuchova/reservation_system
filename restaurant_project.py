import os
from datetime import datetime
from cryptography.fernet import Fernet

def parse_user_date(raw_datetime: str, formats: list[str]) -> datetime | None:
    for format in formats:
        try:
            return datetime.strptime(raw_datetime, format)
        except ValueError:
            pass

def get_date() -> str:
    supported_date_formats = ['%d.%m.%Y', '%d/%m/%Y']
    while True:
        date_raw = input('Write a date of your visit:').replace(" ", "")
        datetime_object = parse_user_date(date_raw, supported_date_formats)
        if datetime_object is not None:
            return datetime_object.strftime("%d.%m.%Y")
        print('Wrong format of the date, please try again.')


def get_whole_name() -> str:
    while True:
        whole_name = input('What is your whole name?')
        if ' ' in whole_name:
            return whole_name
        print('Fill your first name and last name')

def complete_reservation() -> dict[str:str]:
    reservation_completed = {}
    reservation_completed[get_whole_name()] = get_date()
    print('Reservation completed:')
    print(reservation_completed)
    print('We will contact you with confirmation soon.')


def write_reservation_to_file():
    f_loc = r"C:\Users\42073\IdeaProjects\reservation_system\reservation_data.txt"
    if not os.path.exists(f_loc):
        open(f_loc, 'w').close()
    with open('reservation_data.txt', mode='a+', encoding='utf-8') as f:
        print(complete_reservation(), file=f)

def get_user_email() -> str:
    while True:
        email = input('\tWhat is your email?')
        if '@' and '.' in email:
            return email
        else:
            print('Wrong email format')


menu = {
    1: {'option_1': {'starters': ['Mezze Classic'], 'main': ['Mix Grill'], 'dessert': ['Baklava'], 'wine': 'Santorini'},
        'option_2': {'starters': ['Flogeres'], 'main': ['Kebab'], 'dessert': ['Kataifi'], 'wine': 'Retsina'}},

    2: {'option_1': {'starters': ['Feta Psiti', 'Pantsari'], 'main': ['Moussakas', 'Paidhakia'],
                     'dessert': ['Pagoto', 'Baklava'], 'wine': 'Rapsani'},
        'option_2': {'starters': ['Hummus', 'Kafteri'], 'main': ['Stifado', 'Katsikaki sto furno'],
                     'dessert': ['Cheesecake', 'Fruits'], 'wine': 'Nemea'}},

    3: {'option_1': {'starters': ['Tzatziki', 'Challoumi', 'Elies'], 'main': ['Moussakas', 'Gyros', 'Kebab'],
                     'dessert': ['Sokolatina'], 'wine': 'Ovilos'},
        'option_2': {'starters': ['Chorta', 'Dakos'], 'main': ['Souvlaki', 'Arnaki psito'],
                     'dessert': ['Giaurti', 'Galaktoboureko'], 'wine': 'Mavroudi'}},

    4: {'option_1': {'starters': ['Thalasino mezzes', 'Gavros'], 'main': ['Piato Poseidon'],
                     'dessert': ['Ellinika Glyka'], 'wine': 'Biblia Chora'},
        'option_2': {'starters': ['Burekakia', 'Choriatiki'], 'main': ['Elliniko piato'], 'dessert': ['Fruits'],
                     'wine': 'Xinomavro'}}
}


while True:
    try:
        number_of_guests = int(input('Please insert number of guests: '))
        if number_of_guests < 1:
            raise ValueError
    except ValueError:
        print("Please write only a number")
        continue
    if number_of_guests > 4:
        print('Please contact us, for more than 4 people you can not use the application')
        break

    for option, offers in menu[number_of_guests].items():
        starter_list = offers['starters']
        print(f"\nThe {option} consists of:")
        print(f"the first course is:")
        for one_starter_option in starter_list:
            starter = one_starter_option
            print(f"\t{starter}")

        main_list = offers['main']
        print("\n", end="")
        print(f"the second course is:")
        for one_main_option in main_list:
            main = one_main_option
            print(f"\t{main}")

        dessert_list = offers['dessert']
        print("\n", end="")
        for one_dessert_option in dessert_list:
            dessert = one_dessert_option
            print(f"\t the third course is: {dessert}", end="")

        wine = offers['wine']
        print(f"\n\t and the sommelier will open for you a bottle of {wine} wine.")


    option_menu = int(input('Please select your option (1 or 2)? '))
    if option_menu in (1, 2):
        print(f'You have selected option {option_menu}, good choice!')
        write_reservation_to_file()
    else:
        print("Haven't you chosen? Please contact us by phone. We are sure that we will find some option for you.")
    break
print('Thank you for using our system to book a table:)')

registration_info = {}
while True:
    register = input("Would you like to register? (yes/no)")
    if register.lower() == 'yes':
        key = Fernet.generate_key()
        f = Fernet(key)
        user_email = get_user_email()
        password = input('\tFill your password: ')
        password_as_bytes = str.encode(password)
        encrypt_value = f.encrypt(password_as_bytes)
        print(f"Your email for sign up is {user_email}. We secure your password encrypted {encrypt_value.decode()[:10]}. Thank you for registration!")
        break
    elif register in ('no', 'No', 'NO'):
        print('We are really sorry, maybe next time :)')
        break
    else:
        print('We do not understand, please answer "yes" or "no"')
        continue




import re
from getpass import getpass


def get_password_len(password_len):
    if password_len <= 4:
        return 1
    elif 5 < password_len <= 9:
        return 2
    else:
        return 3


def get_password_symbol(password, regular_expression):
    find_symbol = re.findall(regular_expression, password)
    find_symbol_len = len(find_symbol)
    if find_symbol_len >= 3:
        strength = 3
    elif 0 < find_symbol_len < 3:
        strength = 1
    else:
        strength = 0
    return strength


def get_password_strength(password):
    password_len = len(password)
    password_len = get_password_len(password_len)

    uppercase = get_password_symbol(password, r'[A-Z]')
    numeric = get_password_symbol(password, r'[0-9]')
    symbol = get_password_symbol(password, r'[@,#,$,%,^,&,*,\-,_,`,~]')
    strength = password_len + uppercase + numeric + symbol

    return strength


if __name__ == '__main__':
    user_password = getpass('Введите пароль: ')
    print('Сложность пароля:', get_password_strength(user_password))

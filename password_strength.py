import re

MIN_RESULT_VALUE = 1
MID_RESULT_VALUE = 2
MAX_RESULT_VALUE = 3


def get_password_len(password_len):
    if password_len <= 4:
        return MIN_RESULT_VALUE
    elif 5 < password_len <= 9:
        return MID_RESULT_VALUE
    else:
        return MAX_RESULT_VALUE


def get_password_uppercase(password):
    uppercase = re.findall(r'[A-Z]', password)
    uppercase_len = len(uppercase)
    if uppercase_len >= 3:
        uppercase = MAX_RESULT_VALUE
    elif 0 < uppercase_len < 3:
        uppercase = MIN_RESULT_VALUE
    else:
        uppercase = 0
    return uppercase


def get_password_numeric(password):
    numeric = re.findall(r'[0-9]', password)
    numeric_len = len(numeric)
    if numeric_len >= 3:
        numeric = MAX_RESULT_VALUE
    elif 0 < numeric_len < 3:
        numeric = MIN_RESULT_VALUE
    else:
        numeric = 0
    return numeric


def get_password_symbol(password):
    symbol = re.findall(r'[@,#,$,%,^,&,*,\-,_,`,~]', password)
    symbol_len = len(symbol)
    if symbol_len:
        symbol = MIN_RESULT_VALUE
    else:
        symbol = 0
    return symbol


def get_password_strength(password):
    password_len = len(password)
    password_len = get_password_len(password_len)
    uppercase = get_password_uppercase(password)
    numeric = get_password_numeric(password)
    symbol = get_password_symbol(password)
    strength = password_len + uppercase + numeric + symbol

    return strength


if __name__ == '__main__':
    user_password = input('Введите пароль: ')
    print('Сложность пароля:',get_password_strength(user_password))

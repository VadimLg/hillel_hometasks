import random

symbols = ""
switch_upper = (0,)
digits = '0123456789'
latin = 'abcdefghijklmnopqrstuvwxyz'
cyrillic = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

cyrillic_flag = int(input("Будемо використовувати кирилицю? (1- так / 0 - ні): "))
latin_flag = int(input("Будемо використовувати латиницю? (1- так / 0 - ні): "))
digits_flag = int(input("Будемо використовувати цифри? (1- так / 0 - ні): "))
if cyrillic_flag == 1 or latin_flag == 1:
    upper_flag = int(input(
        "Будемо використовувати маленькі, великі чи великі і маленькі літери? (0 - маленькі / 1- великі / 2 - великі і маленькі): "))
password_quantity = int(input("Яка кількість символів має бути у паролі?: "))

if cyrillic_flag == 1:
    symbols += cyrillic

if latin_flag == 1:
    symbols += latin

if digits_flag == 1:
    symbols += digits

if upper_flag == 0:
    switch_upper = (0,)
elif upper_flag == 1:
    switch_upper = (1,)
elif upper_flag == 2:
    switch_upper = (0, 1)


def gen_pas(symbols_used: str, quantity: int, switch) -> str:
    pas = ""
    symbols_list = list(symbols_used)
    for i in range(quantity):
        if random.sample(switch, k=1) == [1]:
            pas += random.choice(symbols_used).upper()
        else:
            pas += random.choice(symbols_used)
    return pas


if symbols != "":
    print(f"Пароль: {gen_pas(symbols, password_quantity, switch_upper)}")
else:
    print("Не вибрано жодного набору символів для генерації пароля!")




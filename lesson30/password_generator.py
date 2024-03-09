import random

symbols_used = ""
digits = '0123456789'
latin = 'abcdefghijklmnopqrstuvwxyz'
cyrillic = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

cyrillic_flag = int(input("Будемо використовувати кирилицю? (1- так / 0 - ні): "))
if cyrillic_flag == 1:
    big_or_small_cyrillic = int(
        input("Будемо використовувати великі чи маленькі символи кирилиці? (1- великі / 0 - маленькі): "))
    if big_or_small_cyrillic == 1:
        symbols_used += cyrillic.upper()
    else:
        symbols_used += cyrillic

latin_flag = int(input("Будемо використовувати латиницю? (1- так / 0 - ні): "))
if latin_flag == 1:
    big_or_small_latin = int(
        input("Будемо використовувати великі чи маленькі символи латиниці? (1- великі / 0 - маленькі): "))
    if big_or_small_latin == 1:
        symbols_used += latin.upper()
    else:
        symbols_used += latin

digits_flag = int(input("Будемо використовувати цифри? (1- так / 0 - ні): "))
if digits_flag == 1:
    symbols_used += digits

password_quantity = int(input("Яка кількість символів має бути у паролі?: "))


def gen_pas(symbols: str, quantity: int) -> str:
    pas = ""
    symbols_list = list(symbols)
    for i in range(quantity):
        pas += "".join(random.sample(symbols_list, k=1))
    return pas


if symbols_used != "":
    print(f"Пароль: {gen_pas(symbols_used, password_quantity)}")
else:
    print("Не вибрано жодного набору символів для генерації пароля!")

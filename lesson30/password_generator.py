import random

symbols = ""
digits = '0123456789'
latin = 'abcdefghijklmnopqrstuvwxyz'
cyrillic = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

cyrillic_flag = int(input("Будемо використовувати кирилицю? (1- так / 0 - ні): "))
latin_flag = int(input("Будемо використовувати латиницю? (1- так / 0 - ні): "))
digits_flag = int(input("Будемо використовувати цифри? (1- так / 0 - ні): "))
upper_flag = int(input("Будемо використовувати великі чи маленькі літери? (1- великі / 0 - маленькі): "))
password_quantity = int(input("Яка кількість символів має бути у паролі?: "))

if cyrillic_flag == 1:
    symbols += cyrillic

if latin_flag == 1:
    symbols += latin

if digits_flag == 1:
    symbols += digits

if upper_flag == 1:
    symbols = symbols.upper()


def gen_pas(symbols_used: str, quantity: int) -> str:
    pas = ""
    symbols_list = list(symbols_used)
    for i in range(quantity):
        pas += "".join(random.sample(symbols_list, k=1))
    return pas


if symbols != "":
    print(f"Пароль: {gen_pas(symbols, password_quantity)}")
else:
    print("Не вибрано жодного набору символів для генерації пароля!")

print("Lessson 4 Задача 3")
#
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована. Використовуйте цикл while.

# Правильний ПІН-код
pin = 1234
# Максимальна кількість спроб введення ПІН-коду
attempt_pin = 3
print("Введіть ПІН-код, всього 3 спроби.")


def pin_checking(pin_in: int) -> int:
    if pin_in == pin:
        return 1
    else:
        return 0


def message_printing(pin_check: int, attempt_pin: int) -> str:
    if pin_check == 1:
        return str("ПІН-код правильний!")
    elif pin_check == 0 and attempt_pin != 0:
        return str("Введено неправильний ПІН-код!")
    elif pin_check == 0 and attempt_pin == 0:
        return str("Введено неправильний ПІН-код!\nКарта заблокована!")


while attempt_pin > 0:
    pin_in = int(input(f"{4 - attempt_pin}-я спроба: "))
    attempt_pin -= 1
    pin_check = pin_checking(pin_in)
    print(message_printing(pin_check, attempt_pin))
    if pin_check == 1:
        break


print()
print("Lessson 3 Задача 1")
#
# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс,
# памятайте що користувач не знає що в нас індекси починаються з нуля)
# Також нам відомо що цей список має пять або більше елементів.
# Після кожного видалення елементу виводьте наш оновлений список.
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.
# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик. і виведіть їх на екран.
# Але цього разу вже без видалень.
# кроки:
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось

def add_products(grocery_list: list, add_list: list) -> list:
    return grocery_list + add_list


def product_removal(product_number: int):
    grocery_list.pop(int(product_number) - 1)


def print_current_products():
    if len(grocery_list) > 0:
        print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")


grocery_list = input(
    "Напишіть продукти (5 або більше), які потрібно купити, використовуйте пробіл як роздільник: ").split()

if len(grocery_list) >= 5:
    # Відображає список доданих продуктів.
    print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")
    product_all_removal_flag = input('Бажаєте видалити з корзини деякі продукти? (виберіть так/т чи ні/н): ')
    product_all_removal_flag = product_all_removal_flag.lower()

    if product_all_removal_flag == 'так' or product_all_removal_flag == 'т':
        # 5 запросів на видалення
        for i in range(5):
            product_number = input(f"Вкажіть порядковий номер продукту, який потрібно видалити "
                                   f"(от 1 до {len(grocery_list)}): ")
            product_removal(product_number)
            print_current_products()

        # Перевірка порожній кошик чи ні після видалення.
        if len(grocery_list) == 0:
            # Порожній кошик після видалення, додайте продукти.
            add_list = input("Кошик порожній, додайте продукти, використовуйте пробіл як роздільник: ").split()
            grocery_list = add_products(grocery_list, add_list)
            print_current_products()
            print("До побачення!")
        else:
            # Не порожній кошик після видалення, до побачення.
            print("До побачення!")

    else:
        # Бажаєте видалити з корзини деякі продукти? - Ні:
        print(f"{str(grocery_list).strip('[]')}\nДо побачення!")

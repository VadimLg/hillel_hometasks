# Задача 1
#
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл,
# точна кількість не вказана. Вам потрібно до вартості покупок додати 6,5 відсотки податків.
#
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і
# потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.

price_str_list = input("Вкажіть вартість покупок, використовуйте пробіл як роздільник: ").split()

price_float_list = []

for i in price_str_list:
    price_float_list.append(float(i) + float(i) * 6.5 / 100)

coupon = input('У вас є купон на скидку? (введіть "так/т" чи "ні/н"): ')
coupon = coupon.lower()

if coupon == 'так' or coupon == 'т':
    coupon_type = input('Купон на суму чи відсоток? (введіть відповідно "сума/с" або "відсоток/в"): ')
    coupon_type = coupon_type.lower()
    if coupon_type == 'сума' or coupon_type == 'с':
        coupon_sum = float(input('Введіть суму знижки: '))
        result = sum(price_float_list) - coupon_sum
    elif coupon_type == 'в':
        percent = float(input('Введіть відсоток знижки: '))
        result = sum(price_float_list) - sum(price_float_list) * percent / 100
else:
    result = sum(price_float_list)

print(f"Підсумкова сума всіх продуктів: {round(result, 2)}")


# Задача 2
#
# Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in або while.

grocery_list = input("Напишіть продукти (5 або більше), які потрібно купити, використовуйте пробіл як роздільник: ").split()

if len(grocery_list) >= 5:
    # Відображає список доданих продуктів.
    print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")
    product_all_removal_flag = input('Бажаєте видалити з корзини деякі продукти? (виберіть так/т чи ні/н): ')
    product_all_removal_flag = product_all_removal_flag.lower()

    if product_all_removal_flag == 'так' or product_all_removal_flag == 'т':
        # 5 запросів на видалення
        for i in range(5):
            product_number = input(f"Вкажіть порядковий номер продукту, який потрібно видалити (от 1 до {len(grocery_list)}): ")
            grocery_list.pop(int(product_number) - 1)
            if len(grocery_list) > 0:
                print(f"Зараз у кошику такі продукти: {str(grocery_list).strip('[]')}")

        # Перевірка порожній кошик чи ні після видалення.
        if len(grocery_list) == 0:
            # Порожній кошик після видалення, додайте продукти.
            add_list = input("Кошик порожній, додайте продукти, використовуйте пробіл як роздільник: ").split()
            grocery_list = grocery_list + add_list
            print(f"У кошику тепер є такі продукти: {str(grocery_list).strip('[]')}\nДо побачення!")
        else:
            # Не порожній кошик після видалення, до побачення.
            print(f"У кошику є такі продукти: {str(grocery_list).strip('[]')}\nДо побачення!")

    else:
        # Бажаєте видалити з корзини деякі продукти? - Ні:
        print(f"У кошику є такі продукти: {str(grocery_list).strip('[]')}\nДо побачення!")


# Задача 3
#
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована. Використовуйте цикл while.

# Правильний ПІН-код
pin = 1234
# Максимальна кількість спроб введення ПІН-коду
attempt_pin = 3
print("Введіть ПІН-код, всього 3 спроби.")

while attempt_pin > 0:
    pin_in = int(input(f"{4 - attempt_pin}-я спроба: "))
    attempt_pin -= 1
    if pin != pin_in :
        print(f"Введено неправильний ПІН-код!")
        if attempt_pin == 0:
            print("Карта заблокована.")
    else:
        print("ПІН-код правильний!")
        break


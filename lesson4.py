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

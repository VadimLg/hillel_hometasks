# 1 Арифметичні операції:
# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.
print('1 Арифметичні операції:')

a_1 = int(input('Введите первое число: '))
b_1 = int(input('Введите второе число: '))

print('Сумма: ', a_1 + b_1)
print('Разность: ', a_1 - b_1)
print('Произведение: ', a_1 * b_1)
print('Деление:: ', a_1 / b_1, end = '\n\n')


# 2 Залишок від ділення:
# Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.
print('2 Залишок від ділення:')

a_2 = int(input('Введите первое число: '))
b_2 = int(input('Введите второе число: '))

print('Остаток от деления: ', a_2 % b_2, end = '\n\n')

# 3 Цілочисельне ділення:
# Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.
print('3 Цілочисельне ділення:')

a_3 = int(input('Введите первое число: '))
b_3 = int(input('Введите второе число: '))

print('Целочисленное деление: ', a_3 // b_3, end = '\n\n')


# 4 Перетворення стрічки у число:
# Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.
print('4 Перетворення стрічки у число:')

a_4 = int(input('Введите числовой ряд: '))
print('Строка "', a_4, '" преобразована в число, тип:', type(a_4), end = '\n\n')


# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.
print('5 Стрічкова конкатенація + математика:')

a_5 = input('Введите первое число: ')
b_5 = input('Введите второе число: ')

s_int_5 = int(a_5) + int(b_5)
s_str_5 = a_5 + b_5

print('Сумма чисел: ', s_int_5)
print('Конкатенация строк: ', s_str_5, end = '\n\n')


# 6 Вік користувача:
# Запитати у користувача його рік народження, ім'я та який зараз рік (три змінні)
# та вивести на екран два прінти: ім'я та скільки років користувачу.
print('6 Вік користувача:')

year_of_birth_6 = int(input('Введите год рождения: '))
username_6 = input('Введите Ваше имя: ')
this_year_6 = int(input('Введите текущий год: '))
user_age_6 = this_year_6 - year_of_birth_6
if (user_age_6 % 10 == 1) and (user_age_6 != 11) and (user_age_6 != 111):
    print_age_6 = 'год'
elif (user_age_6 % 10 > 1) and (user_age_6 % 10 < 5) and (user_age_6 != 12) and (user_age_6 != 13) and (user_age_6 != 14):
    print_age_6 = 'года'
else:
    print_age_6 = 'лет'
print(username_6,', ваш возраст:', user_age_6, print_age_6, end = '\n\n')


# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.
print('7 Перевод з цельсія в фаренгейт:')

temperature_in_celsius_7 = int(input ('Введите температуру в цельсиях: '))
temperature_in_fahrenheit_7 = temperature_in_celsius_7 * 9 / 5 + 32

print('Температура в фарингейтах: ', temperature_in_fahrenheit_7, end = '\n\n')


# 8 Перевод з фаренгейта в цельсій:
# Напишіть програму, яка запитує в користувача кількість градусів в фаренгейтах і повертає в цельсіях.
# Вам може здатися, що ця задача така ж, як попередня, але будьте уважні і перевірте результат вручну.
print('8 Перевод з фаренгейта в цельсій:')

temperature_in_fahrenheit_8 = int(input ('Введите температуру в цельсиях: '))
temperature_in_celsius_8 = 5 * (temperature_in_fahrenheit_8 - 32) / 9

print('Температура в цельсиях: ', temperature_in_celsius_8, end = '\n\n')


# 9 Теорема Піфагора:
# Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)
print('9 Теорема Піфагора:')

leg_1_9 = int(input('Введите первый катет треугольника: '))
leg_2_9 = int(input('Введите второй катет треугольника: '))

hypotenuse_9 = (leg_1_9 ** 2 + leg_2_9 ** 2) ** (1/2)
print('Длина гипотенузы: ', hypotenuse_9)
if leg_1_9 == leg_2_9:
    print('Прямоуголиный треугольник - равнобедренный')
else:
    print('Прямоуголиный треугольник - не равнобедренный')


# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.
print('10 Школярі та яблука:')

number_of_schoolchildren_10 = 0
while (number_of_schoolchildren_10 <= 0 or number_of_schoolchildren_10 > 10000):
    number_of_schoolchildren_10 = int(input('Введите кол-во школьников (положительное число больше нуля до 10000): '))

number_of_apples_10 = 0
while (number_of_apples_10 <= 0 or number_of_apples_10 > 10000 or number_of_apples_10 < number_of_schoolchildren_10):
    number_of_apples_10 = int(input('Введите кол-во яблок (положительное число, не меньшее кол-ва школьников до 10000): '))

number_of_apples_for_a_schoolchild_10 = number_of_apples_10 // number_of_schoolchildren_10
number_of_apples_in_the_basket_10 = number_of_apples_10 % number_of_schoolchildren_10

print('Каждому школьнику достанется яблок: ', number_of_apples_for_a_schoolchild_10, 'шт.')
print('В корзине останется яблок: ', number_of_apples_in_the_basket_10, 'шт.', end = '\n\n')


# 11 Магазин канцелярських товарів
# Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# Вхідні дані
# просимо користувача ввести три змінні
# кожне з яких не перевищує 109.
# Вихідні дані
# виведіть одне ціле число – вартість покупки в гривнях.
# приклад для перевірки програми 1
# ввів: 1 1 1
# отримав: 20
print('11 Магазин канцелярських товарів:')

pencil_cost_11 = 3
pen_cost_11 = 3 + 2
marker_cost_11 = pen_cost_11 + 7

number_of_pencils_11 = 0
while (number_of_pencils_11 <=0 or number_of_pencils_11 > 109):
    number_of_pencils_11 = int(input('Введите кол-во карандашей (от 1 до 109): '))

number_of_pens_11 = 0
while (number_of_pens_11 <=0 or number_of_pencils_11 > 109):
    number_of_pens_11 = int(input('Введите кол-во ручек (от 1 до 109): '))

number_of_markers_11 = 0
while (number_of_markers_11 <=0 or number_of_markers_11 > 109):
    number_of_markers_11 = int(input('Введите кол-во фломастеров (от 1 до 109): '))

price_pencils_11 = number_of_pencils_11 * pencil_cost_11
price_pencs_11 = number_of_pens_11 * pen_cost_11
price_markers_11 = number_of_markers_11 * marker_cost_11
purchase_price_11 = price_pencils_11 + price_pencs_11 + price_markers_11

print('Стоимость покупки:', purchase_price_11, 'грн.', end = '\n\n')


# 12 Циферблад
# Запитайте в користувача скільки хвилин пройшло з початку доби.
# Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# приклад для перевірки програми 1
# користувач ввів:150
# користувач отримує: 2, 30
# приклад для перевірки програми 2
# користувач ввів:1441
# користувач отримує: 0, 1
print('12 Циферблат:')

number_of_minutes_12 = 0
while (number_of_minutes_12 <=0 or number_of_minutes_12 > 1140):
    number_of_minutes_12 = int(input('Введите кол-во минут от начала суток, от 1 до 1140 (макс. число мин. в сутках): '))

hours_12 = number_of_minutes_12 // 60
minutes_12 = number_of_minutes_12 % 60

print('С начала суток прошло', hours_12,'ч.,', minutes_12, 'мин.', end = '\n\n')


# 13 Журавлики
# Петро, Катя та Сергій роблять з паперу журавликів. Разом вони зробили S журавликів.
# Скільки журавликів зробила кожна дитина, якщо відомо, що Петро та Сергій зробили однакову кількість журавликів,
# а Катя зробила в два рази більше журавликів, ніж Петро та Сергій разом.
# Вхідні дані
# Юзер вводить загальну кількість журавликів. Отримує три значення скільки зробив кожен (Петро, Катя та Сергій).
print('13 Журавлики:')

number_of_cranes_13 = 0
while (number_of_cranes_13 < 6 or (number_of_cranes_13 % 6) != 0):
    number_of_cranes_13 = int(input('Введите кол-во журавликов, кратное 6 (мин. возможное число): '))

petya_13 = sergey_13 = number_of_cranes_13 / 6
katya_13 = 2 * (petya_13 + sergey_13)

print('Петя сделал журавликов:', int(petya_13), 'шт.')
print('Катя сделала журавликов:', int(katya_13), 'шт.')
print('Сергей сделал журавликов:', int(sergey_13), 'шт.', end = '\n\n')


# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба сплатити податків за 3 місяці. Не забудьте ЄСВ(4422)
print('14 Податки:')

esb_14 = 4422

while True:
    salary_14 = float(input('Введите зарплату (не отрицательное число): '))
    if salary_14 >=0:
        break
while True:
    percent_14 = float(input('Введите процент, который нужно оплатить (не отрицательное число от 0 до 100): '))
    if (percent_14 >=0 and percent_14 <= 100):
        break

taxes_for_the_quarter_14 = (salary_14 / 100 * percent_14) * 3
if (taxes_for_the_quarter_14 < esb_14):
    print('Сумма налогов будет равна ЄСВ (мінімальний страховий внесок) за квартал: ', esb_14, 'грн.')
else:
    print('Налоги за квартал составляют: ', taxes_for_the_quarter_14, 'грн.')
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
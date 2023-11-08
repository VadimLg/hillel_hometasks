# Задача 1
#
# Напишіть программу "Касир в кінотеватрі", яка попросить користувача ввести свій вік
# (можна використати константу або функцію input(), на екран має бути виведено лише одне повідомлення).
#
# якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
#
# якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
#
# якщо від 16 до 65 то зробіть якесь вітальне повідомлення, на ваш розсуд.
# якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"

print('Задача 1. Касир в кінотеватрі')
age = int(input('Ведите свой возраст (полных лет): '))
if age <= 0:
    print('Invalid number entered!')
elif age > 0 and age < 7:
    print('Де твої батьки?')
elif age >= 7 and age < 16:
    print('Це фільм для дорослих!')
elif age >= 16 and age < 65:
    print('Hi man!')
else:
    print('Покажіть пенсійне посвідчення!')


# Задача 2
#
# Текстова в чому різниця між is та ==?
print("""
Задача 2
    Оператор is перевіряє ідентичність самих об'єктів. 
Його використовують, щоб переконатися, що змінні вказують на той самий об'єкт у пам'яті
    Оператор == перевіряє рівність значень двох об'єктів

Приклад 1 у консолі:
>>>short_str_1 = 'hello'
>>>short_str_2 = 'hello'
>>>short_str_1 == short_str_2
True
>>>short_str_1 is short_str_2
True

Приклад 2 у консолі:
>>>short_int_1 = 111
>>>short_int_2 = 111
>>>short_int_1 == short_int_2
True
>>>short_int_1 is short_int_2
True

Приклад 3 у консолі:
>>>long_str_1 = 'Текстова в чому різниця між is та ==?'
>>>long_str_2 = 'Текстова в чому різниця між is та ==?'
>>>long_str_1 == long_str_2
True
>>>long_str_1 is long_str_2
False

Приклад 4 у консолі:
>>>long_int_1 = 1111
>>>long_int_2 = 1111
>>>long_int_1 == long_int_2
True
>>>long_int_1 is long_int_2
False
""")

# Задача 3
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт,
# а можуть бути в стр). Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає
# і повертає результат перемножений на три. якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.

print('Задача 3')
number_str_1 = input('Enter number 1: ')
number_str_2 = input('Enter number 2: ')
string_or_number = input('Is it a string or a number? (Y/N)')

string_or_number = string_or_number.lower()

if string_or_number == 'y' or string_or_number == 'yes':
    result = number_str_1 + number_str_2
    print('Result =', result)
elif string_or_number == 'n' or string_or_number == 'no':
    result = (int(number_str_1) + int(number_str_2)) * 3
    print('Result =', result)
else:
    print('An incorrect answer was entered to the question "Is it a string or a number? (Y/N)"')
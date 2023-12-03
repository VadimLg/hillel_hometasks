from datetime import datetime


print("Задача 1")
# додайте requirements.txt на ваш гіт

print("Cтворено requirements.txt і викладено на git\n")



print("Задача 2")
# Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)

try:
    dividend_number = int(input("Введіть ціле число, яке ділитимемо (якщо ввести символ, буде помилка): "))
    divider_number = int(input("Введіть число, на яке ділитимемо (якщо ввести 0 або символ, буде помилка): "))
except (ValueError, NameError):
    print("! Замість числа було введено символ\n")
except:
    print("! Помилка введення даних\n")


def dividing_numbers(n_1: int, n_2: int) -> float:
    try:
        print(f"Результат обчислення = {round(n_1 / n_2, 5)}\n")
    except ZeroDivisionError:
        print("! На нуль у пайтоні ділити не можна\n")
    except:
        print("! Помилка роботи функції dividing_numbers\n")


try:
    dividing_numbers(dividend_number, divider_number)
except NameError:
    print("! Помилка вхідних даних функції при виклику функції dividing_numbers\n")
except:
    print("! Помилка виклику функції dividing_numbers\n")



print("Задача 3")
# зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами

print('Тест кейси у файлі "lesson9_test_parametrize.py"\n')

def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    "Функція з трьома параметрами"
    result = number_1 + number_2 + number_3
    return result


print("Задача 4")
# перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює

def func_decorator_time(func):
    def wrapper(*arg, **kwarg):
        start_time = datetime.now()
        result = func(*arg, **kwarg)
        delta_time = datetime.now() - start_time
        print("Час виконання функції: ", delta_time)
        return result

    return wrapper


@func_decorator_time
def slow_algorithm(a: int, b: int) -> int:
    "Повільний алгоритм Евкліда"
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@func_decorator_time
def fast_algorithm(a: int, b: int) -> int:
    "Швидкий алгоритм Евкліда"
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


print("Повільний алгоритм Евкліда")
res_slow_algorithm = slow_algorithm(2, 10000000)
print(f"Найбільший спільний дільник: {res_slow_algorithm}\n")

print("Швидкий алгоритм Евкліда")
res_fast_algorithm = fast_algorithm(2, 10000000)
print(f"Найбільший спільний дільник: {res_fast_algorithm}")

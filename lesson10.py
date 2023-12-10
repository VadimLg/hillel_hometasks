print("Задача 1")
# 1) Напишіть 10 тестів(можна що б просто повертали Тру(щоб проходили)) імена тестів повині йти підряд
# test_1, test_2 ... . Повішайти на них три декоратора old, main, new. кожен декоратор повинен бути на 3 функціях
# на одній з функцій повино бути повішано два декоратора old i main.
# додайти їх в python.ini що б були правильні виводи
#
print("Тести знаходяться у файлі test_lesson10.py")
#
print("Прогони:")
#
print("1) всі тексти де немає лейби old")
print('У вікні Terminal виконуємо: pytest -m "not old" -v test_lesson10.py')
print("Скріншот у файлі result_of_run_1.png", end="\n\n")
#
print("2) тест де пересікаються old i main")
print('У вікні Terminal виконуємо: pytest -m "old and main"" -v test_lesson10.py')
print("Скріншот у файлі result_of_run_2.png", end="\n\n")
#
print("3) тести з маркерами main, new")
print('У вікні Terminal виконуємо: pytest -m "main or new"" -v test_lesson10.py')
print("Скріншот у файлі result_of_run_3.png", end="\n\n")


print("Задача 2")
# Візьміть задачу з минулого уроку(
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
# ) модернізуйте її так що кожний раз коли ми її запускаємо те що ми туди передаєм та результат повинно записуватись в файл log.txt
# Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
# Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,
# тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:
# функція з минулого уроку
# функція що записую текст
# і декоратор

print('Тест кейси у файлі "test_lesson10_2.py"\n')

def func_decorator(func):
    def wrapper(*arg, **kwarg):
        log_text = f"Input data: {str(arg)} "
        logging_to_file(log_text)
        result = func(*arg, **kwarg)
        log_text = f"Result: {str(result)}\n"
        logging_to_file(log_text)
        return result

    return wrapper


@func_decorator
def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    "Функція з трьома параметрами"
    result = number_1 + number_2 + number_3
    return result


def logging_to_file(text_str: str):
    with open("log.txt", "a") as file:
        file.write(text_str)
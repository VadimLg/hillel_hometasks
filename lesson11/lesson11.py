print("Задача 1")


# Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі, перший метод який буде вітатись і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі).
# Вивідіть дві функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.

class StudentClass:
    name = "Jerry"
    list_ratings = [1, 2, 3, 4, 5]

    def get_hello(self):
        print(f"Привіт, мене звуть {self.name}!")

    def get_ratings(self):
        print(f"Мої оцінки {self.list_ratings}")


Student_1 = StudentClass()

Student_2 = StudentClass()
Student_2.name = "Tom"
Student_2.list_ratings = [6, 7, 8, 9, 10]

Student_1.get_hello()
Student_1.get_ratings()

Student_2.get_hello()
Student_2.get_ratings()


print("\nЗадача 2")
# Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
# Запустіть їх за домогою pytest-xdist ліби в 5 потоків.
# Запустіть цей ваш унікальний тест з маркером -k
# додайте скірншоти виконання(не забудьте додавати -v, що б я бачив що ви проганяли) і біля скріншотів
# пропишіть команди які ви використовували.

print('У вікні Terminal виконуємо: pytest test_lesson11.py -n=5 -v')
print("Скріншот у файлі lesson11_result_of_run1.png", end="\n\n")

print('У вікні Terminal виконуємо: pytest -k "unique" test_lesson11.py -v')
print("Скріншот у файлі lesson11_result_of_run2.png", end="\n\n")


print("Задача 3")
print("обновіть requirements.txt")
print("requirements.txt - оновлено")

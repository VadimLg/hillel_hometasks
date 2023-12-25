# 1) Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2

if __name__ == "__main__":
    print("Задача 1")
    my_list = [i for i in range(34,122) if (i % 2 == 0 and i % 3 == 0)]
    print(my_list)

# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.

class MyCalculator:

    def sum(self, first_number: int | float, second_number: int | float) -> int | float:
        """Плюс"""
        return first_number + second_number

    def sub(self, first_number: int | float, second_number: int | float) -> int | float:
        """Мінус"""
        return first_number - second_number

    def div(self, first_number: int | float, second_number: int | float) -> int | float:
        """Ділення"""
        return first_number / second_number

    def mul(self, first_number: int | float, second_number: int | float) -> int | float:
        """Множення """
        return first_number * second_number

    @staticmethod
    def hi_message():
        print("Привіт я калькулятор")


if __name__ == "__main__":
    print("Задача 2")
    MyCalculator.hi_message()

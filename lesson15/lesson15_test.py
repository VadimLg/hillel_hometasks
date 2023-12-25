from datetime import datetime
from lesson15 import MyCalculator
import pytest

# Задача 3
# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
#
#  Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл коли ми запустили тест
#
#  та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили
#
#  використайте вже відому вам бібліотеку дататайм

class TestCalculator:
    @classmethod
    def setup_class(cls):
        with open("log.txt", "a") as file:
            file.write(f"Start test at {datetime.now()}, ")

    @classmethod
    def teardown_class(cls):
        with open("log.txt", "a") as file:
            file.write(f"end test at {datetime.now()}\n")

    @pytest.mark.parametrize("num_1, num_2, result", [
        (1, 2, 3),
        (1, -1, 0),
        (1.01, 2.02, 3.03),
        (1, 999999, 1000000),
        (-1, -101, -102)
    ])
    def test_sum(self, num_1, num_2, result):
        obj_test_sum = MyCalculator()
        assert round(obj_test_sum.sum(num_1, num_2), 2) == result

    @pytest.mark.parametrize("num_1, num_2, result", [
        (2, 1, 2),
        (1, -1, -1),
        (10.99, 1, 10.99),
        (0, 1, 0),
        (-1, -1, 1)
    ])
    def test_div(self, num_1, num_2, result):
        obj_test_div = MyCalculator()
        assert round(obj_test_div.div(num_1, num_2), 2) == result

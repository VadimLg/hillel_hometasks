import pytest


# Задача 1
# перевірити поля "icon_url" чи він не пусти + чи це картинка,  - 2 теста
# перевірити чи є ключ "value"  і перевірити його значення - 2 теста
@pytest.mark.usefixtures("fixture_ramdom")
class TestRandom:
    def test_icon_value_is_not_None(self):
        assert len(self.response.json()["icon_url"]) > 0, "Перевіряємо, що значення поля \"icon_url\" не пусте"

    def test_icon_is_image(self):
        img_expansion = ("png", "jpg")
        assert self.response.json()["icon_url"].split(".")[-1] in img_expansion, ("Перевіряємо, що в значенні поля "
                                                                                  "\"icon_url\" посилання на картинку")

    def test_field_value(self):
        assert "value" in self.response.json(), "Перевіряємо, що є ключ \"value\""

    def test_validation_value(self):
        assert self.response.json()["value"].count(
            "Chuck Norris"), "Перевіряємо, що Чак Норріс згадується в тексті жарту"


# Задача 2
# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести

@pytest.mark.usefixtures("fixture_query")
class TestQuery:
    def test_status_code(self):
        assert self.status_code == 200, "Тест на статус код"

    def test_number_of_jokes(self):
        assert len(self.response.json()["result"]) == 16, "Тест на кількість жартів, на запит \"fishing\"(рибалка)"

    def test_2(self):
        joke_template = "Chuck Norris enjoys big game deep sea fishing. He generally uses a live moose for bait."
        joke_list = []
        for x in self.response.json()["result"]:
            joke_list.append(x["value"])
        assert joke_template in joke_list, ("Тест на сам жарт. У респонсі шукаємо жарт про лося: \"Chuck Norris enjoys "
                                            "big game deep sea fishing. He generally uses a live moose for bait.\"")

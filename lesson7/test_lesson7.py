from lesson7.lesson7_functions import list_sorting_increase_int, list_sorting_descending_int, list_sorting_increase_str_lenght

list_int = [34, 456, 11, 12, -100, 77, 100, 35, 100.0, 100]
list_str = ['груша', 'грушаa', 'банан',  'яблуко', 'диня', "слива", "апельсин"]

def test_sorting_increase_int():
    list_out = list_sorting_increase_int(list_int)
    assert list_out == [-100, 11, 12, 34, 35, 77, 100, 100.0, 100, 456], "Сортування за зростанням"

def test_sorting_descending_int():
    list_out = list_sorting_descending_int(list_int)
    assert list_out == [456, 100, 100.0, 100, 77, 35, 34, 12, 11, -100], "Сортування за зменшенням"

def test_sorting_increase_str_lenght():
    list_out = list_sorting_increase_str_lenght(list_str)
    assert list_out == ['диня', 'груша', 'банан', 'слива', 'грушаa', 'яблуко', 'апельсин'], "Сортування за кількістю букв у слові"

import pytest
from lesson10.lesson10 import add_three_numbers


# solution 1
def test_1_add_three_numbers_solution_1():
    assert add_three_numbers(1, 2, 3) == 6, "positive 1"


def test_2_add_three_numbers_solution_1():
    assert add_three_numbers(3, 2, 1) == 6, "positive 2"


def test_3_add_three_numbers_solution_1():
    assert add_three_numbers(-1, 2, 3) == 6, "failed test 1"


def test_4_add_three_numbers_solution_1():
    assert add_three_numbers(3, 2, -1) == 0, "failed test 2"


# solution 2
@pytest.mark.parametrize("num_1, num_2, num_3, result", [
    pytest.param(1, 2, 3, 6, id="positive 1"),
    pytest.param(3, 2, 1, 6, id="positive 2"),
    pytest.param(-1, 2, 3, 6, id="failed test 1"),
    pytest.param(3, 2, -1, 0, id="failed test 2")])
def test_add_three_numbers_solution_2(num_1, num_2, num_3, result):
    assert add_three_numbers(num_1, num_2, num_3) == result


# solution 3

list_test = [(1, 2, 3, 6), (3, 2, 1, 6), (-1, 2, 3, 6), (3, 2, -1, 0)]


@pytest.mark.parametrize("num_1, num_2, num_3, result", list_test)
def test_add_three_numbers_solution_3(num_1, num_2, num_3, result):
    assert add_three_numbers(num_1, num_2, num_3) == result

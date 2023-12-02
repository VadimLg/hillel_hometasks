import pytest
from lesson9 import add_three_numbers

@pytest.mark.parametrize("num_1, num_2, num_3, result", [
    pytest.param(1, 2, 3, 6, id="positive 1"),
    pytest.param(3, 2, 1, 6, id="positive 2"),
    pytest.param(-1, 2, 3, 6, id="failed test 1"),
    pytest.param(3, 2, -1, 0, id="failed test 2")])
def test_add_three_numbers(num_1, num_2, num_3, result):
    assert add_three_numbers(num_1, num_2, num_3) == result
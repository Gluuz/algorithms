import pytest
from binary_search import binary_search


test_cases = [
    ([1, 3, 5, 7, 9], 3, 1),  # Elemento está na lista
    ([1, 3, 5, 7, 9], 9, 4),  # Elemento está na lista
    ([1, 3, 5, 7, 9], 1, 0),  # Elemento está na lista
    ([1, 3, 5, 7, 9], 6, None),  # Elemento não está na lista
    ([], 10, None),  # Lista vazia
    ([1, 2, 3, 4, 5], 6, None),  # Elemento não está na lista
]

@pytest.mark.parametrize("lst, item, expected", test_cases)
def test_binary_search(lst, item, expected):
    assert binary_search(lst, item) == expected
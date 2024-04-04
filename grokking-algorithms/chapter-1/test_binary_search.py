import pytest
from binary_search import binary_search


test_cases = [
    ([1, 3, 5, 7, 9], 3, 1),  # Element is in the list
    ([1, 3, 5, 7, 9], 9, 4),  # Element is in the list
    ([1, 3, 5, 7, 9], 1, 0),  # Element is in the list
    ([1, 3, 5, 7, 9], 6, None),  # Element is not in the list
    ([], 10, None),  # Empty list
    ([1, 2, 3, 4, 5], 6, None),  # Element is not in the list
]

@pytest.mark.parametrize("lst, item, expected", test_cases)
def test_binary_search(lst, item, expected):
    assert binary_search(lst, item) == expected
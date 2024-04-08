from quicksort import sum, count, max, quicksort

# Test cases for the sum function
def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([7]) == 7
    assert sum([]) == 0

# Test cases for the count function
def test_count():
    assert count([1, 2, 3]) == 3
    assert count([]) == 0

# Test cases for the max function
def test_max():
    assert max([1, 5, 2, 0, 100]) == 100
    assert max([]) == "error: list must contain at least one number!"
    assert max([9]) == 9

# Test case for the quicksort function
def test_quicksort():
    assert quicksort([2, 1, 109, 20, 40, 10]) == [1, 2, 10, 20, 40, 109]
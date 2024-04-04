import pytest
from selection_sort import findSmallest, selectionSort

# Tests for the findSmallest function
def test_findSmallest():
    assert findSmallest([5, 3, 6, 2, 10]) == 3  # smallest value is at position 3
    assert findSmallest([1, 2, 3, 4, 5]) == 0  # smallest value is at position 0
    assert findSmallest([10, 8, 6, 4, 2]) == 4  # smallest value is at position 4
    assert findSmallest([-5, -3, -6, -2, -10]) == 4  # smallest value is at position 4

# Tests for the selectionSort function
def test_selectionSort():
    assert selectionSort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]  # sorted
    assert selectionSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # already sorted
    assert selectionSort([10, 8, 6, 4, 2]) == [2, 4, 6, 8, 10]  # sorted in reverse
    assert selectionSort([-5, -3, -6, -2, -10]) == [-10, -6, -5, -3, -2]  # sorted
    assert selectionSort([]) == []  # empty list

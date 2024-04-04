
from countdown import countdown
#Test the countdown function

def test_countdown():
    assert countdown(5) == [5, 4, 3, 2, 1]  # Test with input 5
    assert countdown(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Test with input 10
    assert countdown(1) == [1]  # Test with input 1
    assert countdown(0) == []  # Test with input 0
    assert countdown(-1) == []  # Test with negative input
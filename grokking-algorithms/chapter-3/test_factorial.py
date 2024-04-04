from factorial import factorial

# Test the fact function
def test_fact():
    assert factorial(1) == 1  # Test with input 1
    assert factorial(5) == 120  # Test with input 5
    assert factorial(10) == 3628800  # Test with input 10
    assert factorial(20) == 2432902008176640000  # Test with input 20
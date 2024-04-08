from hashtable import check_voter

# Test case for the check_voter function
def test_check_voter():
    # Test with a new voter
    assert check_voter("Alice") == "let them vote!"

    # Test with the same voter again
    assert check_voter("Alice") == "kick them out!"

    # Test with a different voter
    assert check_voter("Bob") == "let them vote!"

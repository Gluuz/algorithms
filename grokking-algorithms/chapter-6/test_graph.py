from graph import search_mango_seller

def test_search_mango_seller():
    assert search_mango_seller("you") is True
    assert search_mango_seller("bob") is False
    assert search_mango_seller("alice") is False
    assert search_mango_seller("claire") is True
    assert search_mango_seller("anuj") is False
    assert search_mango_seller("peggy") is False
    assert search_mango_seller("thom") is True
    assert search_mango_seller("jonny") is False
from main import valid_password
def test_password():
    assert valid_password("ab")
    assert valid_password("abc") 
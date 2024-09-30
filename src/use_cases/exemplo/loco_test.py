from .loco import static_url_funct

def test_integer_input():
    assert static_url_funct(333) == 333

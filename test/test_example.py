def test_first():
    value= 1+2
    print(value)
    assert value == 3

def test_second():
    assert "hello" == "hi"

def test_third():
    assert "hello" in "hello, World"

def test_four():
    assert len("hello") == 4




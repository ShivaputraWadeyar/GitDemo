import pytest


def test_meths(setup):
    msg = "Hello"
    assert msg == "Hello","Test failed,msg not matched with"
    print(msg)

def test_Creditcard():
    a = 4
    b = 5
    assert a+2 == 6, "Addition do not match"

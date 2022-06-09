import pytest


def test_firsttest(setup):
    print("Hello Shiva")


def test_greetCreditcard(setup):
    print("Good morning Shiva")

@pytest.mark.usefixtures
def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])



import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_firstprogram(self):
        print("First program")

    def test_secondprogram(self):
        print("second program")

    def test_thirdprogram(self):
        print("third program")

    def test_forthprogram(self):
        print("fourth program")
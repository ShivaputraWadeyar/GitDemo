import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataload():
    print("user data is created here")
    return  ["Rahul","shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("Chrome","Raj"),("Firefox","Shiv"), ("ie","Pot")])
def crossbrowser(request):
    return request.param

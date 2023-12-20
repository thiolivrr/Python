import pytest
import employee

@pytest.fixture
def worker():
    John = employee.Employee('John', 'Doe', 15000)
    return John

def test_give_default_raise(worker):
    res = worker.give_raise()
    assert res == 'Seu sálario agora é 20000'

def test_give_custom_raise(worker):
    res = worker.give_raise(15000)
    assert res == 'Seu sálario agora é 30000'




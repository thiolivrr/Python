import employee

def test_give_default_raise():
    william = employee.Employee('william', 'fernandes', 15000)
    res = william.give_raise()
    assert res == 'Seu sálario agora é 20000'

def test_give_custom_raise():
    william = employee.Employee('william', 'fernandes', 15000)
    res = william.give_raise(15000)
    assert res == 'Seu sálario agora é 30000'




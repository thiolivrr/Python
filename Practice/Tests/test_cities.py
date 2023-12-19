from city_functions import location

def test_city_country():
    place = location("Ottawa, Canadá")
    assert place == ("Otawwa, Canadá.")
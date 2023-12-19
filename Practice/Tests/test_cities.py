from city_functions import location

def test_city_country():
    place = location("Quebec, Canadá")
    assert place == ("Quebec, Canadá.")
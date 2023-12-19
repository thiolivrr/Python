import pytest

from city_functions import location

def test_city_country():
    place = location("Quebec","Canadá")
    assert place == "Quebec, Canadá"

def test_city_country_population():
    place = location("Quebec","Canadá", 50000)
    assert place == "Quebec, Canadá - population 50000"